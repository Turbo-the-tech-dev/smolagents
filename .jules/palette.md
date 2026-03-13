## 2025-05-14 - Theme-Adaptive Subdued Text
**Learning:** Using hardcoded hex colors (e.g., `#bbbbc2`) for subdued text like footnotes fails to maintain proper contrast across different themes (Light/Dark). Using `opacity: 0.7` on the default text color ensures the text remains readable and meets WCAG AA standards by adapting to the background theme.
**Action:** Always prefer `opacity` or theme-aware CSS variables over hardcoded gray hex codes for secondary UI elements.

## 2025-05-14 - Gradio 6.0 Theme Configuration
**Learning:** Gradio 6.0+ deprecated passing the `theme` parameter to the `gr.Blocks` constructor. It must now be passed to the `launch()` method to avoid `UserWarning` and ensure future compatibility.
**Action:** Move `theme` configuration from the Blocks definition to the application launch call.
