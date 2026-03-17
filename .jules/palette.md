## 2025-05-15 - [Initial setup]
**Learning:** This repository uses Gradio for its UI and has a suite of pytest tests.
**Action:** Always ensure Gradio-related tests pass and use existing Gradio components effectively.
## 2025-05-15 - [Gradio UI Polish & Accessibility]
**Learning:** In Gradio 6.x, `gr.Chatbot` supports a 'clear' button through the `buttons` parameter. When clearing, it's essential to also reset auxiliary Gradio states (like message history and upload logs) via a helper method to ensure UI consistency. Also, using `opacity: 0.7` for secondary text is a robust way to maintain WCAG AA contrast across dynamic themes compared to hardcoded hex codes.
**Action:** Use `buttons=["copy", "clear"]` in `gr.Chatbot` and implement comprehensive clear handlers for complex Gradio apps.
