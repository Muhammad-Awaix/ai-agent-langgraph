from pydantic import BaseModel
from fastapi import FastAPI
from typing import List
import uvicorn
from ai_agent import get_response_from_ai

app = FastAPI(title="LangGraph AI Agent")

ALLOWED_MODEL_NAMES = [
    "llama-3.3-70b-versatile",
    "qwen/qwen3-32b",
    "openai/gpt-oss-120b"
]

class Message(BaseModel):
    role: str
    content: str

class RequestState(BaseModel):
    model_name: str
    system_prompt: str
    messages: List[str]
    allow_research: bool
    chat_history: List[Message] = []  # ── NEW ──

@app.post('/chat')
def chat_endpoint(request: RequestState):
    
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error": "Invalid model name. Please select a valid model."}
    
    query = " ".join(request.messages)
    
    response = get_response_from_ai(
        llm_id=request.model_name,
        query=query,
        allow_search=request.allow_research,
        system_prompt=request.system_prompt,
        chat_history=[m.dict() for m in request.chat_history]  # ── NEW ──
    )
    
    return {"response": response}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)