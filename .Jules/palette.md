## 2026-04-30 - [ARIA Attributes for Toggle Buttons]
**Learning:** When using `aria-pressed` for a toggle button, the `aria-label` should ideally remain static (e.g., "Bookmark"). Changing both the label (e.g., "Add bookmark" / "Remove bookmark") and the `aria-pressed` state simultaneously can result in overly verbose or confusing screen reader announcements.
**Action:** When implementing toggle buttons with `aria-pressed`, keep the `aria-label` static describing the function, relying on the `aria-pressed` state to convey the current status.
