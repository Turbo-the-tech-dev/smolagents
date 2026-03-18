## 2025-05-15 - [Initial setup]
**Learning:** This repository uses Gradio for its UI and has a suite of pytest tests.
**Action:** Always ensure Gradio-related tests pass and use existing Gradio components effectively.

## 2025-05-20 - [Micro-UX improvements for Gradio UI]
**Learning:** For subdued text (like footnotes) in Gradio, using `opacity: 0.7` is superior to hardcoded gray hex codes because it automatically adapts to light and dark themes while maintaining contrast.
**Action:** Prefer `opacity` over fixed colors for non-primary text.

**Learning:** Gradio 6 `gr.Textbox` labels are more reliably accessible when `container=True` is used, as it ensures proper wrapping and label association in the DOM.
**Action:** Use `container=True` for primary input fields to enhance screen reader support.

**Learning:** UX feedback for asynchronous actions like file uploads is cleaner using transient notifications (`gr.Info`) rather than persistent UI elements that clutter the sidebar.
**Action:** Use `gr.Info` and `gr.Warning` for status updates that don't require permanent visibility.
