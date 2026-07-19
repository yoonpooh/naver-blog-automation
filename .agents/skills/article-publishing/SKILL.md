---
name: article-publishing
description: Prepare and publish the latest completed Korean article in Naver Blog with exact text structure, ordered images, AI-use labels, 19px bold section headings, hashtags, and an appropriate existing category. Use when the user asks to write, stage, prepare, or publish the article in Naver Blog.
---

# Article Publishing

Transfer the latest completed article and its generated images into the logged-in Naver Blog editor without changing the copy.

## Safety Boundary

- Complete every verification before opening publish settings. Select only an existing category and click the final publish control once.
- Use at most one primary write tab and one fallback write tab per article. Never open a third write tab, and never rebuild the article more than once.
- Never clear, replace, or re-enter an article in a tab that already contains content. If that tab's state is uncertain, preserve it and stop using it.
- Never use editor-wide `Cmd+A` or whole-document replacement after components have been inserted. Do not use undo as a general repair mechanism. If the immediately preceding command unexpectedly replaced or removed unrelated article content, use exactly one immediate `Cmd+Z`, verify the complete source structure is restored, and stop that placement attempt before retrying.
- Never improvise a repair after a mismatch. Stop the affected step, compare it with the source article, and repair only that component.
- Use Chrome for text and DOM-backed editor operations. The image upload boundary is mandatory: use Computer Use exclusively from clicking `사진` through the native file picker's `열기` action.
- Never use Chrome, Playwright, CDP, DOM injection, `setInputFiles`, a hidden file input, or clipboard file transfer to upload images. Do not fall back to them if Computer Use is inconvenient; stop and report the upload step as blocked.
- Do not use Computer Use `type_text` for Korean copy. It can be corrupted by the active input method. Use Chrome text entry or clipboard paste from the exact source.
- Never translate coordinates from a Chrome/Browser screenshot into Computer Use screen coordinates. A Computer Use click requires a fresh Computer Use accessibility target or Computer Use screenshot; if neither is available, stop as blocked.

## Inputs

Recover these from the current thread and workspace:

1. The final title.
2. The exact final article, including section headings and hashtags.
3. The ordered image paths produced by `$image-generation`.

Stop if the title, complete article, or any required image is missing. Do not regenerate or rewrite them inside this skill.

## Preflight

1. Count article image markers and ordered image files. Require an exact match.
2. Require unique, zero-padded filenames in marker order, such as `01-cover.png`, `02-product.png`, and `03-schedule.png`.
3. Confirm every file exists, is non-empty, and is a PNG, JPEG, or WebP.
4. Convert the article's `{이미지 영역}` markers in the working copy to unique markers: `[[IMAGE_01]]`, `[[IMAGE_02]]`, and so on.
5. Add `[[UPLOAD_STAGING]]` on its own final paragraph after the hashtags. This is an editor-only marker and must not remain in the finished draft.
6. Record the expected title, heading list, marker count, image filenames, and hashtags for final verification.

## Open the Editor

1. Reuse the user's logged-in Chrome session and open the Naver Blog write editor.
2. If Naver offers an earlier draft, follow the user's stated intent: resume only when requested; otherwise start the new draft. If intent is ambiguous and discarding content would be risky, stop for confirmation.
3. Confirm that the editor is ready before entering content.
4. Record the primary write tab before entering content. Do not create another write tab preemptively.
5. If an OS-level Computer Use click on `사진` is not delivered in the primary tab, do not retry or alter that tab. A single fallback is allowed:
   - preserve the primary tab as-is;
   - open exactly one new logged-in write tab directly through Computer Use;
   - require a fresh, usable Computer Use accessibility state or screenshot before entering anything;
   - keep the fallback tab free of Chrome, Playwright, CDP, or debugger control until the native picker closes;
   - reproduce the exact source only by clipboard paste and Computer Use formatting, never Korean `type_text`;
   - if copy, formatting, or upload cannot be verified in that Computer Use-only tab, stop as blocked. Never open a third tab or return to a preserved tab for another attempt.

## Enter Text First

1. Enter the title exactly once.
2. Enter the full article working copy with natural paragraph breaks and the numbered image markers.
3. Keep each section heading as its own paragraph, with exactly one blank paragraph above and below it.
4. Keep the intended spacing between sections, images, closing copy, and hashtags.
5. Select each section heading independently, apply Bold, and set its font size to 19px. Verify its computed weight or `<b>` state and computed font size immediately.
6. Verify that normal body paragraphs are not Bold or 19px.
7. Confirm every numbered marker and `[[UPLOAD_STAGING]]` is present before uploading.

