# CrewAI Workshop

## Intro

This repo contains demos and code samples for the [Crew AI](https://github.com/crewAIInc/crewAI) workshop.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) - Required for containerization
- [dip](https://github.com/bibendi/dip) - Docker Interaction Process tool

## Installation

### 1. Install dip

You can install dip using RubyGems:

```bash
gem install dip
```

For alternative installation methods, please refer to the [dip documentation](https://github.com/bibendi/dip).

### 2. Set up environment variables

Copy the example environment file and update it with your API keys:

```bash
cp .env.example .env
```

Required API keys:
- `OPENAI_API_KEY` - Get from [OpenAI](https://platform.openai.com/)
- `MEM0_API_KEY` - Get from [Mem0](https://mem0.ai/)
- `SERPER_API_KEY` - Get from [Serper](https://serper.dev/)
- `OPENWEATHERMAP_API_KEY` - Get from [OpenWeatherMap](https://openweathermap.org/api)
- `GITHUB_PERSONAL_ACCESS_TOKEN` - Get from [GitHub Settings](https://github.com/settings/tokens)

### 3. Build the Docker container

```bash
docker compose build
```

## Running Demos

To run a specific demo, use the following command:

```bash
DEMO=<demo_number> dip crewai python run.py
```

For example, to run the first demo:

```bash
DEMO=1 dip crewai python run.py
```
## Workshop Plan

- Basics (Agent / Task / Crew / LLM)
- Basics with LangChain (Chain / Prompt / LLM)
- Structured output (Pydantic)
- Multiple agents (Multiple Tasks / Multiple Agents)
- Tracing (Phoenix setup)
- Tools (CrewAI Tools / LangChainTools)
- MCP (MCPServerAdapter / GitHub MCP)
- More building blocks (Conditional Tasks / Guardrails)
- Tasks Advanced flows ( Async Tasks Executions )
- CLI (Training / Testing / Chat)
- Knowledge (JSON / PDF / RAG)
- Memory (ShortTermMemory / LongTermMemory / EntityMemory / UserMemory)
- Coding execution (CodingAgent)
- Collaboration + Manager (Manager LLM / Hierarchical Execution)
- Planning (Planner LLM)
- Flows (Basics/State/Control/Router)
