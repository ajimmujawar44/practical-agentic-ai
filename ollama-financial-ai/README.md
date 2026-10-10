# Ollama Financial AI

## Overview

A Streamlit-based financial information application that combines web search with a locally running language model.

Unlike the cloud-based Groq projects, this application uses Ollama to run DeepSeek-R1 locally and LangChain to interact with the model.

## Technologies

* Python
* Streamlit
* LangChain
* Ollama
* DeepSeek-R1 1.5B
* DDGS

## Features

* Company-name input through a Streamlit interface.
* Web searches for company news and background information.
* Retrieval of broader stock-market trend information.
* Local LLM analysis of the collected search results.
* Browser-based interface for displaying the analysis.

## Architecture

1. The user enters a company name in Streamlit.
2. DDGS retrieves relevant web search results.
3. Python combines the results into a prompt.
4. LangChain sends the prompt to the local Ollama model.
5. DeepSeek-R1 generates an analysis.
6. Streamlit displays the response.

## Prerequisites

Install Ollama from:

https://ollama.com/

Download the model:

```powershell
ollama pull deepseek-r1:1.5b
```

Check the installed models:

```powershell
ollama list
```

## Setup

Install the Python dependencies from the repository root:

```powershell
python -m pip install -r requirements.txt
```

Ensure Ollama is running and the required model is available locally.

## Run the Application

From the repository root:

```powershell
streamlit run ollama-financial-ai/ollama_financial_agent.py
```

Streamlit will provide a local URL that you can open in your browser.

## Learning Outcomes

* Running a local language model.
* Using LangChain with ChatOllama.
* Retrieving external information through web search.
* Creating a web application with Streamlit.
* Understanding the difference between cloud-based and local LLM inference.

## Limitations

The model's responses depend on its capabilities and the quality of the retrieved search results. Local inference does not mean that web searches are performed offline; DDGS still uses an external search service.

The application provides educational information, not personalized financial advice.

## Author

Ajim Mujawar
