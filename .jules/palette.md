## 2025-05-15 - [Initial setup]
**Learning:** This repository uses Gradio for its UI and has a suite of pytest tests.
**Action:** Always ensure Gradio-related tests pass and use existing Gradio components effectively.

## 2025-05-20 - [Gradio UX/A11y Enhancements]
**Learning:** Using `gr.Info` and `gr.Warning` provides a cleaner UX for transient events like file uploads than dedicated status components. `gr.Textbox` supports `html_attributes` for ARIA labels, which is critical for accessible icon-heavy interfaces.
**Action:** Favor transient notifications for status updates and always use `html_attributes` for accessibility when visible labels are omitted.
