## 2025-05-15 - [Initial setup]
**Learning:** This repository uses Gradio for its UI and has a suite of pytest tests.
**Action:** Always ensure Gradio-related tests pass and use existing Gradio components effectively.

## 2025-05-15 - [Persistent File Upload State]
**Learning:** In Gradio UIs where state is managed through components like `gr.State`, event handlers must explicitly return the existing state to maintain it across multiple interactions. Returning an empty list or default value will inadvertently clear the user's previous inputs (like uploaded files).
**Action:** Ensure that helper functions like `log_user_message` return the current state variable for components that should persist across conversation turns.
