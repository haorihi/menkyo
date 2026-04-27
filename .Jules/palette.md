## 2024-05-24 - Accessibility for Icon-Only Buttons
**Learning:** Icon-only navigation buttons in this app (like the Home and Bookmark buttons in Quiz and Flag List views) lack ARIA labels and clear keyboard focus indicators, making them inaccessible to screen readers and difficult to navigate via keyboard.
**Action:** Always verify that icon-only buttons have descriptive `aria-label` attributes localized to Japanese, and apply consistent keyboard focus styles (e.g., `focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ink/50`) using existing Tailwind utility classes.
