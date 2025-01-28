import gradio as gr
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
import asyncio
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set the environment variable to disable anonymized telemetry
os.environ["ANONYMIZED_TELEMETRY"] = "false"
os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")

# Define a function to run the agent logic
async def agent_logic(task):
    agent = Agent(
    task=task,
    llm=ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp"),
    )
    result = await agent.run()
    return result

# A wrapper to run the async function from sync Gradio context
def run_agent(task):
    return asyncio.run(agent_logic(task))

# Add a second interface to integrate the agent logic
with gr.Blocks() as app:
    gr.Markdown("### Browser-based Agent with Logic Execution")
    demo = gr.Interface(fn=run_agent, inputs="textbox", outputs="textbox")

# Launch the interface
if __name__ == "__main__":
    app.launch(show_error=True)