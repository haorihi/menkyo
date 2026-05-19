
## 2024-05-24 - Accessible Header Icon Buttons
**Learning:** Icon-only buttons used in headers (like Home, Bookmark, Export) often lack aria-labels and keyboard focus indicators, making them inaccessible to screen readers and keyboard users.
**Action:** Always add descriptive Japanese `aria-label` attributes and focus classes (`focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ink`) to icon-only interactive elements in the application.
