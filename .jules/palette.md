## 2025-05-15 - [Initial setup]
**Learning:** This repository uses Gradio for its UI and has a suite of pytest tests.
**Action:** Always ensure Gradio-related tests pass and use existing Gradio components effectively.

## 2025-05-15 - [Reset UI state on clear]
**Learning:** In Gradio UIs that maintain session state (like `gr.State` or file logs), the 'chatbot.clear' event only clears the visual history of the chatbot. Internal states must be manually reset by chaining a `.then()` call to synchronize the UI components and backend memory.
**Action:** Always chain `.then()` to `chatbot.clear()` to reset state variables and restore button interaction states.
