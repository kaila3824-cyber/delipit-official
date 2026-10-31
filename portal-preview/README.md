# DELIPIT PORTAL review candidate

Baseline: main 011ad427046f0388c3182018b9ac5e64d08c2db2 / 2026-11-01 JST.

This is an isolated top-page prototype based on existing official content and official character assets. Existing production HTML, legal documents, apps, records and workflows are unchanged. Never deploy this directory to delipit.jp before SORA accepts the design.

- `index.html`: mobile-first candidate, noindex/nofollow. Existing article links intentionally open delipit.jp's existing design. App launch links go directly to the two official apps.
- `portal.css`: responsive shared design candidate.
- `review.html`: iframe review at 375/390/430/768/1280px (desktop scrollbars reduce content width by 15px in current QA).
- `assets/*.webp`: resized/re-encoded copies of official assets. No character redesign.

A separate owner-private Site serves this review. Its hosting identity stays in that Site checkout, not the official repository. Audit and the next phases are in `docs/portal-20261101/`.
