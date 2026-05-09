## 2024-05-18 - Icon Button ARIA Labels & Focus Rings
**Learning:** Icon-only buttons (like Home, Bookmark, AI Export) lack proper accessibility labels for screen readers and miss clear focus indicators during keyboard navigation, which limits usability for some users. Dynamic state (like bookmark toggling) requires dynamic ARIA labels.
**Action:** Add localized `aria-label`s and consistent Tailwind focus ring utilities (`focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ink`) to all icon-only interactive elements to ensure full accessibility.
