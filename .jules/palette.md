## 2025-05-15 - [Initial setup]
**Learning:** This repository uses Gradio for its UI and has a suite of pytest tests.
**Action:** Always ensure Gradio-related tests pass and use existing Gradio components effectively.

## 2025-05-22 - [Chatbot clear event chaining]
**Learning:** Chaining a `.then()` event handler after `chatbot.clear()` in Gradio requires the subsequent function (or lambda) to accept one positional argument (e.g., `lambda _: ...`) to avoid a `TypeError`, as Gradio passes the result of the `clear` action to the next step.
**Action:** Always ensure event handlers in `.then()` chains account for arguments passed from preceding steps.
