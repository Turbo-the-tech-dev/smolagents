# Palette's UX Journal

This journal contains critical UX and accessibility learnings from working on the `smolagents` repository.

## 2025-05-15 - [Gradio 6.0 Breaking Changes]
**Learning:** Gradio 6.0+ introduced several breaking changes:
1. `theme` parameter moved from `Blocks` constructor to `launch()`.
2. `type="messages"` is now default and the parameter is removed from `Chatbot`.
3. `show_copy_button` removed from `Chatbot`, replaced by `buttons=["copy"]`.
4. Typo `resizeable` fixed to `resizable` in `Chatbot`.
**Action:** When updating Gradio, check component signatures and move `theme` to `launch()`.
