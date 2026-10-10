import streamlit as st

from ddgs import DDGS
from langchain_ollama import ChatOllama


# =========================================================
# 1. PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Ollama Financial AI",
    page_icon="📊",
    layout="wide"
)


# =========================================================
# 2. TITLE
# =========================================================

st.title("📊 Multi-Agent Financial Analysis")
st.caption("Powered by Ollama + DDGS + Open-Source LLM")


# =========================================================
# 3. OLLAMA MODEL
# =========================================================

@st.cache_resource
def load_model():

    return ChatOllama( model="deepseek-r1:1.5b", temperature=0.2)


llm = load_model()


# =========================================================
# 4. WEB SEARCH
# =========================================================

def search_web(query, max_results=3):

    try:

        results = DDGS().text(
            query,
            max_results=max_results
        )

        return results

    except Exception as e:

        return []


# =========================================================
# 5. FORMAT RESULTS
# =========================================================

def format_results(results):

    if not results:
        return "No search results found."

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
# 6. INPUT
# =========================================================

company = st.text_input(
    "🏢 Enter company name",
    placeholder="Example: Tesla, NVIDIA, Microsoft"
)


# =========================================================
# 7. BUTTON
# =========================================================

if st.button("🔍 Get Financial Insights"):

    if not company:

        st.warning("Please enter a company name.")

    else:

        # -------------------------------------------------
        # NEWS
        # -------------------------------------------------

        st.subheader("📰 Latest Financial News")

        with st.spinner("Searching financial news..."):

            news_results = search_web(
                f"latest financial news {company} October 2026",
                max_results=3
            )

        news_data = format_results(news_results)

        # -------------------------------------------------
        # COMPANY INSIGHTS
        # -------------------------------------------------

        st.subheader(f"🏢 {company} Insights")

        with st.spinner("Analyzing company information..."):

            company_results = search_web(
                f"{company} CEO industry revenue company overview",
                max_results=3
            )

        company_data = format_results(company_results)

        # -------------------------------------------------
        # MARKET TRENDS
        # -------------------------------------------------

        st.subheader("📈 Market Trend Analysis")

        with st.spinner("Analyzing market trends..."):

            trend_results = search_web(
                f"latest stock market trends October 2026 major companies",
                max_results=3
            )

        trend_data = format_results(trend_results)

        # =================================================
        # AI ANALYSIS
        # =================================================

        prompt = f"""
You are a financial research assistant.

Analyze the following research information.

COMPANY:
{company}

--------------------------------------------------
FINANCIAL NEWS
--------------------------------------------------

{news_data}

--------------------------------------------------
COMPANY INFORMATION
--------------------------------------------------

{company_data}

--------------------------------------------------
MARKET TRENDS
--------------------------------------------------

{trend_data}

--------------------------------------------------

Provide a concise report with:

1. Latest financial news
2. Company overview
3. Important market trends
4. Potential business implications
5. Sources

Rules:

- Use only the provided information.
- Do not invent facts.
- Do not invent prices or statistics.
- Clearly distinguish facts from analysis.
- Do not provide personalized investment advice.
"""

        with st.spinner("Ollama is analyzing the information..."):

            try:

                response = llm.invoke(prompt)

                st.subheader("🤖 AI Financial Analysis")

                st.markdown(response.content)

            except Exception as e:

                st.error(
                    f"Ollama error: {e}"
                )


# =========================================================
# 8. FOOTER
# =========================================================

st.divider()

st.caption(
    "Developed by Ajim Mujawar | "
    "Ollama + DDGS + LangChain"
)