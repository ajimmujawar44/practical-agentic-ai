# Agentic AI Projects

A collection of hands-on projects exploring **Agentic AI, Generative AI, Python functions, external tools, web search, financial data, and local LLM applications**.

Developed by **Ajim Mujawar** as part of my learning journey in Data Science, Generative AI, and Agentic AI.

## About This Repository

This repository contains six practical AI applications built to understand how language models can interact with tools, retrieve external information, process data, and generate useful responses.

The projects use Agno and Groq for agent-based applications, along with LangChain, Ollama, and Streamlit for a local LLM application.

## Projects

| No. | Project                    | Key Concepts                                |
| --- | -------------------------- | ------------------------------------------- |
| 01  | Stock Analysis Agent       | Agno, Groq, YFinance                        |
| 02  | Cricket AI Agent           | Web search, DDGS, AI summarization          |
| 03  | Financial News Agent       | Financial news retrieval and analysis       |
| 04  | Multi-Domain AI Agents     | Finance, crypto, e-commerce, travel, sports |
| 05  | Agent with Python Function | Custom functions, YFinance, retry handling  |
| 06  | Ollama Financial AI        | LangChain, Ollama, DeepSeek-R1, Streamlit   |

## Technology Stack

* **Programming language:** Python
* **Agent framework:** Agno
* **LLM provider:** Groq
* **Local LLM runtime:** Ollama
* **LLM integration:** LangChain
* **Web search:** DDGS
* **Financial data:** YFinance
* **Cryptocurrency data:** CoinGecko API
* **Web application:** Streamlit
* **Configuration:** Python dotenv

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/agentic-ai-projects.git
cd agentic-ai-projects
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the repository root and add the API keys required by the projects you intend to run.

Never commit your real `.env` file or expose API keys in screenshots.

### 5. Run a project

For example:

```powershell
python 02-cricket-ai-agent/cricket_agent.py
```

For the Streamlit application:

```powershell
streamlit run ollama-financial-ai/ollama_financial_agent.py
```

Run commands from the repository root. The exact command may need adjusting if a script expects files relative to its own folder.

## Local LLM Requirements

The Ollama Financial AI project requires Ollama to be installed separately and a local model to be downloaded.

For example:

```powershell
ollama pull deepseek-r1:1.5b
ollama list
```

## Learning Outcomes

Through these projects, I practised:

* Connecting LLMs with external tools.
* Retrieving and summarizing web information.
* Working with financial and cryptocurrency data.
* Creating reusable Python functions.
* Handling errors and retrying failed operations.
* Building a Streamlit interface around a local LLM.
* Understanding the differences between cloud-based and local model inference.

## Important Disclaimer

Financial outputs are for educational and informational purposes only. They may contain errors, delays, or incomplete data and should not be treated as financial advice.

Search results, stock prices, and other external data depend on the relevant services and their availability.

## Author

**Ajim Mujawar**

Interested in Data Science, Machine Learning, Generative AI, and Agentic AI.

* GitHub: https://github.com/ajimmujawar44

## License

This repository is intended for educational and portfolio purposes. Add a LICENSE file if you wish to specify the terms under which others may reuse your code.
