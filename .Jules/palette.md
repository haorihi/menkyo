## 2024-05-23 - Icon-only Header Button Accessibility
**Learning:** Icon-only header buttons in primary application views (like Home, Bookmark, Export) frequently lack both accessible names and keyboard focus indicators, making them inaccessible to screen reader and keyboard users.
**Action:** When working on application views or components, systematically check all icon-only interactive elements for `aria-label` attributes (localized in Japanese) and `focus-visible` utility classes (e.g. `focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ink`).
