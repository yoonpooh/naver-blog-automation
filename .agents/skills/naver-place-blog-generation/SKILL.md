---
name: naver-place-blog-generation
description: Turn one Naver Place URL into a complete Korean Naver Blog package by verifying the place, establishing the primary keyword and article angle, then running $title-generation, $article-generation, and strictly Naver-Place-photo-grounded $image-generation in order. Use when the user supplies a Naver Map or Naver Place URL and asks for a title, body, review-style draft, or images derived from the real photos shown on that place page.
---

# Naver Place Blog Generation

Create a complete title, article, and image set from one Naver Place URL without asking the user to repeat information available on the page.

## Scope

- Orchestrate `$title-generation`, `$article-generation`, and `$image-generation` in that order.
- Do not run `$keyword-research`; establish the primary keyword from the verified place name and the user's requested angle.
- Do not publish or open the Naver Blog editor unless the user separately requests publishing.

## 1. Verify the place

1. Open the supplied Naver Map or Naver Place URL and resolve its exact place ID and current canonical place name.
2. Inspect the current place page, including available owner information, menu, business hours, address, phone, parking, reservation, facilities, photos, and relevant recent visitor information.
3. Treat mutable facts such as prices, hours, parking rules, reservation availability, and facilities as current only when visible on the live page. Cross-check important claims with an official source when one exists.
4. Distinguish owner-provided facts from visitor observations. Never convert a reviewer's opinion into an objective claim.
5. Ask the user only if the URL cannot be accessed, identifies more than one place, or the requested angle materially depends on missing firsthand notes.

## 2. Establish shared context

Before invoking the downstream skills, record in the current thread:

- primary keyword: the exact verified place name, including `본점` or branch name when present;
- secondary intents: only directly supported terms such as menu, price, parking, reservation, family dining, group dining, nearby landmark, or access;
- article angle: the strongest useful combination supported by the page;
- evidence set: verified facts, unknown or changing details, and collected photo references;
- experience boundary: whether the user supplied genuine firsthand notes.

When no firsthand notes were supplied, write an informational visit guide. Do not claim that the user or assistant visited, tasted food, received service, or personally photographed anything. If the user supplies firsthand notes, preserve them accurately without embellishment.

## 3. Generate the title

Invoke `$title-generation` using the established primary keyword, article angle, and evidence set.

- Prefer one clear promise based on verified details.
- Avoid `방문 후기`, `먹어봤어요`, `내돈내산`, or similar firsthand wording unless the user supplied evidence for it.
- Keep the selected title available for the article step.

## 4. Generate the article

Invoke `$article-generation` using the selected title and the same verified context.

- Preserve its required `{이미지 영역}` markers.
- Cover only facts supported by the current place page or reliable corroborating sources.
- Label changing details for rechecking instead of estimating them.
- Keep source URLs in an internal evidence ledger; do not clutter the reader-facing article unless the user asks for sources.
- Before drafting, map every planned marker to at least one downloaded Naver Place photo. Shape headings and nearby text so each marker can be illustrated by a real available reference instead of an abstract concept.
- Do not create marker roles that require an unavailable exact exterior, interior, parking layout, booking screen, menu, facility, or service scene. Reuse a relevant real reference with a different crop, angle, distance, or lighting when references are fewer than markers.

## 5. Generate reference-grounded images

Invoke `$image-generation` for every article marker.

1. Download actual owner or visitor photos exposed by the supplied Naver Place page. Save one to three verified references per marker and record each source URL and role in the image manifest.
2. Require at least one real local Naver Place photo for every marker. Pass those exact local paths to the worker and require `$imagegen` to receive them as reference image inputs, not merely as prose descriptions.
3. Use a reference-led generation or precise-object-edit use case. Preserve the reference subject, service result, setting, equipment, food, building, sign, and other identity-bearing details. Change only angle, crop, distance, composition, or lighting.
4. Never generate concept-only or generic substitute imagery in this workflow. Ban abstract calendars, clocks, phones, cars, keys, location pins, icons, miniature scenes, blank checklists, stock props, and invented interfaces unless that exact object is visible in a supplied Naver Place reference.
5. When references are fewer than markers, reuse the closest real photo with materially different framing or lighting. When no usable Place photo exists at all, stop the image stage and report the missing reference instead of generating from text or model memory.
6. Remove source watermarks from generated outputs and reject malformed or invented text. Verified business signage may remain only when reproduced faithfully.
7. Treat every output as AI-generated. Never describe it as a photograph taken during the user's visit.

## Final check

- The exact verified place name anchors the keyword, title, and article.
- The title promise is answered by the article.
- Marker count equals generated image count and every marker is replaced in order.
- Every marker has at least one recorded Naver Place reference URL, local path, explicit role, and confirmation that the file was supplied to `$imagegen`.
- Every output remains visibly traceable to its assigned reference in a side-by-side identity check; matching only its palette or general category is a failure.
- No concept-only image or generic calendar, phone, car, icon, miniature, checklist, or unrelated stock prop remains.
- No unsupported firsthand claim, invented place detail, malformed sign, or source watermark remains.
- `$title-generation`, `$article-generation`, and `$image-generation` were all used; `$article-publishing` was not used.

## Output

Return, in Korean:

1. the single recommended title;
2. the finished article with all images rendered in marker order;
3. a compact ordered list of image paths and visual anchors;
4. the reference manifest and generation report paths;
5. a clear note that generated images are AI-created and must not be presented as original visit photographs.
