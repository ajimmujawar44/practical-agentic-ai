import os
import streamlit as st
from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.yfinance import YFinanceTools


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Ajim Mujawar | Financial AI",
    page_icon="📈",
    layout="wide"
)


# =========================================================
# LOAD ENVIRONMENT VARIABLES
# =========================================================

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")


# =========================================================
# CHECK API KEY
# =========================================================

if not groq_api_key:
    st.error(
        "GROQ_API_KEY not found.\n\n"
        "Please add your API key to the .env file."
    )
    st.stop()


# =========================================================
# COMPANY → STOCK SYMBOL
# =========================================================

def get_company_symbol(company: str) -> str:

    symbols = {
        "infosys": "INFY.NS",
        "tcs": "TCS.NS",
        "reliance": "RELIANCE.NS",
        "wipro": "WIPRO.NS",
        "hdfc bank": "HDFCBANK.NS",
        "icici bank": "ICICIBANK.NS",

        "tesla": "TSLA",
        "apple": "AAPL",
        "microsoft": "MSFT",
        "amazon": "AMZN",
        "google": "GOOGL",
        "alphabet": "GOOGL",
        "nvidia": "NVDA",
        "meta": "META",
        "facebook": "META",
        "netflix": "NFLX",
    }

    return symbols.get(
        company.strip().lower(),
        "Unknown"
    )


# =========================================================
# FINANCIAL AI AGENT
# =========================================================

agent = Agent(
    name="Ajim's Financial AI Agent",

    model=Groq(
        id="openai/gpt-oss-120b",
        api_key=groq_api_key
    ),

    tools=[
        YFinanceTools()
    ],

    instructions=[
        "Use the financial tools to retrieve stock information.",
        "Use tables to display stock data.",
        "Include analyst recommendations when available.",
        "Include important stock fundamentals when available.",
        "Clearly identify the stock symbol being analyzed.",
        "Do not invent financial data.",
        "If financial data is unavailable, clearly state that it is unavailable.",
        "Give concise and easy-to-understand explanations.",
    ],

    markdown=True,
)


# =========================================================
# DASHBOARD HEADER
# =========================================================

st.title("📈 Ajim Mujawar - Financial AI Dashboard")

st.markdown(
    """
    ### 🤖 AI-Powered Stock Analysis

    Analyze stock prices, financial fundamentals and
    analyst information using **Agno + Groq + Yahoo Finance**.
    """
)

st.divider()


# =========================================================
# COMPANY INPUT
# =========================================================

st.subheader("🔍 Stock Analysis")

col1, col2 = st.columns(2)


with col1:

    company_1 = st.text_input(
        "🏢 First Company",
        placeholder="Example: NVIDIA"
    )


with col2:

    company_2 = st.text_input(
        "🏢 Second Company (Optional)",
        placeholder="Example: Tesla"
    )


# =========================================================
# EXAMPLE COMPANIES
# =========================================================

st.caption(
    "Examples: NVIDIA, Tesla, Apple, Microsoft, Amazon, "
    "Google, Infosys, TCS, Reliance"
)


# =========================================================
# ANALYZE BUTTON
# =========================================================

if st.button(
    "🚀 Analyze Stock",
    type="primary",
    use_container_width=True
):

    # -----------------------------------------------------
    # Validate first company
    # -----------------------------------------------------

    if not company_1:

        st.warning(
            "⚠️ Please enter at least one company."
        )

        st.stop()


    # -----------------------------------------------------
    # Convert company names → symbols
    # -----------------------------------------------------

    symbol_1 = get_company_symbol(company_1)

    symbol_2 = None

    if company_2:

        symbol_2 = get_company_symbol(company_2)


    # -----------------------------------------------------
    # Check first company
    # -----------------------------------------------------

    if symbol_1 == "Unknown":

        st.error(
            f"❌ Company '{company_1}' was not found."
        )

        st.info(
            "Try: NVIDIA, Tesla, Apple, Microsoft, "
            "Amazon, Google, Infosys, TCS or Reliance."
        )

        st.stop()


    # =====================================================
    # BUILD AI QUERY
    # =====================================================

    query = f"""
    Analyze the stock:

    Company: {company_1}
    Symbol: {symbol_1}

    Provide the following information:

    1. Latest available stock price
    2. Stock price information
    3. Important financial fundamentals
    4. Analyst recommendations, if available
    5. Important financial metrics
    6. Company overview

    Use tables wherever appropriate.

    Use the available Yahoo Finance tools to retrieve
    financial information.

    Do not invent financial data.
    """


    # =====================================================
    # SECOND COMPANY COMPARISON
    # =====================================================

    if symbol_2 and symbol_2 != "Unknown":

        query += f"""

        Also analyze:

        Company: {company_2}
        Symbol: {symbol_2}

        Compare both companies using tables.

        Compare:

        - Stock price
        - Financial fundamentals
        - Analyst recommendations
        - Important financial metrics

        Clearly identify which information belongs
        to each company.
        """

    elif company_2:

        st.warning(
            f"⚠️ '{company_2}' was not found. "
            f"Only {company_1} will be analyzed."
        )


    # =====================================================
    # RUN AI AGENT
    # =====================================================

    with st.spinner(
        f"🤖 Analyzing {company_1} ({symbol_1})..."
    ):

        try:

            response = agent.run(query)


            # ---------------------------------------------
            # Display AI response
            # ---------------------------------------------

            if response and response.content:

                st.divider()

                st.subheader("📊 Financial Analysis")

                st.markdown(
                    response.content
                )

            else:

                st.warning(
                    "⚠️ The AI agent did not return a response."
                )


        except Exception as e:

            st.error(
                "❌ An error occurred while running the AI agent."
            )

            st.exception(e)


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "Built by Ajim Mujawar | "
    "Generative AI & Agentic AI Project"
)