## 2025-05-15 - [Gradio Markdown & UI Consistency]
**Learning:** Broken markdown blocks (e.g., missing closing triple backticks) can disrupt the entire chat history rendering in Gradio. Consistency in placeholders and accessible labels (even when visually hidden) is key for a polished experience.
**Action:** Always verify that all markdown blocks are properly closed in stream outputs and use `show_label=False` for cleaner accessible inputs.
