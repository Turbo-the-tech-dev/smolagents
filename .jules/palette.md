## 2025-05-15 - [Initial setup]
**Learning:** This repository uses Gradio for its UI and has a suite of pytest tests.
**Action:** Always ensure Gradio-related tests pass and use existing Gradio components effectively.

## 2025-05-15 - Gradio State Persistence in Event Chains
**Learning:** In Gradio event chains (`.then()`), returning a value for a state component (like `gr.State`) that is a reset (e.g., `[]`) instead of the current state variable will clear that state for all subsequent functions in the chain.
**Action:** Always return the current state variable in event handlers if the intention is to persist that data across multi-turn interactions or multiple steps in an event sequence.
