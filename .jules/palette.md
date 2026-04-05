## 2025-05-15 - [Initial setup]
**Learning:** This repository uses Gradio for its UI and has a suite of pytest tests.
**Action:** Always ensure Gradio-related tests pass and use existing Gradio components effectively.

## 2025-05-22 - [Chatbot State Reset]
**Learning:** In Gradio 6.x, `gr.Chatbot.clear()` event can be used to reset not only the visual chat history but also internal state variables (like `gr.State`) by chaining `.then()` handlers.
**Action:** Always chain state-resetting logic to the `chatbot.clear` event to ensure a consistent user experience when starting a fresh session.
