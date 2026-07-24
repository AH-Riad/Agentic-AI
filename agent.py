from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv

load_dotenv()

def build_agent():
    agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    markdown=True
)
    return agent

agent = build_agent()
agent.print_response("Share a 2 sentence horror story.")
