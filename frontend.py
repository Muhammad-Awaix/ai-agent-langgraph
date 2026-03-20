import streamlit as st
import requests

st.set_page_config(page_title="AI Agent", page_icon="◆", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@500;700&display=swap');
* { font-family: 'Syne', sans-serif; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem 2rem 1rem; }

.msg-user {
    background: #1a1a1a; color: #e0e0e0;
    border-radius: 16px 16px 4px 16px;
    padding: 12px 16px; margin: 6px 0 6px 40px;
    font-size: 15px; line-height: 1.6;
}
.msg-ai {
    background: #0f1f0f; color: #b8e0b8;
    border-radius: 16px 16px 16px 4px;
    padding: 12px 16px; margin: 6px 40px 6px 0;
    font-size: 15px; line-height: 1.7;
}
.lbl { font-size: 11px; color: #555; margin-bottom: 3px; letter-spacing:.06em; }
</style>
""", unsafe_allow_html=True)

# ── State ──────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

# ── Header ─────────────────────────────────────────────
st.markdown("## ◆ AI Agent")

# ── Settings ───────────────────────────────────────────
c1, c2 = st.columns([2, 1])
with c1:
    model = st.selectbox("Model", [
        "llama-3.3-70b-versatile",
        "qwen/qwen3-32b",
        "openai/gpt-oss-120b"
    ], label_visibility="collapsed")
with c2:
    search = st.toggle("Web Search", value=True)

system_prompt = st.text_input(
    "System Prompt",
    value="You are a smart and helpful AI assistant.",
    placeholder="System prompt..."
)

st.divider()

# ── Chat history ────────────────────────────────────────
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="lbl">You</div><div class="msg-user">{msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="lbl">◆ Agent</div><div class="msg-ai">{msg["content"]}</div>', unsafe_allow_html=True)

if not st.session_state.messages:
    st.markdown("<br><center style='color:#444;font-size:14px'>Send a message to start</center>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Input ───────────────────────────────────────────────
c1, c2, c3 = st.columns([5, 1, 1])
with c1:
    query = st.text_input("query", placeholder="Ask anything...", label_visibility="collapsed", key="q")
with c2:
    send = st.button("Send", use_container_width=True, type="primary")
with c3:
    if st.button("Clear", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# ── Send logic ──────────────────────────────────────────
if send and query.strip():
    st.session_state.messages.append({"role": "user", "content": query.strip()})

    with st.spinner("Thinking..."):
        try:
            res = requests.post("http://127.0.0.1:8000/chat", json={
                "model_name": model,
                "system_prompt": system_prompt,
                "messages": [query.strip()],
                "allow_research": search
            }, timeout=60)

            reply = res.json().get("response", "No response.") if res.status_code == 200 else f"Error {res.status_code}"

        except requests.exceptions.ConnectionError:
            reply = "Backend not running. Open a new terminal and run: `python main.py`"
        except Exception as e:
            reply = f"Error: {str(e)}"

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.rerun()