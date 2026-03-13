## 2025-05-15 - [Initial setup]
**Learning:** This repository uses Gradio for its UI and has a suite of pytest tests.
**Action:** Always ensure Gradio-related tests pass and use existing Gradio components effectively.

## 2025-05-15 - [Gradio Accessibility & Theming]
**Learning:** Hardcoded hex colors (like #bbbbc2) for secondary text fail to maintain contrast across Gradio's light and dark themes. Using CSS 'opacity: 0.7' on the base text color ensures WCAG AA compliance in both modes. Additionally, 'html_attributes' on 'gr.Textbox' may not propagate ARIA labels to the underlying textarea in all Gradio 6.x configurations; using 'container=True' provides a more reliable way to ensure inputs have accessible labels.
**Action:** Use opacity for subdued text and prefer Gradio's native container/labeling system for accessibility over raw HTML attributes.
