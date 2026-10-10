import os

from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.yfinance import YFinanceTools


# =========================================================
# LOAD ENVIRONMENT VARIABLES
# =========================================================

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError(
        "GROQ_API_KEY not found. Please add it to your .env file."
    )


# =========================================================
# COMPANY SYMBOL TOOL
# =========================================================

def get_company_symbol(company: str) -> str:

    symbols = {
        "Tesla": "TSLA",
        "Apple": "AAPL",
        "Microsoft": "MSFT",
        "Amazon": "AMZN",
        "Google": "GOOGL",
        "NVIDIA": "NVDA",
        "Meta": "META",
        "Infosys": "INFY",
        "Phidata": "MSFT"
    }

    return symbols.get(company, "Unknown")


# =========================================================
# STOCK ANALYSIS AGENT
# =========================================================

stock_agent = Agent(

    name="Stock Analysis Agent",

    model=Groq(
        id="openai/gpt-oss-120b",

        request_params={
            "max_completion_tokens": 1200
        }
    ),

    tools=[
        YFinanceTools(all=True),
        get_company_symbol
    ],

    instructions=[
        "You are a financial research assistant.",
        "Use Yahoo Finance tools for stock information.",
        "Use the company-symbol tool when a company name is provided.",
        "Do not invent financial data.",
        "Keep the response concise.",
        "Use Markdown tables when useful.",
        "Clearly identify ticker symbols.",
        "This is financial research information, not personalized investment advice."
    ],

    markdown=True
)


# =========================================================
# USER QUERY
# =========================================================

query = """
Compare Tesla (TSLA) and Microsoft (MSFT).

Provide:

1. Current stock price
2. Market capitalization
3. Revenue
4. Profitability
5. Analyst recommendations
6. Key differences

Use a concise Markdown table.

Do not invent missing information.
"""


# =========================================================
# RUN AGENT
# =========================================================

try:

    print("\n" + "=" * 65)
    print("             STOCK ANALYSIS AI")
    print("=" * 65)
    print()

    response = stock_agent.run(query)

    if response and response.content:
        print(response.content)
    else:
        print("The agent returned an empty response.")


except Exception as e:

    print("\nError while running Stock Analysis Agent:")
    print(e)