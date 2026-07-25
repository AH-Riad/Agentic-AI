from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.db.sqlite import SqliteDb
from agno.tools.duckduckgo import DuckDuckGoTools

load_dotenv()
db_file = "tmp/memory_summarize_strategy.db"
db = SqliteDb(db_file=db_file)

def build_agent():
    agent = Agent(
    tools=[DuckDuckGoTools()],
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions = "You are a helpful and expert travel agent.",
    markdown=True,
    add_datetime_to_context=True,
    db=SqliteDb(db_file="tmp/memory.db"),
    update_memory_on_run=True,
)
    return agent

agent = build_agent()

agent.print_response(
    "I prefer email updates and morning meetings.",
    user_id="sarah",
    session_id="onboarding",
)

agent.print_response(
    "How should you schedule and send my project updates?",
    user_id="sarah",
    session_id="project-planning",
)