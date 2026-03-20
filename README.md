# ◆ LangGraph AI Agent

> A production-ready AI agent with web search, built with LangGraph, FastAPI, and Streamlit.

![Python](https://img.shields.io/badge/Python-3.10+-4a8c0f?style=flat-square&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-0.3+-1C3C3C?style=flat-square&logo=chainlink&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?style=flat-square&logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.43+-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-LLM-F55036?style=flat-square)

---

## What it does

This is a full-stack AI agent application that can answer questions and search the web in real time. You pick the model, write your own system prompt, toggle web search on or off, and chat — all from a clean UI.

```
User message → Streamlit UI → FastAPI backend → LangGraph Agent → Groq LLM + Tavily Search → Response
```

---

## Stack

| Layer | Technology |
|---|---|
| LLM | Groq (`llama-3.3-70b-versatile`, `qwen3-32b`) |
| Agent framework | LangGraph `create_react_agent` |
| Web search | Tavily Search API |
| Backend | FastAPI + Uvicorn |
| Frontend | Streamlit |
| Config | python-dotenv |

---

## Project structure

```
LLM_Projects/
├── ai_agent.py       # core agent logic (LangGraph + Groq + Tavily)
├── main.py           # FastAPI backend — exposes /chat endpoint
├── frontend.py       # Streamlit UI
├── .env              # API keys (never commit this)
├── .gitignore
└── README.md
```

---

## Quickstart

### 1. Clone the repo

```bash
git clone https://github.com/Muhammad-Awaix/ai-agent-langgraph.git
cd ai-agent-langgraph
```

### 2. Create virtual environment

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install langchain langchain-groq langchain-community langchain-tavily langgraph fastapi uvicorn streamlit python-dotenv requests
```

### 4. Set up API keys

Create a `.env` file in the root folder:

```env
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

Get your keys:
- Groq → [console.groq.com](https://console.groq.com) (free)
- Tavily → [app.tavily.com](https://app.tavily.com) (free tier)

### 5. Run the app

Open **two terminals**:

```bash
# Terminal 1 — backend
python main.py
```

```bash
# Terminal 2 — frontend
streamlit run frontend.py
```

Open your browser at `http://localhost:8501`

---

## API reference

### `POST /chat`

```json
{
  "model_name": "llama-3.3-70b-versatile",
  "system_prompt": "You are a helpful assistant",
  "messages": ["What is LangGraph?"],
  "allow_research": true
}
```

**Response:**

```json
{
  "response": "LangGraph is a framework for building stateful, multi-step agent workflows..."
}
```

**Allowed models:**
- `llama-3.3-70b-versatile`
- `qwen/qwen3-32b`
- `openai/gpt-oss-120b`

---

## Features

- Multi-model support — switch between models from the UI
- Real-time web search via Tavily (toggle on/off)
- Custom system prompt — define your agent's personality
- Chat history within session
- Clean dark UI built with Streamlit
- REST API — connect any frontend you want

---

## Author

**Muhammad Awais**
- GitHub: [@Muhammad-Awaix](https://github.com/Muhammad-Awaix)
- Co-founder: [Dev66.pk](https://dev66.pk) — online coding school

---

## License

MIT — use it, fork it, build on it.
