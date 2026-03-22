from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
load_dotenv()

def get_response_from_ai(llm_id, query, allow_search, system_prompt, chat_history=[]):
    
    llm = ChatGroq(model=llm_id)
    
    tools = [TavilySearchResults(max_results=3)] if allow_search else []
    
    agent = create_react_agent(
        model=llm,
        tools=tools,
        prompt=system_prompt
    )
    
    # ── MEMORY: build full message history ──
    messages = []
    for msg in chat_history:
        messages.append({"role": msg["role"], "content": msg["content"]})
    messages.append({"role": "user", "content": query})
    # ────────────────────────────────────────

    state = {"messages": messages}
    response = agent.invoke(state)
    
    return response["messages"][-1].content