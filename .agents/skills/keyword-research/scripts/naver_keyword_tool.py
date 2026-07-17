#!/usr/bin/env python3
import base64
import argparse
import hashlib
import hmac
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

PATH = "/keywordstool"
REQUIRED = (
    "NAVER_SEARCHAD_API_KEY",
    "NAVER_SEARCHAD_SECRET_KEY",
    "NAVER_SEARCHAD_CUSTOMER_ID",
)


def load_dotenv(path=Path(".env")):
    if not path.is_file():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.removeprefix("export ").split("=", 1)
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        os.environ.setdefault(key.strip(), value)


def signature(timestamp, secret):
    message = f"{timestamp}.GET.{PATH}".encode()
    return base64.b64encode(hmac.new(secret.encode(), message, hashlib.sha256).digest()).decode()


def count_estimate(value):
    text = str(value).replace(",", "").strip()
    return 5 if "<" in text else int(float(text or 0))


def normalize(value):
    return "".join(str(value).lower().split())


def keyword_data(query, item):
    pc = item.get("monthlyPcQcCnt", 0)
    mobile = item.get("monthlyMobileQcCnt", 0)
    return {
        "keyword": item.get("relKeyword", ""),
        "exact_match": normalize(item.get("relKeyword")) == normalize(query),
        "monthly_pc": pc,
        "monthly_mobile": mobile,
        "monthly_total_estimate": count_estimate(pc) + count_estimate(mobile),
        "competition": item.get("compIdx"),
    }


def fetch(keyword, expand=False, limit=20, min_volume=0):
    missing = [key for key in REQUIRED if not os.environ.get(key)]
    if missing:
        raise RuntimeError("Missing environment variables: " + ", ".join(missing))

    timestamp = str(round(time.time() * 1000))
    query = urllib.parse.urlencode({"hintKeywords": normalize(keyword), "showDetail": 1})
    request = urllib.request.Request(
        f"https://api.searchad.naver.com{PATH}?{query}",
        headers={
            "X-Timestamp": timestamp,
            "X-API-KEY": os.environ["NAVER_SEARCHAD_API_KEY"],
            "X-Customer": os.environ["NAVER_SEARCHAD_CUSTOMER_ID"],
            "X-Signature": signature(timestamp, os.environ["NAVER_SEARCHAD_SECRET_KEY"]),
        },
    )
    with urllib.request.urlopen(request, timeout=10) as response:
        items = json.load(response).get("keywordList", [])

    keywords = [keyword_data(keyword, item) for item in items if item.get("relKeyword")]
    if not keywords:
        raise RuntimeError("No keyword data returned")

    if expand:
        unique = {normalize(item["keyword"]): item for item in keywords}
        candidates = [item for item in unique.values() if item["monthly_total_estimate"] >= min_volume]
        candidates.sort(key=lambda item: item["exact_match"], reverse=True)
        return {"query": keyword, "count": min(len(candidates), limit), "keywords": candidates[:limit]}

    match = next((item for item in keywords if item["exact_match"]), keywords[0])
    return {
        "query": keyword,
        "matched_keyword": match.pop("keyword"),
        **match,
    }


def main():
    if sys.argv[1:] == ["--self-test"]:
        assert normalize("  키워드 검증 ") == "키워드검증"
        assert count_estimate("< 10") == 5
        assert count_estimate("1,234") == 1234
        assert signature("1", "secret")
        rows = [
            keyword_data("테스트", {"relKeyword": "테스트", "monthlyPcQcCnt": 10, "monthlyMobileQcCnt": 20}),
            keyword_data("테스트", {"relKeyword": "테스트방법", "monthlyPcQcCnt": "< 10", "monthlyMobileQcCnt": 30}),
        ]
        assert rows[0]["exact_match"] and rows[1]["monthly_total_estimate"] == 35
        print("ok")
        return
    parser = argparse.ArgumentParser()
    parser.add_argument("keyword")
    parser.add_argument("--expand", action="store_true")
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--min-volume", type=int, default=0)
    args = parser.parse_args()
    if not 1 <= args.limit <= 50 or args.min_volume < 0:
        parser.error("--limit must be 1-50 and --min-volume must be non-negative")
    load_dotenv()
    try:
        print(json.dumps(fetch(args.keyword.strip(), args.expand, args.limit, args.min_volume), ensure_ascii=False, indent=2))
    except urllib.error.HTTPError as error:
        message = "rate limited" if error.code == 429 else f"HTTP {error.code}"
        raise SystemExit(f"Naver keyword tool failed: {message}") from None
    except (OSError, RuntimeError, ValueError) as error:
        raise SystemExit(f"Naver keyword tool failed: {error}") from None


if __name__ == "__main__":
    main()