## Upload Images Once

1. Put a caret in an empty paragraph immediately after `[[UPLOAD_STAGING]]`.
2. Verify that no title, heading, body text, marker, or component is selected. Abort the upload if any text selection exists.
3. Switch to Computer Use before clicking `사진`. Computer Use must perform the entire upload sequence: click `사진`, operate the native file picker, navigate to the prepared directory, select the files, and click `열기`.
4. After clicking `사진`, require fresh Computer Use evidence that the native file picker is actually open. Do not send picker shortcuts, paths, or selection keys based only on the click being issued.
5. While the native file picker is open, do not use Chrome or any browser automation API. Re-read the current Computer Use accessibility state before every interaction.
6. In Computer Use, use `Cmd+A` only when the directory contains exactly the expected image files and no folders or unrelated files. Otherwise select the first expected file and extend the selection through the last expected file.
7. In Computer Use, verify that exactly the expected files are selected, then click the native `열기` button once.
8. Only after the native file picker closes may control return to Chrome. A fallback tab may be claimed or debug-controlled only at this point. Use Chrome to choose `개별사진`.
9. Verify that Naver inserted the expected number of separate image components at the staging position and that their filenames remain in order.
10. Before moving anything, record each staged image component ID in filename order. Naver may clear an image's filename or `alt` value after cut-and-paste, so use the recorded IDs for post-placement order verification.

Record & Replay may automate only the stable native file-picker sequence. Do not replay the editor layout, scrolling, marker replacement, formatting, save, or publish steps.

## Place Images by Filename

For each image in ascending filename order:

1. Locate the staged image by its exact filename or `alt` value.
2. Select only that image component and cut it with `Cmd+X`.
3. Click only its exact numbered marker text. Press `Home`, then `Shift+End` to select that marker line. Never press `Cmd+A` here; in the Naver editor it can select the whole article.
4. Paste the image component with `Cmd+V`. The filename or `alt` may become empty after a successful move; identify the moved component by its recorded ID instead.
5. Verify that the total image count is unchanged, the target marker is gone, the image appears between the intended surrounding paragraphs, and the recorded title, heading count, and hashtags are unchanged.
6. Select the moved image component so its controls become visible, enable `AI 활용 설정`, and verify its toggle is active (for example, `se-is-selected`) before continuing.

If any check fails, stop before moving the next image. Outside the single immediate recovery allowed in Safety Boundary, never compensate with editor-wide selection, undo, or re-paste.

After all images are placed, delete only the `[[UPLOAD_STAGING]]` paragraph. Confirm that no numbered or staging marker remains.

## Final Verification

Require every check to pass:

- exactly one title matching the source;
- article copy matching the source, with no missing, duplicated, or corrupted paragraph;
- image count equal to the original marker count;
- images ordered by filename and placed at their intended sections;
- one overall visual review confirms that section headings, body paragraphs, and images have natural and consistent spacing above and below, matching the established Naver layout with no visibly stuck-together content or excessive gaps;
- every section heading Bold and 19px, with exactly one blank paragraph above and below it;
- normal body copy not Bold or 19px;
- all expected hashtags present;
- `AI 활용 설정` active for every image;
- no `[[IMAGE_..]]` or `[[UPLOAD_STAGING]]` marker remains;
- the editor has not yet been published before opening publish settings.

## Publish

1. Only after final verification passes, click the editor header's `발행` button once to open the publish settings panel. This first click opens settings; it does not complete publication.
2. Open the category selector in the publish panel and inspect the existing categories.
3. Choose the closest existing category for the article's primary keyword and informational intent. Prefer a specific match; if none fits, select `오늘의 이슈`. Never create, rename, or reorganize categories.
4. Verify the selected category label. Do not change topic, visibility, comments, reactions, search exposure, sharing, publication time, notice status, or any other publish setting unless the user explicitly requested it.
5. Confirm that the tag editor contains the expected article hashtags without missing or duplicate tags.
6. Distinguish the publish panel's final `발행` control from the editor header button and require exactly one matching panel control before clicking it once.
7. Verify publication succeeded by confirming the resulting post page, exact title, and stable Naver Blog post URL. If the panel remains open or success cannot be confirmed, report `blocked` and do not click the final button again.
8. If the caller requested a success-only thread-title change, perform it only after the published post page, exact title, and URL are confirmed. Never change it for `partial` or `blocked` runs.

## Output

Report only:

- `done`, `partial`, or `blocked`;
- the verified title, image count, heading count, AI-use count, and hashtag presence;
- the selected category;
- whether publication was confirmed and the final post URL;
- any single failed check that prevented completion.
