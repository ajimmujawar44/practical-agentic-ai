# 03 — Financial News Agent

## Overview

A financial news analysis application that searches the web for recent company-related news and uses an LLM to summarize the available results.

The project was developed to practise combining web retrieval with AI-generated financial news summaries.

## Technologies

* Python
* Agno
* Groq
* DDGS
* Python-dotenv

## Features

* Searches for financial news about a specified company.
* Collects relevant search-result titles, URLs, and summaries.
* Uses an LLM to organize and explain the retrieved information.
* Presents the output in Markdown format.

## How It Works

1. A company name is included in a search query.
2. DDGS retrieves available financial news results.
3. Python formats the results for the language model.
4. The Agno agent analyzes the supplied information.
5. The application displays a structured news summary.

## Setup

Install the required dependencies:

```powershell
python -m pip install -r requirements.txt
```

Add your Groq API key to `.env`:

```env
GROQ_API_KEY=your_groq_api_key
```

Run:

```powershell
python 03-financial-news-agent/financial_news_multi_agent.py
```

## Learning Outcomes

* Retrieving company-related news.
* Processing web search results.
* Using an LLM to summarize financial information.
* Building an AI workflow around external data.

## Limitations

The application analyzes the search results it receives. It does not guarantee complete coverage of the news or real-time market data. Verify important claims using the original linked sources.

This project is for educational purposes and does not provide personalized investment advice.

## Author

Ajim Mujawar
