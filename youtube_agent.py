from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.db.sqlite import SqliteDb
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.youtube import YouTubeTools

load_dotenv()
db_file = "tmp/memory_summarize_strategy.db"
db = SqliteDb(db_file=db_file)

def build_agent():
    agent = Agent(
    tools=[YouTubeTools()],
    model=Groq(id="openai/gpt-oss-20b"),
    description="You are a YouTube agent. Obtain the captions of a YouTube video and answer questions.",
    markdown=True,
    add_datetime_to_context=True,
    db=SqliteDb(db_file="tmp/memory.db"),
    update_memory_on_run=True,
)
    return agent

agent = build_agent()

agent.print_response("Summarize this video https://www.youtube.com/watch?v=l-6Pm-112io", markdown=True)