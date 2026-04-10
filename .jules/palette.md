## 2025-05-15 - [Initial setup]
**Learning:** This repository uses Gradio for its UI and has a suite of pytest tests.
**Action:** Always ensure Gradio-related tests pass and use existing Gradio components effectively.

## 2025-05-15 - [Gradio UI Accessibility and State Management]
**Learning:** To ensure WCAG AA compliance and theme compatibility in Gradio, use `opacity` or theme variables instead of hardcoded hex colors for secondary text. For complex state management (e.g. file uploads), chaining `.then()` after `chatbot.clear()` is necessary to reset all session state variables alongside the agent memory.
**Action:** Use `opacity: 0.7` for subdued text and ensure all session `gr.State` variables are reset in a `.then()` block after a clear event.
