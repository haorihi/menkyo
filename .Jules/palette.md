## 2024-05-24 - Missing ARIA Labels on Icon-Only Buttons
**Learning:** Circular icon-only buttons in the quiz and flag-list views lacked `aria-label` attributes and keyboard focus indicators, making them inaccessible to screen readers and difficult to navigate via keyboard.
**Action:** Added dynamic and static `aria-label` attributes along with `focus-visible:ring-2 focus-visible:outline-none` styles to ensure accessibility.
