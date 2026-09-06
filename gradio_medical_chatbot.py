import gradio as gr
from app import rag_chain
import time

def chatbot(user_message, history):
    history = history or []
    user_msg = f"🧑 {user_message}"
    typing_indicator = "🤖 <span class='typing-dots'></span>"
    history.append((user_msg, typing_indicator))
    time.sleep(0.5)
    try:
        answer = rag_chain.invoke(user_message)
    except Exception as e:
        answer = f"⚠️ Error: {e}"
    history[-1] = (user_msg, f"🤖 {answer}")
    return history, history


with gr.Blocks(css="""
@import url('https://fonts.googleapis.com/css2?family=Lora:wght@400;700&family=Merriweather:wght@400;700&display=swap');

body {
    margin:0; padding:0;
    font-family:'Lora','Merriweather',serif;
    background: linear-gradient(135deg, #16222a, #3a6073);
    background-size: 400% 400%;
    animation: gradientShift 20s ease infinite;
    display:flex; justify-content:center; align-items:center;
    min-height:100vh;
    color:#f6f7fb;
}

@keyframes gradientShift {
  0% {background-position: 0% 50%;}
  50% {background-position: 100% 50%;}
  100% {background-position: 0% 50%;}
}

#main-container {
    width:100%;
    max-width:1100px;
    display:flex;
    flex-direction:column;
    align-items:center;
    padding:25px;
    box-sizing:border-box;
}

/* HEADER */
#header {
    text-align:center;
    margin-bottom:25px;
}
#header h1 {
    font-size:42px;
    font-weight:700;
    background: linear-gradient(90deg, #00e0b8, #7fffd4);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    text-shadow: 0 0 18px rgba(0,255,200,0.45);
    margin:0;
}
#header p {
    font-size:18px;
    color:#94a3b8;
    margin-top:6px;
    opacity:0.85;
}

/* CHAT LAYOUT */
#chat-container {
    display:flex;
    gap:25px;
    width:100%;
    flex-wrap: wrap;
    align-items:flex-start;
    justify-content:center;
}

/* CHAT PANEL */
#chat-panel {
    flex:3;
    display:flex;
    flex-direction:column;
    background:#1e2a35;
    border:1px solid rgba(255,255,255,0.12);
    border-radius:25px;
    padding:20px;
    box-shadow:0 10px 25px rgba(0,0,0,0.4);
}

/* CHATBOX */
#chatbot {
    height:600px;
    overflow-y:auto;
    padding:20px;
    border-radius:20px;
    background:#243543;
    margin-bottom:20px;
    color:#f6f7fb;
}

/* SCROLLBAR */
#chatbot::-webkit-scrollbar { width:8px; }
#chatbot::-webkit-scrollbar-thumb {
    background:#00e0b8;
    border-radius:10px;
}

/* MESSAGES */
.chatbot-message {
    font-size:17px;
    line-height:1.6;
    padding:14px 18px;
    border-radius:18px;
    margin-bottom:14px;
    word-wrap:break-word;
    animation: fadeInUp 0.4s forwards;
}
.user-message {
    background: linear-gradient(135deg, #00e0b8, #007f7f);
    color:#001219;
    max-width:75%;
    margin-left:auto;
    box-shadow:0 3px 10px rgba(0,255,200,0.25);
}
.bot-message {
    background:#324a5f;
    border-left:4px solid #00e0b8;
    max-width:75%;
    margin-right:auto;
    box-shadow:0 3px 10px rgba(0,0,0,0.3);
}

/* INPUT */
#user-input-container {
    display:flex;
    gap:10px;
}
#user-textbox {
    flex-grow:1;
    border:none;
    outline:none;
    border-radius:20px;
    padding:14px 18px;
    font-size:17px;
    background:#2d3d4d;
    color:#f6f7fb;
    box-shadow:inset 0 0 8px rgba(0,0,0,0.2);
}
#user-textbox:focus {
    background:#364d5e;
    box-shadow:0 0 8px rgba(0,255,200,0.3);
}
#send-btn {
    background:linear-gradient(135deg, #00e0b8, #7fffd4);
    color:#001219;
    border:none;
    border-radius:20px;
    padding:12px 22px;
    font-size:17px;
    font-weight:600;
    cursor:pointer;
    box-shadow:0 0 12px rgba(0,255,200,0.4);
    transition:all 0.3s ease;
}
#send-btn:hover {
    transform:scale(1.07);
    box-shadow:0 0 20px rgba(0,255,200,0.7);
}

/* TIPS BOX */
#tips-box {
    flex:1;
    min-width:300px;
    background:rgba(36,53,67,0.85);
    border:1px solid rgba(255,255,255,0.1);
    border-radius:25px;
    padding:25px;
    box-shadow:0 8px 20px rgba(0,0,0,0.3);
    color:#f6f7fb;
}
#tips-box h3 {
    color:#00e0b8;
    font-size:22px;
    margin-top:0;
}
#tips-box ul {
    list-style-type:'💡 ';
    padding-left:10px;
    margin-top:10px;
}
#tips-box li {
    margin-bottom:8px;
    color:#f1f3f5;
}
#tips-box p {
    margin-top:15px;
    font-style:italic;
    color:#b6c9d6;
}

/* ANIMATIONS */
@keyframes fadeInUp {
  0% {opacity:0; transform:translateY(20px);}
  100% {opacity:1; transform:translateY(0);}
}
.typing-dots::before, .typing-dots::after {
  content:''; display:inline-block; width:6px; height:6px;
  margin:0 2px; background:#00e0b8; border-radius:50%;
}
.typing-dots::after {animation:bounce 1s infinite;}
.typing-dots::before {animation:bounce 1s 0.3s infinite;}
@keyframes bounce {0%,80%,100%{transform:scale(0);}40%{transform:scale(1);}}
""") as demo:

    with gr.Column(elem_id="main-container"):
        gr.Markdown("""<div id="header">
            <h1>🩺 AI Medical Chatbot</h1>
            <p>Your modern healthcare assistant — smart, clean, and precise.</p>
        </div>""")

        with gr.Row(elem_id="chat-container"):
            with gr.Column(scale=3, elem_id="chat-panel"):
                chatbot_ui = gr.Chatbot(label="", elem_id="chatbot")
                with gr.Row(elem_id="user-input-container"):
                    user_input = gr.Textbox(label="", placeholder="Ask your medical question here...", elem_id="user-textbox")
                    send_btn = gr.Button("Send", elem_id="send-btn")

            gr.Markdown("""
            <div id="tips-box">
                <h3>💡 Quick Tips</h3>
                <ul>
                    <li>Describe symptoms clearly.</li>
                    <li>Include age and gender if relevant.</li>
                    <li>Ask one question at a time.</li>
                    <li>Consult a doctor for serious issues.</li>
                </ul>
                <p>⚙️ Powered by RAG + LangChain medical intelligence.</p>
            </div>
            """)

    user_input.submit(chatbot, [user_input, chatbot_ui], [chatbot_ui, chatbot_ui])
    send_btn.click(chatbot, [user_input, chatbot_ui], [chatbot_ui, chatbot_ui])

demo.launch(share=True)
