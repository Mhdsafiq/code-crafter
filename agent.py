import os
from crewai import Agent, LLM
from tools import search_tool

llm = LLM(
    model="groq/llama-3.1-8b-instant",
    api_key=os.environ.get("GROQ_API_KEY"),
    temperature=0.2,
    max_tokens=900 
)

search_agent = Agent(
    role="CodeResearcher",
    goal="find optimized code solutions",
    llm=llm,
    backstory=(
        "Find the best implementation for the task. "
        "Summarize concisely. No long explanations."
    ),
    verbose=True,
    allow_delegation=False,
    #tools=[search_tool]
)

code_write = Agent(
    role="CodeWriter",
    goal="write clean and optimized code",
    llm=llm,
    backstory=(
        "Write clean, efficient, production-quality code "
        "based on the given research."
    ),
    verbose=False,
    allow_delegation=False
)
