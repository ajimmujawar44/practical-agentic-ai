
import os
from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools


# =====================================================
# 1. Load environment variables
# =====================================================

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError(
        "OPENAI_API_KEY not found. "
        "Add it to your .env file."
    )


# =====================================================
# 2. Create Cricket AI Agent
# =====================================================

cricket_agent = Agent(
    name="Cricket AI Assistant",

    model=OpenAIChat(
        id="gpt-4o",
        api_key=api_key
    ),

    tools=[
        DuckDuckGoTools()
    ],

    instructions=[
        "You are a cricket research assistant.",

        "Search the web for current cricket information "
        "before answering questions about live scores or news.",

        "LIVE MATCH SCORES:",
        "- Find the latest available score.",
        "- Identify both teams, innings, runs, wickets and overs.",
        "- Include the batting team, target and required run rate "
        "when available.",
        "- Explain the current match situation briefly.",
        "- Clearly state when a match has ended or no live match "
        "can be verified.",

        "PLAYER STATISTICS:",
        "- Find recent statistics for the requested player.",
        "- Include the last five matches when reliable data is available.",
        "- For batters, include runs, balls, strike rate and scores.",
        "- For bowlers, include overs, wickets, runs conceded and economy.",
        "- Identify the match format: Test, ODI or T20I.",
        "- Do not invent missing statistics.",

        "CRICKET NEWS:",
        "- Search for recent cricket news.",
        "- Include the publication date when available.",
        "- Summarize important match results, upcoming fixtures, "
        "injury updates and tournament news.",
        "- Prefer reputable cricket sources.",

        "OUTPUT FORMAT:",
        "- Use Markdown headings and tables.",
        "- Include source URLs for important factual claims.",
        "- Distinguish confirmed information from unverified reports.",
        "- State the date and time of the information when available.",
        "- If information cannot be verified, say so clearly."
    ],

    markdown=True
)


# =====================================================
# 3. Ask a question
# =====================================================

query = """
Give me a cricket update.

1. Find the latest available score for India vs Australia.
2. Summarize the match situation and key players.
3. Find Virat Kohli's statistics from his last five
   international matches, separating formats where possible.
4. Summarize the latest cricket news.
5. Include source URLs and publication dates where available.

Use tables for scores and player statistics.
Do not invent live scores or missing statistics.
"""

# =====================================================
# 4. Run the agent
# =====================================================

try:
    print("\n" + "=" * 60)
    print("       CRICKET AI ASSISTANT")
    print("=" * 60 + "\n")

    response = cricket_agent.run(query)

    if response and response.content:
        print(response.content)
    else:
        print("The agent returned no response.")

except Exception as e:
    print(f"Error while running Cricket AI Agent: {e}")