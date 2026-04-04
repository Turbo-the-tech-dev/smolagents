## 2025-05-15 - [Initial setup]
**Learning:** This repository uses Gradio for its UI and has a suite of pytest tests.
**Action:** Always ensure Gradio-related tests pass and use existing Gradio components effectively.

## 2025-05-20 - [Accessibility and Multi-theme Contrast]
**Learning:** Hardcoding hex colors for "subdued" text (like #bbbbc2) often leads to accessibility failures in light mode (low contrast) or dark mode. Using `opacity: 0.7;` on the container or element is a more robust, theme-agnostic way to achieve a subdued look while maintaining readable contrast across both Gradio themes.
**Action:** Prefer `opacity` or theme-aware CSS variables over hardcoded hex colors for secondary UI elements.
