import os
from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.groq import Groq
from ddgs import DDGS


# =========================================================
# 1. LOAD API KEY
# =========================================================

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError(
        "GROQ_API_KEY not found. Please add it to your .env file."
    )


# =========================================================
# 2. WEB SEARCH TOOL
# =========================================================

def web_search(query: str) -> str:
    """
    Search the web for cricket information.
    """

    try:
        results = DDGS().text(
            query,
            max_results=3
        )

        if not results:
            return "No results found."

        output = []

        for result in results:

            title = result.get("title", "")
            url = result.get("href", "")
            body = result.get("body", "")

            output.append(
                f"Title: {title}\n"
                f"URL: {url}\n"
                f"Summary: {body}"
            )

        return "\n\n".join(output)

    except Exception as e:
        return f"Search error: {e}"


# =========================================================
# 3. CREATE AGENT
# =========================================================

cricket_agent = Agent(
    name="Cricket AI Assistant",

    model=Groq(
        id="openai/gpt-oss-20b",
        api_key=groq_api_key,

        request_params={
            "max_completion_tokens": 500
        }
    ),

    tools=[web_search],

    instructions=[
        "You are a cricket research assistant.",
        "Use web_search for current cricket information.",
        "Always call web_search with a query string.",
        "Do not invent information.",
        "Use the search results.",
        "Mention sources.",
        "Keep answers short."
    ],

    markdown=True
)


# =========================================================
# 4. QUERY
# =========================================================

query = """
Find recent international cricket updates.

Give:
1. Two recent updates
2. One upcoming match or tournament
3. One player update

Use web search.
Keep the answer short.
"""


# =========================================================
# 5. RUN AGENT
# =========================================================

try:

    print("\n" + "=" * 65)
    print("                 CRICKET AI ASSISTANT")
    print("=" * 65)
    print()

    response = cricket_agent.run(query)

    if response and response.content:
        print(response.content)
    else:
        print("The agent returned an empty response.")


except Exception as e:

    print("\nError while running Cricket AI Agent:")
    print(e)