from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use.agent.views import AgentHistoryList
from browser_use import Agent
import asyncio
import os

from dotenv import load_dotenv
load_dotenv()

# Set the environment variable to disable anonymized telemetry
os.environ["ANONYMIZED_TELEMETRY"] = "false"
os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")

async def main():
    agent = Agent(
        task="Find a one-way flight from Bali to Oman on 19 January 2025 on Google Flights. Return me the cheapest option.",
        llm=ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp"),
    )
    result = await agent.run()
    print(result)


asyncio.run(main())