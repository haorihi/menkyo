## 2026-05-07 - Add ARIA Labels and Focus Styles to Icon-only Buttons
**Learning:** Found multiple icon-only buttons (Home, Bookmark, Export) without proper aria-labels and visual focus rings for keyboard navigation, making them difficult to use for screen reader and keyboard users.
**Action:** Always add descriptive `aria-label`s to interactive elements containing only visual icons, hide the inner icons using `aria-hidden="true"`, and provide clear keyboard focus feedback (e.g. `focus-visible:ring-2`) matching the theme palette.
