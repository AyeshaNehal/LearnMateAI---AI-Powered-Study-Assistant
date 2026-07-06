# In this version of LearnMateAI,
# I will transform my basic AI chatbot into a complete web-based study assistant using Streamlit.
# The application will maintain conversation memory so the AI can remember previous messages and respond with context.
# The application will implement built-in commands such as /help, /history, /clear, /save, /stats using sidebar controls.

# To improve the overall user experience,
# the program will provide a chat interface similar to ChatGPT,
# include streaming responses, and automatically save chat history in a text file.

from groq import Groq
from dotenv import load_dotenv
import streamlit as st
import os


st.set_page_config(page_title="LearnMateAI", layout="wide")

st.markdown("""
<style>

/* Add spacing around the main page */
.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
    padding-left:3rem;
    padding-right:3rem;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="
background:rgba(255,255,255,.30);
backdrop-filter:blur(20px);
border-radius:20px;
padding:18px;
margin-bottom:25px;
text-align:center;
border:1px solid rgba(255,255,255,.35);
">

<h1 style="
font-size:48px;
font-weight:800;
color:#D63384;
margin-bottom:5px;
">
LearnMateAI
</h1>

<p style="
font-size:22px;
color:#555;
margin:0;
">
Your Personalized AI Learning Companion </p>

</div>
""", unsafe_allow_html=True)



st.markdown("""
<style>
.stApp {
    background: linear-gradient(to bottom right,
        #FF69B4,
        #CBC3E3,
        #E0F2FE);
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

html, body, [data-testid="stAppViewContainer"], .stApp {
    font-family: 'Poppins', sans-serif;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

/* Sidebar Background */
[data-testid="stSidebar"]{
    background: linear-gradient(
        to bottom,
        #FFE4F2,
        #F8E8FF,
        #EAF6FF
    );
}

/* Sidebar Buttons */
.stButton > button{
    width:100%;
    background:#F8C8DC;
    color:#5C2E4F;
    border:1px solid #E9AFC7;
    border-radius:8px;
    padding:12px;
    font-size:15px;
    font-weight:600;
    transition:0.3s;
}

.stButton > button:hover{
    background:#EC4899;
    color:white;
    transform:translateY(-2px);
    box-shadow:0px 6px 12px rgba(236,72,153,0.3);
}

</style>
""", unsafe_allow_html=True)

# ---------------- ENV SETUP ----------------
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

# ---------------- PAGE SETUP ----------------



# ---------------- SESSION STATE ----------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": (
                "You are LearnMateAI, a friendly AI study coach. "
                "Explain concepts clearly, use simple language, "
                "give examples, and encourage learning."
            )
        }
    ]

if "question_count" not in st.session_state:
    st.session_state.question_count = 0

if "response_count" not in st.session_state:
    st.session_state.response_count = 0


# ---------------- FUNCTIONS ----------------

def savetofile():
    with open("chathistory.txt", "w") as file:
        for message in st.session_state.messages:
            if message["role"] == "system":
                continue
            file.write(f"{message['role']}: {message['content']}\n")


def autosave():
    with open("chathistory.txt", "w") as file:
        for message in st.session_state.messages:
            if message["role"] == "system":
                continue
            file.write(f"{message['role']}: {message['content']}\n")


def show_stats():
    st.info(f"Questions Asked: {st.session_state.question_count}")
    st.info(f"AI Responses: {st.session_state.response_count}")
    st.info(f"Total Messages: {len(st.session_state.messages) - 1}")


def clear_chat():
    st.session_state.messages = [st.session_state.messages[0]]
    st.session_state.question_count = 0
    st.session_state.response_count = 0


def show_history():
    st.subheader("Chat History")
    for message in st.session_state.messages:
        if message["role"] != "system":
            st.write(f"{message['role']}: {message['content']}")


st.markdown("""
<style>

/* Buttons */
.stButton > button {
    width: 100%;
    background: #F8C8DC;
    color: #5C2E4F;
    border: 1px solid #E9AFC7;
    border-radius: 8px;
    padding: 14px 18px;
    font-size: 16px;
    font-weight: 600;
    transition: all 0.3s ease;
}

/* Hover Effect */
.stButton > button:hover {
    background: #EC4899;
    color: white;
    border: 1px solid #EC4899;
    transform: translateY(-2px);
    box-shadow: 0px 6px 15px rgba(236, 72, 153, 0.35);
}

</style>
""", unsafe_allow_html=True)


# ---------------- SIDEBAR COMMANDS ----------------

# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.markdown("""
    <div style="text-align:center;">

    <h1 style="
    color:#C2185B;
    margin-bottom:5px;
    ">
    LearnMateAI
    </h1>

    <p style="
    color:#7A5C61;
    font-size:16px;
    ">
    Your Personal AI Study Coach
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.markdown("### Conversation")

    if st.button("History", use_container_width=True):
        show_history()

    if st.button("Save Chat", use_container_width=True):
        savetofile()
        st.success("Chat saved successfully!")

    if st.button("Clear Chat", use_container_width=True):
        clear_chat()
        st.success("Chat cleared!")

    st.divider()

    st.markdown("### Information")

    if st.button("Help", use_container_width=True):
        st.info("""
Available Commands

• Save Chat
• Clear Chat
• View History
• View Statistics
""")

    if st.button("Statistics", use_container_width=True):
        show_stats()

    st.divider()

    st.markdown("### Session Statistics")

    st.metric(
        label="Questions Asked",
        value=st.session_state.question_count
    )

    st.metric(
        label="AI Responses",
        value=st.session_state.response_count
    )

    st.metric(
        label="Total Messages",
        value=len(st.session_state.messages) - 1
    )

    st.divider()

    st.markdown(
        """
        <div style="text-align:center; color:#7A5C61; font-size:14px;">
        <b>LearnMateAI </b><br>
        Created by Ayesha Nehal
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------------- CHAT DISPLAY ----------------

if len(st.session_state.messages) == 1:

    st.markdown("""
    <div style="
    background:rgba(255,255,255,.35);
    padding:25px;
    border-radius:20px;
    text-align:center;
    margin-bottom:20px;
    ">

    <h2 style="color:#D63384;">
    Welcome to LearnMateAI!
    </h2>

    <p>
    Have a question? Whether it's programming, mathematics, AI, or your university coursework, LearnMateAI is ready to help.
    </p>

    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<style>

/* Bottom area behind the input */
[data-testid="stBottom"]{
    background: linear-gradient(
        to bottom right,
        #FF69B4,
        #CBC3E3,
        #E0F2FE
    ) !important;
}

/* Some Streamlit versions use this container */
[data-testid="stBottomBlockContainer"]{
    background: linear-gradient(
        to bottom right,
        #FF69B4,
        #CBC3E3,
        #E0F2FE
    ) !important;
    padding-top:15px;
    padding-bottom:20px;
}

/* Chat input container */
[data-testid="stChatInput"]{
    background: rgba(255,255,255,0.35) !important;
    backdrop-filter: blur(15px);
    border: 2px solid rgba(255,255,255,.45);
    border-radius:20px;
    padding:10px;
    box-shadow:0px 8px 25px rgba(0,0,0,.15);
}

/* Text area */
[data-testid="stChatInput"] textarea{
    background: transparent !important;
    color:#4A2C40 !important;
    font-size:17px;
}

/* Placeholder */
[data-testid="stChatInput"] textarea::placeholder{
    color:#7A5C61 !important;
}

/* Send button */
[data-testid="stChatInput"] button{
    background:#EC4899 !important;
    color:white !important;
    border-radius:12px !important;
}

[data-testid="stChatInput"] button:hover{
    background:#D63384 !important;
}

</style>
""", unsafe_allow_html=True)



for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


st.markdown("""
<style>

/* User Messages */
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
    background:#FFE5F1;
    border-radius:18px;
    padding:10px;
    margin-bottom:15px;
}

/* Assistant Messages */
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) {
    background:rgba(255,255,255,.45);
    border-radius:18px;
    padding:10px;
    margin-bottom:15px;
}

</style>
""", unsafe_allow_html=True)


st.markdown("""
<style>

/* User message */
[data-testid="stChatMessage"]:nth-of-type(odd){
    background:#FFE5F2;
    border-radius:20px;
    padding:15px;
    margin-bottom:15px;
}

/* Assistant message */
[data-testid="stChatMessage"]:nth-of-type(even){
    background:rgba(255,255,255,.55);
    border-radius:20px;
    padding:15px;
    margin-bottom:15px;
}

</style>
""", unsafe_allow_html=True)


# ---------------- USER INPUT ----------------

user_question = st.chat_input("Ask your question...")

if user_question:

    if user_question.strip() == "":
        st.warning("Please enter a question.")
        st.stop()

    
    if user_question.lower() == "/clear":
        clear_chat()
        st.rerun()

    if user_question.lower() == "/stats":
        show_stats()
        st.stop()

    if user_question.lower() == "/history":
        show_history()
        st.stop()

   
    st.session_state.messages.append(
        {"role": "user", "content": user_question}
    )

    st.session_state.question_count += 1

    with st.chat_message("user"):
        st.markdown(user_question)

    
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=st.session_state.messages
            )

            ai_response = response.choices[0].message.content

            
            placeholder = st.empty()
            text = ""

            for word in ai_response.split():
                text += word + " "
                placeholder.markdown(text)

    st.session_state.response_count += 1

    st.session_state.messages.append(
        {"role": "assistant", "content": ai_response}
    )

    
    autosave()

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div style="
background:rgba(255,255,255,.30);
backdrop-filter:blur(10px);
padding:12px;
border-radius:15px;
text-align:center;
margin-top:25px;
">

<b>LearnMateAI v3.0</b><br>

Created by Ayesha Nehal • Built with Streamlit • Powered by Groq AI

</div>
""", unsafe_allow_html=True)



