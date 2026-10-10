import os
import requests

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
    raise ValueError(
        "GROQ_API_KEY not found. Please add it to your .env file."
    )


# =========================================================
# 2. COMMON GROQ MODEL
# =========================================================

def create_model():
    return Groq(
        id="openai/gpt-oss-20b",
        api_key=groq_api_key,
        request_params={
            "max_completion_tokens": 400
        }
    )


# =========================================================
# 3. WEB SEARCH FUNCTION
# =========================================================

def web_search(query, max_results=3):

    try:

        results = DDGS().text(
            query,
            max_results=max_results
        )

        if not results:
            return []

        return results

    except Exception as e:

        print(f"Web search failed: {e}")

        return []


# =========================================================
# 4. FORMAT SEARCH RESULTS
# =========================================================

def format_results(results):

    if not results:
        return "No results found."

    text = ""

    for i, result in enumerate(results, start=1):

        text += f"""
SOURCE {i}

Title:
{result.get("title", "")}

URL:
{result.get("href", "")}

Summary:
{result.get("body", "")}

"""

    return text


# =========================================================
# 5. CRYPTO DATA FUNCTION
# =========================================================

def get_bitcoin_price():

    try:

        url = (
            "https://api.coingecko.com/api/v3/simple/price"
            "?ids=bitcoin&vs_currencies=usd"
        )

        response = requests.get(
            url,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        return data["bitcoin"]["usd"]

    except Exception as e:

        return f"Unable to retrieve Bitcoin price: {e}"


# =========================================================
# 6. CREATE SPECIALIST AGENTS
# =========================================================

news_agent = Agent(

    name="Financial News Agent",

    model=create_model(),

    instructions=[
        "You are a financial news specialist.",
        "Analyze the provided financial news.",
        "Do not invent information.",
        "Mention important sources.",
        "Keep the answer concise."
    ],

    markdown=True
)


crypto_agent = Agent(

    name="Crypto Analysis Agent",

    model=create_model(),

    instructions=[
        "You are a cryptocurrency research specialist.",
        "Analyze the provided cryptocurrency information.",
        "Do not invent prices or statistics.",
        "Explain the information clearly.",
        "Do not provide personalized investment advice.",
        "Keep the answer concise."
    ],

    markdown=True
)


ecommerce_agent = Agent(

    name="E-Commerce Agent",

    model=create_model(),

    instructions=[
        "You are an e-commerce research specialist.",
        "Analyze product search results.",
        "Compare products using only the provided information.",
        "Do not invent prices or ratings.",
        "Mention source websites.",
        "Keep the answer concise."
    ],

    markdown=True
)


travel_agent = Agent(

    name="Travel Research Agent",

    model=create_model(),

    instructions=[
        "You are a travel research specialist.",
        "Analyze the provided travel search results.",
        "Do not invent flight or hotel prices.",
        "Clearly distinguish search information from suggestions.",
        "Keep the answer concise."
    ],

    markdown=True
)


sports_agent = Agent(

    name="Sports Research Agent",

    model=create_model(),

    instructions=[
        "You are a sports research specialist.",
        "Analyze the provided sports information.",
        "Do not invent scores, statistics or results.",
        "Mention sources when available.",
        "Keep the answer concise."
    ],

    markdown=True
)


# =========================================================
# 7. DISPLAY PROJECT HEADER
# =========================================================

print("\n" + "=" * 70)
print("                 MULTI-DOMAIN AI AGENTS")
print("=" * 70)


# =========================================================
# 8. FINANCIAL NEWS
# =========================================================

print("\n[1/5] Searching financial news...")

financial_results = web_search(
    "latest Tesla NVIDIA financial news October 2026",
    max_results=3
)

financial_data = format_results(financial_results)

financial_prompt = f"""
Analyze the following financial news.

Give:
1. Two important news points
2. What they mean
3. Potential market impact
4. Sources

News:

{financial_data}
"""

try:

    response = news_agent.run(financial_prompt)

    print("\n--- FINANCIAL NEWS ---")

    if response and response.content:
        print(response.content)

except Exception as e:

    print("Financial agent error:", e)


# =========================================================
# 9. CRYPTO
# =========================================================

print("\n[2/5] Getting Bitcoin price...")

bitcoin_price = get_bitcoin_price()

crypto_prompt = f"""
Analyze this Bitcoin price information:

Current Bitcoin price:
${bitcoin_price}

Explain:
1. Current price
2. What the price represents
3. Important limitation of this simple price lookup

Do not predict the future price.
"""

try:

    response = crypto_agent.run(crypto_prompt)

    print("\n--- CRYPTO ANALYSIS ---")

    if response and response.content:
        print(response.content)

except Exception as e:

    print("Crypto agent error:", e)


# =========================================================
# 10. E-COMMERCE
# =========================================================

print("\n[3/5] Searching product information...")

product_results = web_search(
    "iPhone 15 price reviews specifications",
    max_results=3
)

product_data = format_results(product_results)

product_prompt = f"""
Analyze these product search results.

Product:
iPhone 15

Provide:
1. Main features
2. Price information if available
3. Review information if available
4. Important differences
5. Sources

Do not invent information.

Search results:

{product_data}
"""

try:

    response = ecommerce_agent.run(product_prompt)

    print("\n--- E-COMMERCE ANALYSIS ---")

    if response and response.content:
        print(response.content)

except Exception as e:

    print("E-commerce agent error:", e)


# =========================================================
# 11. TRAVEL
# =========================================================

print("\n[4/5] Searching travel information...")

travel_results = web_search(
    "Paris travel flights hotels November 2026",
    max_results=3
)

travel_data = format_results(travel_results)

travel_prompt = f"""
Analyze these travel search results for Paris.

Provide:
1. Travel information found
2. Flight information if available
3. Hotel information if available
4. Useful travel considerations
5. Sources

Do not invent prices or availability.

Search results:

{travel_data}
"""

try:

    response = travel_agent.run(travel_prompt)

    print("\n--- TRAVEL ANALYSIS ---")

    if response and response.content:
        print(response.content)

except Exception as e:

    print("Travel agent error:", e)


# =========================================================
# 12. SPORTS
# =========================================================

print("\n[5/5] Searching sports information...")

sports_results = web_search(
    "latest NBA news October 2026",
    max_results=3
)

sports_data = format_results(sports_results)

sports_prompt = f"""
Analyze these NBA search results.

Provide:
1. Two important updates
2. Players or teams mentioned
3. Important statistics only if provided
4. Sources

Do not invent information.

Search results:

{sports_data}
"""

try:

    response = sports_agent.run(sports_prompt)

    print("\n--- SPORTS NEWS ---")

    if response and response.content:
        print(response.content)

except Exception as e:

    print("Sports agent error:", e)


# =========================================================
# 13. COMPLETE
# =========================================================

print("\n" + "=" * 70)
print("                 ALL AGENTS COMPLETED")
print("=" * 70)