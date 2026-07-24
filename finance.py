from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv

from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools


load_dotenv()

def build_agent():
    agent = Agent(
    tools=[DuckDuckGoTools(), YFinanceTools()],
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions = "You are a helpful and expert travel agent.",
    markdown=True,
    add_datetime_to_context=True,
)
    return agent

agent = build_agent()
agent.print_response("Share the NVDA stock price and analyst recommendations?")
