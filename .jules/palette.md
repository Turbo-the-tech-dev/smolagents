## 2025-05-15 - [Initial setup]
**Learning:** This repository uses Gradio for its UI and has a suite of pytest tests.
**Action:** Always ensure Gradio-related tests pass and use existing Gradio components effectively.

## 2025-05-20 - [Gradio 6.x Accessibility and State Management]
**Learning:** In Gradio 6.x, adding an ARIA label via `html_attributes={"aria-label": "..."}` and setting `show_label=False` on a `gr.Textbox` is essential for maintaining accessibility while achieving a clean UI. Additionally, resetting complex UI state (like file logs and message history) after a `chatbot.clear()` event requires explicit chaining with `.then()` to ensure all `gr.State` components are cleared.
**Action:** Use `html_attributes` for ARIA labels on text inputs and explicitly reset all relevant `gr.State` components during clear events to avoid stale UI state.
