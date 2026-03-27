## 2025-05-15 - [Gradio UI Accessibility & UX Improvements]
**Learning:** In Gradio 6.10.0, the `gr.Textbox` component in multiline mode uses `Ctrl/Cmd+Enter` for submission, which differs from common user expectations of `Shift+Enter`. Communicating this in the placeholder is critical. Additionally, `html_attributes={"aria-label": "..."}` is necessary for accessibility when standard labels are hidden.
**Action:** Always include keyboard shortcut hints in placeholders for multiline textboxes and use `html_attributes` for ARIA labels when `show_label=False`.

## 2025-05-15 - [State Persistence in Gradio Event Handlers]
**Learning:** Returning a literal `[]` in a Gradio event handler that is mapped to a state component (like `file_uploads_log`) will overwrite that state, causing data loss across turns. The current state must be explicitly returned to persist it.
**Action:** Ensure event handlers return the existing state variables instead of reset values unless a reset is intended.
