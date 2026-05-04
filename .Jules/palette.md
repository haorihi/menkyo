
## 2024-05-24 - Missing ARIA Labels on Icon-only Buttons
**Learning:** Icon-only interactive elements (like Home, Bookmark, Export buttons) must have programmatic labels for screen readers. Keyboard focus states (`focus-visible`) are critical for non-mouse users to identify which element has focus.
**Action:** Ensure all future icon-only buttons include `aria-label` and `focus-visible` styles.
