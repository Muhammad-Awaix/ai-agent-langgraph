from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

def get_response_from_ai(llm_id, query, allow_search, system_prompt):
    
    llm = ChatGroq(model=llm_id)
    
    tools = [TavilySearch(max_results=3)] if allow_search else []
    
    agent = create_react_agent(
        model=llm,
        tools=tools,
        prompt=system_prompt
    )
    
    state = {"messages": [{"role": "user", "content": query}]}
    response = agent.invoke(state)
    
    return response["messages"][-1].content