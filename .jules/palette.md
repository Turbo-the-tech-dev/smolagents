## 2025-05-15 - [Initial setup]
**Learning:** This repository uses Gradio for its UI and has a suite of pytest tests.
**Action:** Always ensure Gradio-related tests pass and use existing Gradio components effectively.

## 2025-05-16 - [Gradio 6.x Accessibility]
**Learning:** In Gradio 6.x, `gr.Textbox` components with `show_label=False` still benefit from explicit `aria-label` via `html_attributes` to ensure accessibility in container-less layouts.
**Action:** Always add `html_attributes={"aria-label": "..."}` to inputs when `show_label=False` or `container=False` is used.
