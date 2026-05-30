
## 2024-05-30 - Accessible Icon-Only Buttons
**Learning:** Icon-only buttons without `aria-label`s are completely invisible to screen readers, leaving users guessing their function. Additionally, screen readers often read out the internal class names of SVG or font icons if they aren't explicitly hidden with `aria-hidden="true"`. Finally, missing visible focus states (like focus rings) make keyboard navigation nearly impossible as users cannot see where their focus is.
**Action:** Always ensure that icon-only buttons have a descriptive `aria-label`, explicitly hide their internal icons from assistive technologies using `aria-hidden="true"`, and provide clear keyboard focus indicators using styles like `focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ink`.
