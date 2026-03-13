import gradio as gr
from smolagents.agents import CodeAgent
from smolagents.models import Model
from smolagents.gradio_ui import GradioUI

class MockModel(Model):
    def __init__(self):
        super().__init__()
    def __call__(self, messages, stop_sequences=None, grammar=None):
        return "Final Answer: I am a mock agent."

agent = CodeAgent(tools=[], model=MockModel())
ui = GradioUI(agent)
app = ui.create_app()
# We don't need to launch it to just inspect the code or run a small test,
# but let's see if we can check the components.
print(f"Chatbot buttons: {ui.create_app().blocks[439] if hasattr(ui.create_app(), 'blocks') else 'N/A'}")
