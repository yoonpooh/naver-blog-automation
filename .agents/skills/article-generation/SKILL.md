---
name: article-generation
description: Write a complete, fact-checked Korean informational Naver Blog article with image placeholders and keyword-tool-validated hashtags from the latest keyword and title selected in the current thread. Use when the user asks for the body, full article, draft, sections, image areas, or hashtags after keyword research and title generation.
---

# Article Generation

Write publishable reader-facing copy without asking the user to repeat usable context from the thread.

## Context and Research

1. Reuse the latest selected keyword, opportunity type, title, article angle, and evidence.
2. Ask only for the missing keyword or title when neither can be recovered from the conversation.
3. Verify mutable facts such as dates, prices, availability, rules, and product details against current reliable sources. Prefer primary sources and corroborate important claims.
4. Build an internal claim-to-source ledger before drafting. Mark unavailable facts as undisclosed instead of estimating them.
5. Inspect current competing articles only to identify unanswered questions. Synthesize sources; never closely rewrite one article.

## Structure

1. Answer the title's main promise within the opening and first section.
2. Write a 150-250 character opening in two or three short paragraphs without a greeting or heading.
3. Write 5-7 `##` sections. Give every section a distinct reader question and 250-450 useful characters. Never split one idea merely to reach the minimum.
4. Use specific headings that reveal the answer scope. Avoid generic headings such as `Features`, `Advantages`, `Conclusion`, or `Things to know`.
5. End with a concise 100-180 character closing, followed by hashtags.

Adapt the depth:

- Breakout: target 1,500-2,200 Korean characters and five or six sections; prioritize verified new facts and do not pad missing information.
- Durable: target 2,200-3,200 characters and six or seven sections; cover conditions, steps, exceptions, and common mistakes.
- Seasonal durable: target 1,800-2,800 characters; emphasize current rules and meaningful changes.

Treat ranges as guidance, not SEO guarantees. Information density and completeness outrank length.

## Image Placeholders

- Insert the literal marker `{이미지 영역}` on its own line once after the opening and once after every `##` section. A five- to seven-section article must therefore contain 6-8 markers.
- Place each section marker immediately after that section's final paragraph and before the next heading or closing paragraph.
- Never place markers consecutively, inside a sentence, after the closing, or among hashtags.
- Do not include image prompts or captions. Make each marker's intended image inferable from the nearest heading and body so a later `imagegen` step can generate it.
- Exclude markers from character-count targets.

## Voice

- Use friendly, calm explanatory Korean, primarily `-입니다`, `-할 수 있습니다`, and `-하면 됩니다`.
- Keep paragraphs to one to three sentences and sentences usually under 60 Korean characters.
- Start directly with the useful answer. Avoid greetings, meta-writing, report language, and phrases equivalent to `let's look into it`, `in this post`, or `I hope this helped`.
- Never invent firsthand use, visits, taste, performance, atmosphere, or personal opinions.
- State verified facts clearly, attribute company claims, and label unknown or changing details.
- Use the exact primary keyword naturally in the opening and where useful. Do not repeat it in every heading or force related terms into the body.
- Use a list or table only when it makes steps or comparisons materially clearer.

## Hashtags

Generate 8-12 relevant Naver Blog hashtags after the article:

- Reuse related-keyword results already produced in the current thread. Otherwise run `python3 .agents/skills/keyword-research/scripts/naver_keyword_tool.py "<keyword>" --expand --limit 20` from the project root.
- If the exact query returns too few useful terms, expand one broader parent seed such as the brand or product category. Make no more than two keyword-tool requests.
- Select validated phrases by search demand and direct relevance. Fill remaining slots with the exact topic, brand, product, intent, or category only when useful, without implying that fallback tags have measured demand.
- Include the exact core topic, important proper nouns, two to four intent terms, and two to three category terms.
- start every tag with `#`, remove internal spaces and punctuation, and deduplicate normalized variants;
- reject unrelated high-volume tags and near-identical keyword stuffing;
- keep extra related terms in hashtags instead of forcing all of them into body sentences.

## Final Check

- Ensure the title's promise is fully answered and every factual claim is supported.
- Remove repeated explanations, unsupported superlatives, fake urgency, and writer-facing instructions.
- Keep the claim-to-source ledger internal. Do not include a source list, citations, or links in the article unless the user requests them or the topic is medical, legal, financial, or otherwise high-stakes.
- Use brief natural attribution such as `회사 발표에 따르면` only when it helps distinguish a claim from an independently verified fact.
- Ensure every image marker has distinct nearby content worth visualizing.
- Confirm that the marker count equals the `##` section count plus one.

## Output

Write only the Korean article in this order:

```text
<opening paragraphs>

{이미지 영역}

## <specific subheading>
<body>

{이미지 영역}

...repeat one marker after every section...

<closing paragraph>

#태그1 #태그2 ... #태그8
```
