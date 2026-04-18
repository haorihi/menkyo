## 2024-04-18 - Icon-only Button Accessibility
**Learning:** Throughout the application, icon-only utility buttons (such as Home, Bookmark, and Export) lack `aria-label`s and `focus-visible` states. This specific pattern makes the app difficult to navigate for both screen reader users and keyboard-only users.
**Action:** Always ensure icon-only buttons include descriptive `aria-label`s and explicit `focus-visible` utility classes (`focus-visible:outline-none focus-visible:ring-2`) to provide proper context and interaction feedback.
