## 2025-05-15 - [Initial setup]
**Learning:** This repository uses Gradio for its UI and has a suite of pytest tests.
**Action:** Always ensure Gradio-related tests pass and use existing Gradio components effectively.

## 2025-05-15 - [Gradio State Consistency]
**Learning:** When clearing a Chatbot in Gradio, it's crucial to also reset any associated state variables (like message history or upload logs) to maintain consistency. A callback used for `chatbot.clear` that targets multiple outputs must return the correct number of values (e.g., empty lists) rather than `None`.
**Action:** Use a helper method like `clear_all` to reset both the backend memory and the frontend state components.

## 2025-05-15 - [Accessibility & Contrast]
**Learning:** Using `opacity: 0.7` for subdued text ensures better WCAG AA contrast compliance across both light and dark themes compared to hardcoded hex colors like `#bbbbc2`.
**Action:** Prefer relative opacity or theme-aware variables for secondary text.
