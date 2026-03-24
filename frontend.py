from flask import Flask, render_template, request, jsonify
from ai_agent import get_response_from_ai

app = Flask(__name__)

ALLOWED_MODEL_NAMES = [
    "llama-3.3-70b-versatile",
    "qwen/qwen3-32b",
    "openai/gpt-oss-120b"
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()

    model_name    = data.get('model_name')
    system_prompt = data.get('system_prompt', '')
    messages      = data.get('messages', [])
    allow_search  = data.get('allow_research', False)
    chat_history  = data.get('chat_history', [])

    if model_name not in ALLOWED_MODEL_NAMES:
        return jsonify({"error": "Invalid model name."}), 400

    query = " ".join(messages)

    response = get_response_from_ai(
        llm_id=model_name,
        query=query,
        allow_search=allow_search,
        system_prompt=system_prompt,
        chat_history=chat_history
    )

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=7860, debug=False)