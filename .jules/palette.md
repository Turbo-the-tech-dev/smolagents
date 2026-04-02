## 2025-05-15 - [Initial setup]
**Learning:** This repository uses Gradio for its UI and has a suite of pytest tests.
**Action:** Always ensure Gradio-related tests pass and use existing Gradio components effectively.

## 2025-05-20 - [Accessibility and Session Management Improvements]
**Learning:** In agent-based UIs, log metadata (like token usage and step duration) is often styled with low contrast for secondary emphasis, but it must still meet WCAG AA standards (at least 4.5:1) to remain readable. Additionally, explicit session 'clear' actions should reset both the backend agent memory and all frontend state trackers (like file upload logs) to prevent unexpected context leaks.
**Action:** Use high-contrast colors (e.g., #616161) for secondary text and ensure all session-related Gradio States are cleared during reset events.
