
from crewai import Task
from agent import search_agent, code_write

research = Task(
    description=(
        "Research {topic}. "
        "Return only 3 bullet points and one short implementation idea."
    ),
    agent=search_agent,
    expected_output="A list of optimized code snippets along with explanations.",

)

write_code = Task(
    description=(
        "Write complete, runnable code for {topic} in the requested programming language (default to Python if unspecified). "
        "Do NOT include docstrings or explanations. "
        "Only code. "
        "If code is incomplete, continue until finished."
    ),
    agent=code_write,
    expected_output="Clean, efficient, and well-documented code snippets ready for use.",
    async_execution=False,# if it is true both agents work parallel
    output_file='codewrite.md'
)
