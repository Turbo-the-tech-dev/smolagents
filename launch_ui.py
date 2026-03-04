from smolagents import CodeAgent, GradioUI, LiteLLMModel
import os

model = LiteLLMModel(model_id="gpt-4o")
agent = CodeAgent(tools=[], model=model)
ui = GradioUI(agent, file_upload_folder="uploads")

if __name__ == "__main__":
    ui.launch(share=False)
