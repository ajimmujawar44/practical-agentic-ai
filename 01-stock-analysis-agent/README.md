# 01 — Stock Analysis Agent

## Overview

A Python-based AI agent that retrieves available stock market information and generates a structured analysis using a language model.

The project demonstrates how an AI agent can use financial data tools to answer questions about publicly traded companies.

## Technologies

* Python
* Agno
* Groq
* YFinance
* Python-dotenv

## Features

* Retrieves available stock market information.
* Uses financial data tools to support its responses.
* Generates AI-powered explanations of stock information.
* Presents results in a readable format.

## How It Works

1. The user submits a stock-related question.
2. The Agno agent processes the request.
3. The agent uses the configured YFinance tools to retrieve relevant information.
4. Groq generates a response based on the available data.
5. The result is displayed in the terminal.

## Setup

Install the dependencies from the repository root:

```powershell
python -m pip install -r requirements.txt
```

Configure the required Groq API key in your `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

Run the project:

```powershell
python 01-stock-analysis-agent/stock_analysis_agent.py
```

## Learning Outcomes

* Understanding AI agents and tools.
* Connecting an LLM to financial data.
* Using YFinance in an AI workflow.
* Structuring financial information for analysis.

## Limitations

Market data availability and freshness depend on the data provider. AI-generated explanations may be inaccurate. This project is for learning purposes and is not financial advice.

## Author

Ajim Mujawar
