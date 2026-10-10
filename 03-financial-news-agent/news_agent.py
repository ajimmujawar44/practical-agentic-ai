import os

from dotenv import load_dotenv
from ddgs import DDGS

from agno.agent import Agent
from agno.models.groq import Groq


# =========================================================
# 1. LOAD ENVIRONMENT
# =========================================================

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY not found in .env file.")


# =========================================================
# 2. WEB SEARCH FUNCTION
# =========================================================

def search_web(query, max_results=3):

    try:

        results = DDGS().text(
            query,
            max_results=max_results
        )

        return results

    except Exception as e:

        print(f"Web search error: {e}")
        return []


# =========================================================
# 3. CREATE NEWS AGENT
# =========================================================

news_agent = Agent(

    name="Financial News Agent",

    model=Groq(
        id="openai/gpt-oss-20b",
        api_key=groq_api_key,
        request_params={
            "max_completion_tokens": 500
        }
    ),

    instructions=[
        "You are a financial news research assistant.",
        "Analyze only the provided search results.",
        "Summarize important financial news.",
        "Do not invent facts, prices or statistics.",
        "Mention source websites.",
        "Clearly distinguish facts from analysis.",
        "Keep the response concise.",
        "Do not provide personalized investment advice."
    ],

    markdown=True
)


# =========================================================
# 4. COMPANY INPUT
# =========================================================

company = input(
    "\nEnter company name (example: Tesla, NVIDIA): "
)


# =========================================================
# 5. SEARCH
# =========================================================

print("\nSearching financial news...")

results = search_web(
    f"latest financial news {company} October 2026",
    max_results=3
)


if not results:

    print("No financial news found.")
    raise SystemExit


# =========================================================
# 6. PREPARE RESULTS
# =========================================================

news_data = ""

for i, result in enumerate(results, start=1):

    news_data += f"""
SOURCE {i}

Title:
{result.get("title", "")}

URL:
{result.get("href", "")}

Summary:
{result.get("body", "")}

"""


# =========================================================
# 7. AI ANALYSIS
# =========================================================

prompt = f"""
Analyze the latest financial news about {company}.

Provide:

1. Two important news items
2. What each news item means
3. Potential business or market impact
4. Source website

Use only the information provided below.

News:

{news_data}
"""


print("\nGenerating AI analysis...\n")

try:

    response = news_agent.run(prompt)

    print("=" * 65)
    print("              FINANCIAL NEWS AGENT")
    print("=" * 65)
    print()

    if response and response.content:
        print(response.content)
    else:
        print("No response generated.")

except Exception as e:

    print("Groq error:")
    print(e)