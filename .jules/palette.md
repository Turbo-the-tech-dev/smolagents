## 2025-05-15 - [Initial setup]
**Learning:** This repository uses Gradio for its UI and has a suite of pytest tests.
**Action:** Always ensure Gradio-related tests pass and use existing Gradio components effectively.

## 2025-05-15 - [Gradio UI Accessibility and Feedback Patterns]
**Learning:** Hardcoded hex colors (like #bbbbc2) for secondary text in Gradio components can lead to poor contrast in different themes. Using CSS opacity (e.g., opacity: 0.7) ensures better compatibility as it scales with the theme's base text color. Additionally, transient status updates (like file upload status) are better handled by gr.Info/gr.Warning toast notifications rather than persistent UI components to avoid layout shifts.
**Action:** Always prefer opacity over hardcoded grays for subdued text and use native Gradio notifications for transient feedback.
