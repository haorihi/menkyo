## 2026-05-24 - [Accessibility] Added ARIA labels and focus styling to icon-only buttons
**Learning:** Icon-only buttons (like the `ph-house` or `ph-export` ones) lack inherent screen-reader support or keyboard focus state.
**Action:** When adding or modifying icon-only buttons, consistently apply `aria-label`, add `aria-hidden="true"` to the internal icon element (`<i>`), and add `focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ink` to ensure proper accessibility formatting without modifying global CSS.
