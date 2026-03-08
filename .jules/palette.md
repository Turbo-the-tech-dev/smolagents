## 2025-05-15 - [Initial setup]
**Learning:** This repository uses Gradio for its UI and has a suite of pytest tests.
**Action:** Always ensure Gradio-related tests pass and use existing Gradio components effectively.

## 2025-05-16 - [Gradio File Upload UX]
**Learning:** In Gradio, replacing persistent status Textboxes with transient `gr.Info()` and `gr.Warning()` notifications provides a much cleaner and more modern user experience for file uploads.
**Action:** Use `gr.Info()` and `gr.Warning()` for transient feedback in Gradio UIs instead of dedicated status components when appropriate.
