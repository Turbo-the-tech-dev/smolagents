## 2025-05-15 - [Initial setup]
**Learning:** This repository uses Gradio for its UI and has a suite of pytest tests.
**Action:** Always ensure Gradio-related tests pass and use existing Gradio components effectively.

## 2025-05-20 - [Gradio Notification Patterns]
**Learning:** Ephemeral feedback for file uploads in Gradio is much more pleasant when implemented as `gr.Info` or `gr.Warning` notifications rather than persistent UI textboxes, which clutter the interface and require manual clearing.
**Action:** Prefer transient notifications for high-frequency, secondary interactions like file upload status.
