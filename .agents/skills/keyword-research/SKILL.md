---
name: keyword-research
description: Research Korean search demand through separate breakout and durable-demand candidate funnels, then recommend exactly one informational keyword with the best realistic traffic and Naver Blog ranking opportunity. Use parallel discovery, Naver SearchAd expansion, 6-12 month trend checks, intent clustering, and live blog-result audits when the user asks what keyword to write about or wants Codex to choose autonomously.
---

# Keyword Research

Recommend one informational keyword with the best evidence-backed traffic and ranking opportunity without asking the user to choose a subject.

## Opportunity Lanes

Research both lanes on every run. Do not prefer either lane by default.

- **Breakout:** newly launched products, services, features, policies, events, or named issues with fresh demand and sparse exact-intent blog coverage. The target pattern is a new model such as `HAKA H2`.
- **Durable:** informational queries with stable or predictably recurring demand over 6-12 months, meaningful monthly volume, and weak, stale, incomplete, or poorly matched blog results.

Include recurring seasonal queries in the durable lane only when the next demand window is approaching. Do not equate opportunity with the largest volume or the smallest total result count.

## Performance Priors

Use these as general tie-breakers, never as substitutes for live demand and supply evidence:

- Prefer newly searchable official names for products, models, services, features, policies, and events when exact-intent coverage is still sparse.
- Prefer clear follow-up intent such as price, release date, purchase or application method, availability, eligibility, usage, compatibility, differences, and precautions.
- Within breakout candidates, prefer names likely to retain follow-up searches after launch because sales, rollout, updates, or recurring usage questions continue.
- Keep sudden incidents and local issues eligible when people search an exact official name immediately after occurrence and reliable reporting supports a useful factual explainer; reject rumor-driven or tragedy-exploitative angles.
- Penalize broad news or generic technology summaries without a concrete user question, especially when official or major-news results already satisfy the intent.
- Reject restaurants, cafes, stores, travel stays, hands-on reviews, and other topics whose credible treatment depends on firsthand experience or original on-location photography.

## Agent Strategy

Use two subagents for every full recommendation when available:

- Naver scout: inspect Naver News, autocomplete, related searches, result pages, Naver Blog supply, and Naver DataLab.
- Trend scout: inspect Google Trends Korea, Pandarank, official launches, release notes, scheduled events, and established informational queries with stable or seasonal demand.
- Main agent: maintain both lanes, expand seeds, cluster intent, select a winner from each lane, audit finalists, and choose the final keyword.

Ask each scout for 12-20 candidates with at least six per lane. Require the observed signal or trend period, source URL, likely informational query, and apparent blog supply. Do not let scouts rank the final winner. Use no more than two subagents and do not duplicate research.

## Workflow

### 1. Discover broadly

1. Run both scouts in parallel and reuse the user's existing Chrome session when available.
2. Inspect breakout signals across the last few hours, 24 hours, 7 days, and 30 days. Inspect durable demand across 6-12 months and the same season in the previous year when available.
3. Merge at least 20 distinct seeds with at least 10 per lane when signals permit. Record the observation time or trend window and source for every seed.
4. Convert raw entities or headlines into likely informational follow-up queries, prioritizing actionable modifiers from the performance priors. Keep the raw seed and query linked.
5. Deliberately include newly named products, services, features, regulations, events, and updates even when trend tools have not accumulated enough history.

### 2. Expand and cluster

6. Choose up to two seeds per lane. For breakout, require momentum, novelty, or an obvious supply gap. For durable, require stable or recurring demand plus a plausible rankable intent.
7. Run the bundled keyword tool in expansion mode for each seed. Combine related keywords with Naver autocomplete and related searches. Make at most four expansion requests per run.
8. Normalize spacing and case, remove duplicates, and cluster queries that satisfy the same intent. Keep the clearest natural-language query from each cluster.
9. Reject navigational, purely promotional, duplicated, malformed, overly broad, unrelated high-volume, firsthand-experience, or original-photo-dependent terms before scoring. Keep product keywords when the intended article is an independent informational explanation supported by reliable sources.

