from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.team import Team

from agno.tools.duckduckgo import DuckDuckGoTools

load_dotenv()

eng_agent = Agent(name = "English Agent", role = "You answer questions in English")
ban = Agent(name = "Bangla Agent", role = "You answer questions in Bangla")
spn = Agent(name = "Spanish Agent", role = "You answer questions in Spanish")

team_leader = Team(
    
    name = "Answer and Translate Team",
    members=[eng_agent, ban, spn],
    tools=[DuckDuckGoTools()],
    model=Groq(id="llama-3.3-70b-versatile"),
    markdown=True,
    instructions="""
    All member agents must respond to answer the query in their respective languages.
    Do not route to just one agent.
    """
,
    show_members_responses=True,
    add_datetime_to_context=True,
)
team_leader.print_response("what is the capital of France?")
