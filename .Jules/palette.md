## 2025-05-15 - Improving Chat Reset UX and Accessibility

**Learning:** When adding a "clear history" feature to a Gradio Chatbot, it's not enough to just clear the chat component. To provide a seamless "restart" experience, you must also reset the agent's internal memory, clear session-specific state (like uploaded files), and cancel any ongoing asynchronous tasks to prevent the UI from being locked in a "running" state. Using `opacity: 0.7` for secondary information like footnotes is superior to hardcoded colors as it maintains readability and intent across light, dark, and custom themes.

**Action:** Always chain `chatbot.clear()` with a comprehensive reset function and use the `cancels` parameter for event handlers that might be running. Prefer relative styling (opacity) for de-emphasized text.
