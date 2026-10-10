
import os
from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools


# ==========================================
# 1. Load Gemini API key
# ==========================================

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found. "
        "Add it to your .env file."
    )


# ==========================================
# 2. Create Cricket AI Agent
# ==========================================

cricket_agent = Agent(
    name="Cricket Analysis Agent",

    model=Gemini(
        id="gemini-3.8-flash",
        api_key=api_key
    ),

    tools=[DuckDuckGoTools()],

    instructions=[
        "You are an expert cricket research assistant.",

        "LIVE MATCH SCORES:",
        "- Search the web for the latest available scores.",
        "- Identify both teams, innings, runs, wickets and overs.",
        "- Explain the current match situation.",
        "- Include the target and required run rate when available.",
        "- Clearly state if the match has ended or a live score "
        "cannot be verified.",

        "PLAYER STATISTICS:",
        "- Find recent statistics for the requested player.",
        "- Include the last five international matches when "
        "reliable data is available.",
        "- Separate Test, ODI and T20I formats.",
        "- For batting, include runs, balls and strike rate "
        "when available.",
        "- For bowling, include overs, wickets, runs conceded "
        "and economy when available.",
        "- Never invent missing statistics.",

        "CRICKET NEWS:",
        "- Search for recent cricket news.",
        "- Cover match results, upcoming fixtures, injuries "
        "and tournament updates.",
        "- Include publication dates and source URLs when available.",
        "- Distinguish confirmed news from unverified reports.",

        "OUTPUT FORMAT:",
        "- Use Markdown headings and tables.",
        "- Include source URLs for important factual claims.",
        "- Mention the date and time of information when available.",
        "- If information cannot be verified, state that clearly."
    ],

    markdown=True
)


# ==========================================
# 3. Cricket Query
# ==========================================

query = """
Give me a cricket update covering these topics:

1. LIVE MATCH:
   Find the latest available score for India vs Australia.
   Summarize the match situation and key players.
   If no match is currently live, report the latest relevant
   completed match or upcoming fixture instead.

2. PLAYER STATISTICS:
   Find Virat Kohli's statistics from his last five
   international matches.
   Separate formats where possible and use a table.

3. CRICKET NEWS:
   Summarize the latest cricket news, including results,
   upcoming matches and tournament updates.

Include source URLs and publication dates when available.
Do not invent live scores or missing statistics.
"""


# ==========================================
# 4. Run the Agent
# ==========================================

try:
    print("\n" + "=" * 60)
    print("       GEMINI CRICKET AI ASSISTANT")
    print("=" * 60 + "\n")

    response = cricket_agent.run(query)

    if response and response.content:
        print(response.content)
    else:
        print("The agent returned no response.")

except Exception as e:
    print(f"Error while running Cricket AI Agent: {e}")