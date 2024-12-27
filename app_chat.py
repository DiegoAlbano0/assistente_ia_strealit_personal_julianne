import streamlit as st
import pandas as pd
import psycopg2
from gemini_integration import ask_gemini

# Configuração da página
st.set_page_config(page_title="Chat com IA", layout="wide", page_icon="https://github.com/DiegoAlbano0/banco_img/blob/d333546714f9d00f6919c58de07703fb80691bd3/julianne_teste.png?raw=true")
st.image("https://github.com/DiegoAlbano0/banco_img/blob/d333546714f9d00f6919c58de07703fb80691bd3/julianne_teste.png?raw=true", width=200)

# Função para injetar CSS customizado
def inject_custom_css():
    st.markdown("""
    <style>
        .main, .stApp { background-color: #f7faf7; }
        .stApp, .stMarkdown, .stTextInput label, .stSelectbox label { color: black !important; }
        h1 { color: black !important; }
        .stFormSubmitButton button, .stButton > button { 
            background-color: #007bff; 
            color: white !important; 
            border: none; 
            border-radius: 5px; 
            padding: 8px 12px; 
            font-size: 16px; 
            cursor: pointer; 
        }
        .stFormSubmitButton button:hover, .stButton > button:hover { background-color: #0056b3; }
        .stMarkdown { font-size: 16px; }
    </style>
    """, unsafe_allow_html=True)
inject_custom_css()

# Inicializa o histórico no estado da sessão
if "messages" not in st.session_state:
    st.session_state.messages = []  # Lista para armazenar mensagens no formato {"role": "user/assistant", "content": "mensagem"}

# Título
st.title("Estratégia com IA")
st.write("---")

# Exibe o histórico da conversa no formato de chat
for message in st.session_state.messages:
    if message["role"] == "user":
        with st.chat_message("user"):
            st.markdown(message["content"])
    elif message["role"] == "assistant":
        with st.chat_message("assistant"):
            st.markdown(message["content"])

# Campo de entrada do usuário
user_input = st.chat_input("Digite sua pergunta ou mensagem:")

# Processa a mensagem ao enviar
if user_input:
    # Adiciona a mensagem do usuário ao histórico
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Obtém a resposta da IA
    with st.spinner("A IA está pensando..."):
        try:
            historico = "\n".join([f"{msg['role']}: {msg['content']}" for msg in st.session_state.messages])
            bot_response = ask_gemini(historico)
        except Exception as e:
            bot_response = f"Erro ao conectar com a IA: {e}"

    # Adiciona a resposta da IA ao histórico
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant", avatar="https://github.com/DiegoAlbano0/banco_img/blob/d333546714f9d00f6919c58de07703fb80691bd3/julianne_teste.png?raw=true"):
        st.markdown(bot_response)


