## 2025-05-15 - [Initial setup]
**Learning:** This repository uses Gradio for its UI and has a suite of pytest tests.
**Action:** Always ensure Gradio-related tests pass and use existing Gradio components effectively.

## 2025-05-15 - [Gradio Keyboard Shortcuts and Accessibility]
**Learning:** In Gradio 6.x multiline `gr.Textbox` components, the standard keyboard shortcut for triggering the `submit` event is `Ctrl/Cmd+Enter` rather than `Shift+Enter`. Also, when using `show_label=False` and `container=False` for a textbox, adding an ARIA label via `html_attributes` is essential for maintaining accessibility.
**Action:** Always verify the correct keyboard shortcuts in the specific Gradio version used and ensure ARIA labels are present for icon-only or label-less inputs.
