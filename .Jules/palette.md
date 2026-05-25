## 2024-05-25 - Icon-only Buttons Accessibility
**Learning:** Found several icon-only buttons (like Home, Bookmark, Export) without proper ARIA labels and lacking keyboard focus visibility, which negatively impacted keyboard navigation and screen reader support in this static application.
**Action:** Always add Japanese `aria-label` attributes to icon-only interactive elements, ensure standard `focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ink` classes are present, and add `aria-hidden="true"` to the inner icons to avoid redundant screen reader reads.
