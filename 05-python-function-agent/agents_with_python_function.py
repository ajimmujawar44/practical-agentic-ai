import time
import random

from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.yfinance import YFinanceTools


# =========================================================
# 1. Load environment variables
# =========================================================

load_dotenv()


# =========================================================
# 2. Custom Python Function
# =========================================================

def lookup_company_symbol(company: str) -> str:
    """
    Convert a company name into its stock ticker symbol.
    """

    symbols = {
        "Infosys": "INFY",
        "Tesla": "TSLA",
        "Apple": "AAPL",
        "Microsoft": "MSFT",
        "Amazon": "AMZN",
        "Google": "GOOGL",
        "NVIDIA": "NVDA",
        "Meta": "META"
    }

    return symbols.get(company.strip().title(), "Unknown")


# =========================================================
# 3. Create Groq Model
# =========================================================

model = Groq(
    id="openai/gpt-oss-20b",
    request_params={
        "max_completion_tokens": 500
    }
)


# =========================================================
# 4. Stock Agent
# =========================================================

stock_agent = Agent(
    name="Stock Analysis Agent",
    model=model,

    tools=[
        YFinanceTools(all=True)
    ],

    instructions=[
        "Analyze stock market information.",
        "Use the provided company symbols when available.",
        "Fetch stock price and fundamental information.",
        "Compare companies clearly.",
        "Present the result in markdown.",
        "Do not invent financial data."
    ],

    markdown=True
)


# =========================================================
# 5. Retry Function
# =========================================================

def run_with_retry(agent, query, retries=3, delay=5):

    for attempt in range(1, retries + 1):

        try:
            print(f"\nAttempt {attempt}/{retries}")

            response = agent.run(query)

            return response

        except Exception as e:

            print(f"Error: {e}")

            if attempt < retries:

                wait_time = random.uniform(
                    delay,
                    delay + 3
                )

                print(
                    f"Retrying in {wait_time:.1f} seconds..."
                )

                time.sleep(wait_time)

            else:

                print(
                    "Maximum retry attempts reached."
                )

                return None


# =========================================================
# 6. Company Symbols
# =========================================================

apple_symbol = lookup_company_symbol("Apple")
google_symbol = lookup_company_symbol("Google")


print("\nCompany Symbol Lookup")
print("---------------------")
print(f"Apple  → {apple_symbol}")
print(f"Google → {google_symbol}")


# =========================================================
# 7. Prepare Query
# =========================================================

query = f"""
Compare Apple and Google based on their latest available
stock information.

Apple ticker: {apple_symbol}
Google ticker: {google_symbol}

Include:

1. Current/latest available stock price
2. Basic company fundamentals
3. Important differences
4. A concise comparison table

Use factual information only.
Mention when information is unavailable.
"""


# =========================================================
# 8. Run Agent with Retry
# =========================================================

print("\nRunning Finance Agent...")
print("------------------------")

response = run_with_retry(
    stock_agent,
    query
)


# =========================================================
# 9. Display Result
# =========================================================

if response:

    print("\n" + "=" * 70)
    print("FINANCE AGENT RESULT")
    print("=" * 70)

    print(response.content)

else:

    print("\n❌ Failed to complete the finance analysis.")