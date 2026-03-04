## 2025-05-15 - [Initial setup]
**Learning:** This repository uses Gradio for its UI and has a suite of pytest tests.
**Action:** Always ensure Gradio-related tests pass and use existing Gradio components effectively.

## 2025-05-20 - [Accessibility Contrast for Footnotes]
**Learning:** The default subdued text color (#bbbbc2) in `gradio_ui.py` fails WCAG AA contrast standards. Using `#6b7280` provides a compliant 4.5:1 ratio while maintaining a "subdued" look.
**Action:** Use `#6b7280` or darker for small/subdued UI text to ensure readability for all users.
