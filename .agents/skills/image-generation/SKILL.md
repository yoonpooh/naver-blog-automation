---
name: image-generation
description: Generate and save one subject-specific, reference-grounded, validated image for every `{이미지 영역}` in the latest Korean blog article by delegating independent images to parallel subagents using `$imagegen`. Use when the user asks for article images, images for every image area, a complete illustrated post, or the image step after article generation.
---

# Image Generation

Generate every article image without asking the user to repeat usable thread context.

## Plan

1. Recover the latest complete article, title, keyword, and optional verified reference images from the thread. Stop only when the article or image markers are missing.
2. Count `{이미지 영역}` markers in order. Treat the first as the cover and each later marker as illustrating the immediately preceding section.
3. Extract the visual anchors that make the article recognizable: named brands, products, apps, interfaces, people, places, packages, devices, and distinctive objects. Mark each anchor as `must-show`, `supporting`, or `concept-only` for every image.
4. For every real `must-show` anchor, collect one to three current, verified references before prompting. Prefer user-provided material, then official product pages, media kits, documentation, or press assets. Save local references beside the output and record each source URL and role. Do not rely on model memory for exact logos, products, packages, people, places, or interfaces.
5. Create a shared visual contract that fits the subject instead of forcing generic lifestyle photography. Choose the appropriate `$imagegen` use case, keep a consistent aspect ratio and treatment across the set, and prohibit only unsupported or decorative text, watermarks, and invented facts.
6. Assign each marker a distinct subject, distance, viewpoint, and setting. The cover must communicate the primary keyword at thumbnail size within two seconds. Every later image must visibly explain its nearby section, not merely match its mood.
7. Preassign a unique workspace path under `output/images/<keyword-slug>-YYYYMMDD[-vN]/`, using ordered names such as `01-cover.png` and `02-<section-slug>.png`. Never overwrite existing output.

## Delegate

1. Use parallel subagents. Keep the root agent as coordinator and run up to `min(marker count, 6, available non-root agent slots)` image workers concurrently; reuse completed workers for remaining markers.
2. Assign exactly one marker and one output path to each worker. Give it only:
   - the title and primary keyword;
   - marker index and role;
   - the opening or nearest preceding heading and body;
   - the next heading only when needed for disambiguation;
   - the shared visual contract;
   - the image's `must-show` visual anchors and forbidden generic substitutes;
   - its unique composition and factual guardrails;
   - every verified local reference image, source URL, and explicit role;
   - the preassigned output path.
3. Require each worker to read and use `$imagegen`, use the built-in image tool, generate or reference-led edit exactly one raster image, inspect it against the anchors and references, and persist the selected image at its assigned workspace path.
4. Never switch to the CLI/API fallback without explicit user consent. If the built-in tool is unavailable, preserve successful siblings and report the affected marker.

## Factual and Visual Safety

- A verified brand, logo, product, package, or interface is allowed when it is materially relevant. The safety rule forbids fabrication, not recognizable subject matter.
- Never replace a named visual anchor with anonymous spheres, stones, blocks, empty desks, generic devices, or unrelated stock-photo metaphors. If the article would no longer be identifiable without its title, the image fails.
- Use a verified reference-led edit or composition when exact appearance matters. Preserve the reference identity; do not redraw logos, UI, labels, or product details from memory.
- Without a verified reference, create an honest editorial concept and state the limitation. Do not claim that it shows the exact product, package, person, place, interface, document, or event.
- Avoid decorative image text by default, but allow verified names, logos, labels, and UI text when they are necessary for subject identity. Reject malformed or invented text.
- Represent schedules, purchasing, comparisons, and checklists with relevant objects or a verified interface rather than fake screens or arbitrary props.
- Do not imply firsthand use, endorsement, attendance, or an event that did not occur.
- Keep the set visually consistent but make every image materially distinct in subject, crop, angle, background, or action.

## Reconcile and Validate

1. Restore results to marker order regardless of completion order.
2. Confirm each assigned file exists in the workspace and is a non-empty PNG, JPEG, or WebP.
3. Apply a two-second identity check to every image: confirm that its primary subject and nearby section are recognizable without reading the article title. Reject generic imagery that could illustrate an unrelated topic.
4. Inspect the full set for required visual anchors, reference fidelity, section relevance, shared style, meaningful diversity, malformed text or logos, watermarks, factual invention, and duplicate images.
5. Regenerate only a failed marker once with one targeted correction. If identity was the failure, strengthen the verified reference and explicit `must-show` instruction instead of adding more generic styling. Keep successful images unchanged.
6. Do not treat a partial set as complete. If one retry still fails, list the missing marker and retain the successful files for continuation.

## Output

Return the finished Korean article with each `{이미지 영역}` replaced by the corresponding rendered image in marker order. Also provide a compact ordered path list, visual anchors, reference source URLs and roles, the shared visual contract, the final prompt used for each image, the two-second identity result, and confirmation that built-in `$imagegen` was used.
