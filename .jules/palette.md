## 2025-05-15 - [Initial setup]
**Learning:** This repository uses Gradio for its UI and has a suite of pytest tests.
**Action:** Always ensure Gradio-related tests pass and use existing Gradio components effectively.
## 2025-05-15 - [Gradio UI State Management and Accessibility]
**Learning:** In Gradio 6.x, the 'chatbot.clear' event should be chained with '.then()' to fully reset session states (like stored messages or file logs) and utilize the 'cancels' parameter to ensure ongoing asynchronous tasks are terminated. For accessibility, using 'opacity' instead of hardcoded hex colors for subtext ensures better contrast across varying themes.
**Action:** Always chain UI state resets to the 'clear' event and prioritize relative styling (opacity, theme variables) for accessibility.
