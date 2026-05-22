## 2026-05-22 - Adding accessibility to icon-only buttons
**Learning:** Found several icon-only buttons (home, bookmark, export) lacking ARIA labels and focus-visible outlines, which makes them inaccessible for screen reader users and keyboard navigators. Adding these ensures the application meets basic a11y standards.
**Action:** Always add aria-label and focus-visible styles (focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ink) to any button that only contains an icon.
