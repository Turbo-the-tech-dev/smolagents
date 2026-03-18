## 2025-05-15 - [Initial setup]
**Learning:** This repository uses Gradio for its UI and has a suite of pytest tests.
**Action:** Always ensure Gradio-related tests pass and use existing Gradio components effectively.

## 2025-05-15 - [Gradio UI State Sync and Accessibility]
**Learning:** When using `gr.Chatbot` with a clear button, it's essential to not only reset the agent's memory but also clear any Gradio `gr.State` variables (like message history or file logs) to keep the UI and backend in perfect sync. Additionally, using `container=True` for textboxes is the most reliable way to ensure labels are accessible and visible in Gradio 6.x.
**Action:** Always implement a comprehensive `clear_all` routine for chatbot reset events and prefer contained labels for better ARIA support.
