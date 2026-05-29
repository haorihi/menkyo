
## 2024-05-18 - Accessible Icon-Only Buttons
**Learning:** Icon-only buttons (like Home or Bookmark actions) in this app often used `<i className="ph ph-..."></i>` directly inside `<button>` elements. This causes screen readers to read generic icon classes or nothing at all, while keyboard navigation fails to show focus indicators due to Tailwind resetting default outlines. Furthermore, `disabled` elements inherently skip tab order, complicating focus testing natively.
**Action:** Always add explicit Japanese `aria-label` attributes to the parent `<button>`, pair it with `focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ink` for visual keyboard focus, and add `aria-hidden="true"` to the internal `<i>` tag to prevent redundant screen reader announcements.
