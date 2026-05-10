## 2025-01-20 - [Icon Button Accessibility]
**Learning:** Icon-only buttons (like Home, Bookmark, Export) in the app were missing ARIA labels and keyboard focus indicators, making them invisible to screen readers and difficult to navigate via keyboard.
**Action:** Always add `aria-label` to describe the action and use `focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ink` to ensure a clear focus ring that matches the app's established design language. Add `aria-hidden="true"` to the inner icons to prevent redundant screen reader announcements.
