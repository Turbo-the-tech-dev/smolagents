## 2025-05-15 - [Initial setup]
**Learning:** This repository uses Gradio for its UI and has a suite of pytest tests.
**Action:** Always ensure Gradio-related tests pass and use existing Gradio components effectively.

## 2025-05-15 - [Branding and Accessibility in Gradio]
**Learning:** In Gradio 6.x, `gr.Image` in sidebars can show unwanted interactive overlays even if `interactive=False`. Using `gr.HTML` with a standard `<img>` tag is more reliable for static branding. Also, using `opacity` instead of hardcoded hex colors for text ensures better accessibility across themes.
**Action:** Use `gr.HTML` for static mascot/logos and `opacity` for secondary text in Gradio interfaces.
