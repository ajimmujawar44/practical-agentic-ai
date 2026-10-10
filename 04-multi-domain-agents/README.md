# 04 — Multi-Domain AI Agents

## Overview

A Python-based application demonstrating how AI agents can handle tasks across multiple domains, including financial news, cryptocurrency, e-commerce, travel, and sports.

Each domain uses a dedicated agent configured for a specific type of analysis. Python retrieves or prepares the relevant information before passing it to the appropriate agent.

## Technologies

* Python
* Agno
* Groq
* DDGS
* Requests
* CoinGecko API
* Python-dotenv

## Features

* Financial news search and analysis.
* Cryptocurrency price retrieval using CoinGecko.
* E-commerce product information search.
* Travel-related information search.
* Sports news retrieval and summarization.
* Domain-specific prompts and structured outputs.

## How It Works

1. Python retrieves information for the selected domain.
2. External data is prepared for the corresponding agent.
3. The Groq-powered agent analyzes the supplied information.
4. The application displays the result for each domain.

The current implementation runs the agents sequentially.

## Setup

Install the dependencies:

```powershell
python -m pip install -r requirements.txt
```

Configure your Groq API key in `.env`:

```env
GROQ_API_KEY=your_groq_api_key
```

Run:

```powershell
python 04-multi-domain-agents/multi_domain_agents.py
```

## Learning Outcomes

* Designing domain-specific AI agents.
* Separating data retrieval from LLM analysis.
* Integrating multiple external data sources.
* Reusing a common model configuration.
* Organizing a multi-domain AI workflow.

## Limitations

Search results and API responses depend on external service availability. Search-based travel information does not confirm live flight or hotel availability, and product search results do not guarantee current prices or stock.

## Author

Ajim Mujawar
