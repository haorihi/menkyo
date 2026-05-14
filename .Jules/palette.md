
## 2024-05-14 - Accessibility improvements for icon-only buttons
**Learning:** Found a common pattern in the application where icon-only buttons used for navigation or actions (Home, Bookmark, Export) lack `aria-label`s for screen readers. Further, they lacked keyboard focus states, making keyboard navigation difficult for visually impaired users.
**Action:** When working on generic components or standard navigation layouts (especially floating, round icon buttons common in this app's style), always proactively ensure they include descriptive `aria-label`s and proper `focus-visible` styling using the established project pattern (`focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ink`).
