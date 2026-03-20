## 2025-05-15 - [Initial setup]
**Learning:** This repository uses Gradio for its UI and has a suite of pytest tests.
**Action:** Always ensure Gradio-related tests pass and use existing Gradio components effectively.

## 2025-05-20 - [Chatbot State Syncing]
**Learning:** In Gradio, clearing a `gr.Chatbot` via the `clear` event should also reset any underlying `gr.State` variables (like message history or file logs) to maintain UI-backend consistency.
**Action:** When adding a clear button to `gr.Chatbot`, always implement a helper method that resets both the agent's memory and any associated Gradio session states.
