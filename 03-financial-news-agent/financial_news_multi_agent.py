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
        "GROQ_API_KEY not found in .env"
    )


# =========================================================
# 2. WEB SEARCH
# =========================================================

def search_financial_news(query, max_results=3):

    try:

        results = DDGS().text(
            query,
            max_results=max_results
        )

        return results

    except Exception as e:

        print("\nWeb search error:")
        print(e)

        return []


# =========================================================
# 3. SEARCH NVIDIA NEWS
# =========================================================

print("\n" + "=" * 65)
print("              FINANCIAL NEWS AI")
print("=" * 65)

print("\nSearching financial news...")

results = search_financial_news(
    "NVIDIA NVDA latest financial news September 2026",
    max_results=3
)


if not results:

    print("\nNo financial news results found.")
    raise SystemExit


print("Financial news search completed.")


# =========================================================
# 4. PREPARE SEARCH RESULTS
# =========================================================

news_text = ""

for i, result in enumerate(results, start=1):

    title = result.get("title", "")
    url = result.get("href", "")
    body = result.get("body", "")

    news_text += f"""
SOURCE {i}

Title:
{title}

URL:
{url}

Summary:
{body}

"""


# =========================================================
# 5. CREATE FINANCIAL AI AGENT
# =========================================================

financial_agent = Agent(

    name="Financial News Analyst",

    model=Groq(
        id="openai/gpt-oss-20b",
        api_key=groq_api_key,

        request_params={
            "max_completion_tokens": 500
        }
    ),

    instructions=[
        "You are a financial news research assistant.",
        "Analyze only the information provided.",
        "Do not invent financial data or news.",
        "Clearly separate facts from analysis.",
        "Mention the source website.",
        "Do not provide personalized investment advice.",
        "Keep the response concise."
    ],

    markdown=True
)


# =========================================================
# 6. ANALYZE NEWS
# =========================================================

prompt = f"""
Analyze the following recent NVIDIA financial news.

Provide:

1. Three important news points
2. What each news item means
3. Potential market impact
4. Whether each item is positive, negative, or mixed
5. Source website

Do not invent information.

News search results:

{news_text}
"""


# =========================================================
# 7. RUN AI
# =========================================================

print("\nGenerating AI analysis...\n")

try:

    response = financial_agent.run(prompt)

    if response and response.content:

        print("=" * 65)
        print("              FINANCIAL NEWS AI")
        print("=" * 65)
        print()

        print(response.content)

    else:

        print("The AI returned an empty response.")


except Exception as e:

    print("\nGroq error:")
    print(e)