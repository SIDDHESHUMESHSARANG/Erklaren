import os
import nest_asyncio

from dotenv import load_dotenv

load_dotenv()

from pydantic_ai.agent import Agent
from pydantic_ai.common_tools.tavily import tavily_search_tool

nest_asyncio.apply()

GROQ_API_KEY = os.environ["GROQ_API_KEY"]
TAVILY_API_KEY = os.environ["TAVILY_API_KEY"]

agent = Agent(
    model='groq:llama-3.1-8b-instant',         
    tools=[tavily_search_tool(TAVILY_API_KEY)],
    system_prompt="Search Tavily for the given query and return the result."
)

def getSearchResults(query: str) -> str:
    result = agent.run_sync(query)
    return result.output
