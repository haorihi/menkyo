## 2026-05-31 - Icon-only Button Accessibility
**Learning:** Found several icon-only buttons (Home, Bookmark, Export) lacking ARIA labels and clear keyboard focus states in the Quiz and Flag List views. Because the primary language is Japanese, the aria-labels must be localized correctly (e.g., ホームに戻る, ブックマークに追加する) for screen readers.
**Action:** When adding or updating icon-only buttons, always apply localized Japanese `aria-label`s, `focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ink` for keyboard users, and `aria-hidden="true"` to the inner decorative `<i>` tags.
