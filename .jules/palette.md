## 2025-05-15 - [Initial setup]
**Learning:** This repository uses Gradio for its UI and has a suite of pytest tests.
**Action:** Always ensure Gradio-related tests pass and use existing Gradio components effectively.

## 2025-05-15 - [Theme-aware accessibility]
**Learning:** To ensure WCAG AA contrast for subdued text across Gradio's light and dark modes, use 'opacity: 0.7' on the primary text color rather than hardcoded gray hex codes.
**Action:** Favor theme-relative styling (opacity, CSS variables) over fixed colors for better accessibility in multi-theme UIs.
