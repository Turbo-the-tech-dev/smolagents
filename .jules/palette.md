## 2025-05-15 - [Initial setup]
**Learning:** This repository uses Gradio for its UI and has a suite of pytest tests.
**Action:** Always ensure Gradio-related tests pass and use existing Gradio components effectively.

## 2025-05-20 - [Gradio UI Polishing]
**Learning:** Using `opacity: 0.7` for secondary text (like footnotes) is more robust for theme compatibility than hardcoded hex values, ensuring WCAG contrast compliance in both light and dark modes.
**Action:** Prefer opacity over hardcoded gray hex codes for secondary UI elements.

**Learning:** The native `gr.Chatbot` clear button only clears the UI component; manual chaining with `.then()` is required to reset associated `gr.State` variables and cancel ongoing background tasks.
**Action:** Always use `.then()` reset chains when enabling native clear buttons for complex stateful interfaces.
