# 05 — Agent with Custom Python Function

## Overview

A financial analysis application that combines a custom Python function with an AI agent and financial data tools.

The custom function maps supported company names to stock ticker symbols. The agent then uses the supplied symbols and YFinance tools to prepare a comparison.

## Technologies

* Python
* Agno
* Groq
* YFinance
* Python-dotenv

## Features

* Custom company-to-ticker lookup function.
* Support for selected companies, including Apple, Google, NVIDIA, Tesla, Microsoft, Amazon, and Infosys.
* Retrieval of available financial information.
* AI-generated stock comparisons.
* Basic retry handling for failed agent requests.

## How It Works

1. The Python function receives a company name.
2. The function returns the corresponding ticker symbol.
3. The symbols are included in the analysis query.
4. The Agno agent uses YFinance tools to retrieve relevant financial information.
5. Groq generates a structured comparison.
6. The retry function attempts the request again if an exception occurs.

## Setup

Install the repository dependencies:

```powershell
python -m pip install -r requirements.txt
```

Configure the Groq API key in `.env`:

```env
GROQ_API_KEY=your_groq_api_key
```

Run:

```powershell
python 05-python-function-agent/agents_with_python_function.py
```

## Learning Outcomes

* Writing reusable Python functions.
* Mapping company names to stock symbols.
* Integrating custom logic into an AI workflow.
* Connecting agents with financial data tools.
* Handling failures with retry logic.

## Limitations

The ticker lookup supports only the companies explicitly defined in the mapping. Retry handling does not guarantee recovery from persistent errors, rate limits, or unavailable services.

Financial outputs are for educational purposes only and are not investment advice.

## Author

Ajim Mujawar
