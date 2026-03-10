## 2025-05-15 - [Initial setup]
**Learning:** This repository uses Gradio for its UI and has a suite of pytest tests.
**Action:** Always ensure Gradio-related tests pass and use existing Gradio components effectively.
## 2025-05-15 - [Gradio UX patterns]
**Learning:** In Gradio, using hardcoded hex codes for subdued text (like footnotes) can fail WCAG AA contrast standards across light and dark themes. Setting 'opacity: 0.7' on the element ensures the contrast scales correctly with the theme's base text color. Also, using `gr.Info` and `gr.Warning` provides a much smoother user experience for transient status updates (like file uploads) than persistent UI components.
**Action:** Use opacity-based styling for secondary text and toast notifications for action feedback in Gradio interfaces.
