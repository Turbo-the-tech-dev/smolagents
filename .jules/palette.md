## 2025-05-15 - [Initial setup]
**Learning:** This repository uses Gradio for its UI and has a suite of pytest tests.
**Action:** Always ensure Gradio-related tests pass and use existing Gradio components effectively.

## 2026-03-07 - [UI/UX Polishing in Gradio]
**Learning:** For a cleaner UI in Gradio, transient notifications (`gr.Info`/`gr.Warning`) are superior to persistent status textboxes for feedback on asynchronous actions like file uploads.
**Action:** Use `gr.Info()` and `gr.Warning()` for transient user feedback.

**Learning:** WCAG AA contrast for subdued text should use `opacity: 0.7` instead of hardcoded hex codes to ensure compatibility with both light and dark themes in Gradio.
**Action:** Use `opacity: 0.7` for subdued text contrast.

**Learning:** Gradio 6 `gr.Textbox` supports `html_attributes` for passing ARIA labels to the underlying input element when the visible label is hidden.
**Action:** Use `html_attributes={'aria-label': '...'}` for hidden-label accessibility.
