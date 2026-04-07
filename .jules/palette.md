## 2025-05-15 - [Initial setup]
**Learning:** This repository uses Gradio for its UI and has a suite of pytest tests.
**Action:** Always ensure Gradio-related tests pass and use existing Gradio components effectively.

## 2025-07-04 - [UI State Persistence and Reset]
**Learning:** In the `smolagents` Gradio UI, `log_user_message` should return the existing `file_uploads_log` to persist files across conversation turns. Additionally, the `chatbot.clear` event should be explicitly chained with a helper (e.g., `reset_ui_state`) to clear internal Gradio states like `stored_messages` and `file_uploads_log`, ensuring they don't leak into subsequent sessions.
**Action:** Always verify that multi-turn state (like file uploads) persists correctly and that 'Clear' actions reset all relevant UI components, not just the backend agent.
