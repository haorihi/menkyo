
## 2024-06-16 - Accessible Icon-Only Buttons
**Learning:** For React applications relying on utility classes (Tailwind), standardizing focus rings (`focus-visible:outline-none focus-visible:ring-2`) and aria attributes (`aria-label` on button, `aria-hidden="true"` on inner icon) is critical for accessibility. Dynamic buttons (like bookmarks) must also toggle their `aria-label` to accurately reflect their current functional state.
**Action:** When creating or modifying icon-only buttons, always apply explicit `aria-label` and `aria-hidden` combinations, and ensure stateful buttons update their labels dynamically based on state.
