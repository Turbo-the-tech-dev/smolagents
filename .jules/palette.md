## 2025-05-15 - [Initial setup]
**Learning:** This repository uses Gradio for its UI and has a suite of pytest tests.
**Action:** Always ensure Gradio-related tests pass and use existing Gradio components effectively.

## 2025-05-22 - [Refining File Upload UX]
**Learning:** In multi-turn chat interfaces, staged file uploads should be cleared after each successful message submission. Persisting them in the upload area forces users to manually remove them for the next turn, creating friction and leading to redundant data being sent.
**Action:** Always reset the file upload state (e.g., `file_uploads_log = []`) in the final step of a submission event chain.
