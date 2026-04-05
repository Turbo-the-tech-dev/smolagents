## 2025-05-15 - [Initial setup]
**Learning:** This repository uses Gradio for its UI and has a suite of pytest tests.
**Action:** Always ensure Gradio-related tests pass and use existing Gradio components effectively.

## 2025-05-15 - [Theme-Agnostic Subdued Text]
**Learning:** Using hardcoded hex colors like `#bbbbc2` for subdued text (like footnotes) can lead to accessibility issues in dark mode or custom themes. Using `opacity` (e.g., `0.7`) on the default text color ensures consistent contrast and readability across all themes.
**Action:** Prefer `opacity` over hardcoded hex values for secondary/subdued UI elements in Gradio components.