### 3. Evaluate each lane

10. Build separate internal evidence tables. Record trend window, SearchAd match, intent cluster demand, and sampled blog supply.
11. Score breakout candidates from 0-5 on:
   - content-supply gap: few exact-intent posts, stale or incomplete answers, and low first-page saturation (30%);
   - momentum: recency, acceleration, and agreement across independent sources (25%);
   - demonstrated demand: SearchAd, autocomplete, related searches, news repetition, and community curiosity (20%);
   - novelty and timing: a newly searchable name or change with an early-publisher advantage (15%);
   - intent clarity and evidence: one useful article supported by reliable sources (10%).
12. Score durable candidates from 0-5 on:
   - durable demand: meaningful SearchAd cluster volume and stable, rising, or predictably seasonal 6-12 month interest (30%);
   - content-supply gap: few exact-intent answers, stale coverage, or an important unanswered sub-intent (30%);
   - ranking feasibility: limited first-page saturation by strong exact-intent posts and room for a clearer or fresher answer (20%);
   - intent clarity: one recurring informational need answerable in one post (15%);
   - maintainability: facts can be sourced and updated when needed (5%).
13. Treat scores only as internal comparison aids. Do not claim guaranteed ranking, visits, or a fabricated demand-to-document ratio.
14. Keep one winner from each lane. Let low-volume breakout queries win when live demand and supply scarcity are strong; let durable queries win when repeated demand and realistic ranking potential offer greater expected value.

### 4. Audit finalists

15. Audit the top two candidates from each lane on both Naver integrated search and Naver Blog search at `https://search.naver.com/search.naver?where=blog&query=<keyword>`.
16. Inspect at least the first 20 visible blog results per finalist. Record exact-intent matches, publication age, clearly commercial posts, strong publishers, and results that fully answer the query. For durable candidates, inspect older results far enough to distinguish sustained demand from a one-time spike.
17. Do not treat total result count as relevant competition. Distinguish exact answers from incidental mentions and near-duplicate intent.
18. Search one natural query variant per finalist. Open three to five representative posts, including the strongest current answers, and inspect their completeness, freshness, sourcing, and promotion level.
19. Reject high-volume keywords when the first page already satisfies the intent well or is dominated by unreasonably strong exact-match results. Reject low-supply keywords without demonstrated demand.
20. Verify the proposed article against reliable primary sources. Reject politics, celebrity gossip, rumor, tragedy exploitation, purely promotional content, individualized medical/legal/financial advice, and unverifiable topics.
21. Compare the lane winners on evidence-backed expected value: breakout timing over the next days versus durable traffic and rankability over the next months. Select exactly one query.

## Keyword Tool Validation

Expand a seed from the project root:

```bash
python3 .agents/skills/keyword-research/scripts/naver_keyword_tool.py "<seed>" --expand --limit 20
```

Validate a finalist with the same script without `--expand`:

```bash
python3 .agents/skills/keyword-research/scripts/naver_keyword_tool.py "<candidate>"
```

The script reads `NAVER_SEARCHAD_API_KEY`, `NAVER_SEARCHAD_SECRET_KEY`, and `NAVER_SEARCHAD_CUSTOMER_ID` from the process environment or the project `.env` file.

- Prefer an exact normalized match.
- Make at most four API requests for expansion and reuse those results when validating finalists.
- Treat `monthly_total_estimate` as directional demand, not real-time traffic or a guaranteed visit count.
- Treat values derived from `< 10` as estimates, not exact volumes.
- Never expose credentials in commands, logs, or the response.
- If the API is unavailable, rate-limited, or unconfigured, continue with the other signals and do not invent volume.

Do not expose the candidate list, internal table, or score. Do not generate a title or article unless asked.

## Output

Write in Korean and return only:

```text
Recommended keyword: <one keyword>
Opportunity type: <Breakout, Durable, or Seasonal durable>
Reason: <why traffic is likely now, in one concise sentence>
Article angle: <the main question the post should answer>
Keyword tool: <matched keyword and directional monthly demand, or unavailable>
Evidence: <2-3 current source links>
```
