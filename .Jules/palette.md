## 2024-04-16 - Add ARIA Labels to Icon-Only Buttons
**Learning:** Found several icon-only buttons (Home, Bookmark, Export) without accessible names, making them inaccessible to screen reader users. Also noticed keyboard focus styles were missing on these critical navigation elements.
**Action:** Always add descriptive `aria-label` attributes to icon-only `<button>` elements, add `aria-hidden="true"` to the inner `<i>` tags to avoid redundant announcements, and ensure explicit focus styles (e.g., `focus-visible:ring-2 focus-visible:ring-ink`) are applied for keyboard users.
