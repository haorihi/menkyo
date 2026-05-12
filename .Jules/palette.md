
## 2024-05-12 - [Accessible Header Navigation]
**Learning:** Icon-only buttons without `aria-label`s fail screen reader context, and custom rounded header buttons (e.g. `w-12 h-12 rounded-full glass-surface`) need explicit `focus-visible` states to be usable via keyboard navigation.
**Action:** When creating or modifying icon-only utility buttons (like Home, Bookmark, or Export), always ensure they include an appropriate localized `aria-label` and the standard `focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ink` classes.
