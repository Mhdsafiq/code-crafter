import os
from crewai_tools import TavilySearchTool

search_tool = TavilySearchTool(
    api_key=os.environ.get("TAVILY_API_KEY"),
    search_depth="advanced",
    max_results=2,
    include_raw_content=False
)