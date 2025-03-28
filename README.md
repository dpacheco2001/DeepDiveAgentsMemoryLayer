### Made by Diego Pacheco
# Deep Dive: Agents Memory Layer

## Overview
This research repository is dedicated to exploring and understanding the memory layer capabilities in AI agents. It focuses on investigating effective memory management techniques, analyzing how agent behavior can be modified through persistent memories, and developing advanced memory architectures for more contextually aware AI systems.

## Research Focus Areas
- Memory persistence and retrieval strategies in conversational agents
- Dynamic behavior adaptation based on accumulated memories
- Effective memory encoding and representation techniques
- Long-term vs. short-term memory management
- Memory contextualization and relevance assessment
- Memory-augmented reasoning and decision making

## Technologies
This research primarily leverages:
- [LangGraph](https://github.com/langchain-ai/langgraph): For building structured, stateful multi-agent systems
- [LangChain](https://github.com/langchain-ai/langchain): Core framework for language model applications
- OpenAI models: For agent intelligence and reasoning capabilities
- DeepSeek models: For alternative reasoning approaches
- Custom memory storage solutions: For experimenting with different memory persistence strategies

## Setup & Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/DeepDiveAgentsMemoryLayer.git

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
# Copy .env.example to .env and add your API keys