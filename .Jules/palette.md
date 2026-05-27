## 2026-05-27 - Accessible Icon-Only Buttons
**Learning:** Found an accessibility issue pattern specific to this app where icon-only buttons (like Home, Bookmark, Export) were missing `aria-label` attributes and keyboard focus states (`focus-visible`).
**Action:** Always add `aria-label` with explicit `focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ink` classes when creating or modifying icon-only buttons, and add `aria-hidden="true"` to their internal icon elements (e.g., `<i>`).
