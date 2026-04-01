## 2025-05-15 - [Initial setup]
**Learning:** This repository uses Gradio for its UI and has a suite of pytest tests.
**Action:** Always ensure Gradio-related tests pass and use existing Gradio components effectively.

## 2025-05-22 - [Contrast in Step Footnotes]
**Learning:** Step footnotes using `#bbbbc2` on white backgrounds have a contrast ratio of ~1.76:1, which fails WCAG AA readability standards. Darkening to `#616161` provides a 6.6:1 ratio, satisfying accessibility requirements.
**Action:** Always check contrast ratios for small, secondary text elements in the UI to ensure they meet at least WCAG AA (4.5:1) standards.
