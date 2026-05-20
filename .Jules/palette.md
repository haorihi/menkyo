## 2024-05-24 - [ARIA Labels and Focus States on Icon-only Buttons]
**Learning:** Found that multiple icon-only utility buttons (Home, Bookmark, Export) were missing `aria-label`s for screen readers and `focus-visible` styles for keyboard navigation.
**Action:** Always ensure interactive elements with only icons have descriptive `aria-label` attributes and appropriate focus rings (`focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ink`) applied.
