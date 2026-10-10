import streamlit as st
import os

from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools


# =========================================================
# 1. LOAD ENVIRONMENT VARIABLES
# =========================================================

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("GEMINI_API_KEY not found in .env file.")
    st.stop()


# =========================================================
# 2. CREATE CRICKET AI AGENT
# =========================================================

cricket_agent = Agent(
    name="Cricket Analysis Agent",

    model=Gemini(
        id="gemini-3.8-flash",
        api_key=api_key
    ),

    tools=[DuckDuckGoTools()],

    instructions=[
        "You are an expert cricket research assistant.",

        # -------------------------
        # LIVE MATCH
        # -------------------------
        "LIVE MATCH:",
        "- Search the web for the latest available cricket score.",
        "- Identify both teams, innings, runs, wickets and overs.",
        "- Mention the current match situation.",
        "- Include target and required run rate when available.",
        "- Do not invent live scores.",
        "- If no live match can be verified, clearly say so.",

        # -------------------------
        # PLAYER STATISTICS
        # -------------------------
        "PLAYER STATISTICS:",
        "- Find recent statistics for the requested player.",
        "- Include the last five international matches when available.",
        "- Separate Test, ODI and T20I formats when possible.",
        "- For batting include runs, balls and strike rate.",
        "- For bowling include overs, wickets, runs conceded and economy.",
        "- Do not invent missing statistics.",

        # -------------------------
        # CRICKET NEWS
        # -------------------------
        "CRICKET NEWS:",
        "- Search for the latest cricket news.",
        "- Include match results and upcoming matches.",
        "- Include important injury updates.",
        "- Include tournament updates.",
        "- Mention publication dates when available.",
        "- Include source URLs when available.",

        # -------------------------
        # OUTPUT
        # -------------------------
        "OUTPUT FORMAT:",
        "- Use Markdown headings.",
        "- Use Markdown tables for scores and statistics.",
        "- Keep the response organized and easy to read.",
        "- Clearly distinguish verified information from unavailable information."
    ],

    markdown=True
)


# =========================================================
# 3. STREAMLIT PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="🏏 Live Cricket Updates",
    page_icon="🏏",
    layout="wide"
)


# =========================================================
# 4. PAGE TITLE
# =========================================================

st.title("🏏 Cricket AI")
st.subheader("Live Scores • Player Statistics • Cricket News")

st.divider()


# =========================================================
# 5. USER INPUT
# =========================================================

col1, col2 = st.columns(2)

with col1:
    match_query = st.text_input(
        "🏏 Enter Match",
        placeholder="Example: India vs Australia"
    )

with col2:
    player_query = st.text_input(
        "👤 Enter Player",
        placeholder="Example: Virat Kohli"
    )


# =========================================================
# 6. GET CRICKET UPDATES BUTTON
# =========================================================

if st.button("🔍 Get Cricket Updates"):

    # -------------------------
    # Validate input
    # -------------------------

    if not match_query and not player_query:

        st.warning(
            "Please enter a match or player name."
        )
        st.stop()


    # -------------------------
    # Build query
    # -------------------------

    query_parts = []

    if match_query:
        query_parts.append(
            f"""
            Find the latest available score and match situation
            for {match_query}.
            """
        )

    if player_query:
        query_parts.append(
            f"""
            Find the recent international statistics for
            {player_query}, preferably the last five matches.
            """
        )

    query_parts.append(
        """
        Also find the latest important cricket news.

        Use reliable web search results.
        Include source URLs and publication dates where available.
        Do not invent unavailable information.
        """
    )

    query = "\n".join(query_parts)


    # =====================================================
    # 7. RUN AGENT
    # =====================================================

    with st.spinner("🔎 Searching cricket information..."):

        try:

            response = cricket_agent.run(query)

            # Get actual text from Agno response
            result = response.content

            if result:
                st.success("Cricket information fetched successfully!")

                st.markdown(result)

            else:
                st.warning(
                    "The agent returned an empty response."
                )

        except Exception as e:

            st.error(
                f"Error while fetching cricket data:\n\n{e}"
            )


# =========================================================
# 8. FOOTER
# =========================================================

st.divider()

st.markdown(
    """
    <div style="text-align: center; padding: 10px;">
        <p style="font-size: 16px; margin-bottom: 5px;">
            🏏 <b>Cricket AI Assistant</b>
        </p>
        <p style="font-size: 14px;">
            Powered by OpenAI + Agno + DuckDuckGo
        </p>
        <p style="font-size: 14px;">
            Developed by <b>Ajim Mujawar</b>
        </p>
    </div>
    """,
    unsafe_allow_html=True
)