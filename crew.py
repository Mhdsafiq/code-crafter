from crewai import Crew,Process
from tasks import research, write_code
from agent import search_agent, code_write
import os
import litellm

old_completion = litellm.completion
def patched_completion(*args, **kwargs):
    if "messages" in kwargs:
        for m in kwargs["messages"]:
            if "cache_breakpoint" in m:
                del m["cache_breakpoint"]
    return old_completion(*args, **kwargs)
litellm.completion = patched_completion

os.environ["TIKTOKEN_CACHE_DIR"] = r"D:\tiktoken_cache"
os.environ["CREWAI_TELEMETRY_DISABLED"] = "true"

crew=Crew(
    agents=[code_write],
    tasks=[write_code],
    process=Process.sequential, #PARALLEL
    verbose=False,
    max_rpm=2,
    memory=False   
)
user_topic = input("Enter your programming task: ")
result=crew.kickoff(inputs={  "topic": user_topic})
print("\n" + "="*50 + "\nFINAL RESULT:\n" + "="*50 + "\n")
print(result)