## 2026-05-06 - Missing Context on Icon-Only Buttons
**Learning:** Icon-only navigation buttons (like Home, Bookmark, Export) using `ph-` classes consistently lacked `aria-label`s and `focus-visible` rings, making them invisible to screen readers and difficult to target via keyboard navigation.
**Action:** Always verify that buttons containing only an `<i>` or `<svg>` tag have an appropriate localized `aria-label`, an `aria-hidden="true"` on the inner icon, and a `focus-visible:ring-*` class for keyboard focus.
