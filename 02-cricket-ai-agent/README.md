# 02 — Cricket AI Agent

## Overview

A Python application that searches for cricket-related information on the web and uses an LLM to summarize the retrieved results.

The project demonstrates how web search and language models can work together to answer questions about cricket news and events.

## Technologies

* Python
* Agno
* Groq
* DDGS
* Python-dotenv

## Features

* Searches for cricket-related news.
* Retrieves a limited set of web search results.
* Passes the retrieved information to an AI agent.
* Generates a readable summary of the results.

## How It Works

1. Python sends a cricket-related query to DDGS.
2. DDGS returns available search results.
3. The results are formatted and passed to the Agno agent.
4. The Groq model summarizes the supplied information.
5. The final response is printed in the terminal.

## Setup

Install the repository dependencies:

```powershell
python -m pip install -r requirements.txt
```

Configure your Groq API key in `.env`:

```env
GROQ_API_KEY=your_groq_api_key
```

Run:

```powershell
python 02-cricket-ai-agent/cricket_agent.py
```

## Learning Outcomes

* Using web search in an AI application.
* Passing external search results to an LLM.
* Summarizing information with an AI agent.
* Understanding the difference between retrieving information and analyzing it.

## Limitations

Search results depend on the search provider and may not include every relevant article. Verify important sports information against reliable sources.

## Author

Ajim Mujawar
