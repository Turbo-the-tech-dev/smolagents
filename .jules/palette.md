## 2025-05-15 - [Initial setup]
**Learning:** This repository uses Gradio for its UI and has a suite of pytest tests.
**Action:** Always ensure Gradio-related tests pass and use existing Gradio components effectively.

## 2025-05-22 - [Fix file persistence in Gradio UI]
**Learning:** In Gradio, session state variables (gr.State) like `file_uploads_log` must be explicitly returned by event handlers in every turn if they need to be persisted, otherwise they might be reset to default values if the handler returns a literal like `[]`.
**Action:** Always return the current state object from event handlers unless a reset is explicitly intended.
