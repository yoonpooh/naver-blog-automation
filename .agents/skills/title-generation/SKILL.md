---
name: title-generation
description: Create exactly one high-click Korean informational blog title for the keyword most recently selected in the current thread. Use when the user asks for a title after keyword research or wants the best Naver Blog title for an established keyword, article angle, or evidence set.
---

# Title Generation

Create one search-aligned title without asking the user to repeat context already present in the thread.

## Context

1. Reuse the latest keyword-research result: keyword, opportunity type, article angle, and evidence.
2. Ask only for the keyword when no usable keyword exists in the conversation.
3. Treat supplied facts as claims to verify, not permission to invent a price, date, feature, benefit, review, or firsthand experience.

## Search Audit

1. Inspect the current Naver integrated and Blog results for the exact keyword and one natural query variant when browser access is available.
2. Review the first 10-20 visible titles. Identify the dominant promise, repeated wording, strong exact-match publishers, and the most useful unanswered question.
3. If exact-topic posts do not exist, treat that as a supply gap rather than a failure. Infer wording from Naver autocomplete, related searches, current news, official sources, and titles for the parent product or predecessor, while keeping claims limited to the exact topic.
4. Do not imitate an existing title closely. Compete by making the verified answer scope clearer.

## Selection

Generate 10-15 candidates internally across direct-answer, practical, comparison, and curiosity-led patterns. Do not show the candidate list.

Adapt to the opportunity:

- Breakout: place the exact new name early and pair it with the strongest verified immediate question, such as release timing, differences, price, or purchase method.
- Durable: phrase the recurring problem naturally and state the answer boundary clearly.
- Seasonal durable: include a year or season only when freshness materially changes the answer.

Score candidates internally:

- exact search-intent match and early keyword placement: 35%;
- clear reason to click: 25%;
- useful specificity: 20%;
- factual credibility: 15%;
- natural Korean readability: 5%.

## Guardrails

- Preserve the selected keyword exactly when natural and place it near the beginning.
- Prefer roughly 28-45 Korean characters, but never sacrifice clarity to hit a length target.
- Use one clear promise. Remove secondary details before making the title crowded.
- Avoid keyword repetition, unsupported superlatives, fake urgency, excessive punctuation, and expressions such as `shocking`, `must-see`, or `unconditionally`.
- Use `review`, `hands-on`, `price`, `benefit`, or `complete guide` only when the article evidence actually supports that promise.
- Reject a candidate when a strong current result already uses essentially the same wording and scope.

## Output

Write in Korean and return only:

```text
Recommended title: <one title>
```
