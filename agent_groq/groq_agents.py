
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq

# Load API keys from .env
load_dotenv()

# Create the AI agent
agent = Agent(
    model=Groq(id="qwen/qwen3.8-27b"),
    markdown=True
)

# Ask a question
agent.print_response("Give me an overview of NVIDIA stock.")