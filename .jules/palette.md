## 2025-05-15 - [Initial setup]
**Learning:** This repository uses Gradio for its UI and has a suite of pytest tests.
**Action:** Always ensure Gradio-related tests pass and use existing Gradio components effectively.

## 2025-05-16 - [Gradio Accessibility & Contrast]
**Learning:** In Gradio 6.x, `gr.Textbox` supports `html_attributes` for passing ARIA labels (e.g., `html_attributes={'aria-label': 'User input'}`), which is essential when visible labels are hidden. For text contrast, using `opacity: 0.7` is superior to hardcoded gray hex codes as it adapts to both light and dark themes.
**Action:** Use `html_attributes` for ARIA labels in Gradio components and prefer opacity for subdued text to ensure WCAG AA contrast across themes.
