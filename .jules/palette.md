## 2025-05-15 - [Initial setup]
**Learning:** This repository uses Gradio for its UI and has a suite of pytest tests.
**Action:** Always ensure Gradio-related tests pass and use existing Gradio components effectively.

## 2025-05-15 - [Theme-agnostic text contrast]
**Learning:** Using 'opacity: 0.7' instead of hardcoded gray hex codes (like #bbbbc2) for secondary text ensures WCAG AA contrast compliance across both light and dark Gradio themes.
**Action:** Prefer opacity or CSS variables for subdued text to maintain readability across theme switches.
