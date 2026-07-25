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
    model=Groq(id="openai/gpt-oss-20b"),
    instructions = "You are a helpful and expert travel agent.",
    markdown=True,
    add_datetime_to_context=True,
    db=SqliteDb(db_file="tmp/memory.db"),
    update_memory_on_run=True,
)
    return agent

agent = build_agent()

agent.print_response(
    "I am planing a trip to the capital of Spain?",
    user_id="sarah",
    session_id="onboarding",
)

agent.print_response(
    "How can you help me with my trip to this destination?",
    user_id="sarah",
    session_id="project-planning",
)