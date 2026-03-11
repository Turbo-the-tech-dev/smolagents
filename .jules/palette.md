## 2025-05-15 - [Initial setup]
**Learning:** This repository uses Gradio for its UI and has a suite of pytest tests.
**Action:** Always ensure Gradio-related tests pass and use existing Gradio components effectively.
## 2025-05-15 - [UI accessibility and theme compatibility]
**Learning:** Hardcoded hex colors for subdued text (like footnotes) can fail WCAG contrast standards in different themes. Using 'opacity: 0.7' allows the text to adapt while maintaining a consistent visual hierarchy.
**Action:** Use opacity or CSS variables instead of hardcoded grays for secondary UI elements.
