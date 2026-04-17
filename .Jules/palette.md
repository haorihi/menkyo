## 2024-11-20 - Ensure Dynamic Aria-Labels Accommodate State
**Learning:** Icon-only buttons with toggling states (like the bookmark button) must use dynamic `aria-label` attributes that update when the state changes (e.g., 'ブックマークを解除' vs 'ブックマークに追加') so screen readers accurately reflect the action the user is about to take.
**Action:** Always verify if an icon-only button manages state. If so, bind its `aria-label` to the same state variable controlling its visual appearance.
