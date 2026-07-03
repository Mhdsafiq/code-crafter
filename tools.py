from crewai_tools import TavilySearchTool

search_tool = TavilySearchTool(
    api_key="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",
    search_depth="advanced",
    max_results=2,
    include_raw_content=False
)