## 2024-05-15 - Accessible Icon Buttons
**Learning:** Icon-only buttons lack descriptive text for screen readers and often miss clear keyboard focus indicators in standard Tailwind resets.
**Action:** Always pair `aria-label` with explicit `focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ink` classes when creating or modifying icon-only buttons to ensure they are accessible via screen readers and keyboard navigation.
