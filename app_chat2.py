import streamlit as st
from gemini_integration_espanhol import ask_gemini_espanhol
from gemini_integration_estrategia import ask_gemini_estrategia
from gemini_integration_ingles import ask_gemini_ingles

# Configuração da página
st.set_page_config(
    page_title="Chat com IA",
    layout="wide",
    page_icon="https://github.com/DiegoAlbano0/assistente_ia_strealit_personal_julianne/blob/main/julianne_teste.png?raw=true"
)

# Inicializa o estado de autenticação
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False

# Função de logout
def logout():
    st.session_state.autenticado = False
    st.session_state.username = ""
    st.session_state.senha = ""
    st.session_state.page = "login"

# Tela de login
if not st.session_state.autenticado:
    st.title("LOGIN")
    with st.form(key="login_form"):
        username = st.text_input("Usuário:", placeholder="Digite seu usuário")
        senha = st.text_input("Senha:", type="password", placeholder="Digite sua senha")
        submit_button = st.form_submit_button(label="Entrar")
    
    if submit_button:
        if username == "julianne" and senha == "Julianne$%1":  # Substitua pelos seus valores
            st.session_state.autenticado = True
            st.session_state.username = username
            st.session_state.senha = senha
            st.success("Login bem-sucedido! Carregando o aplicativo...")
            st.session_state.page = "main"
        else:
            st.error("Usuário ou senha incorretos. Tente novamente.")
else:
    # App principal após autenticação
    if st.session_state.page == "main":
        st.sidebar.title("Navegação")
        aba = st.sidebar.radio("Escolha uma aba:", ["I.A. - Estratégia", "I.A. - Inglês", "I.A. - Espanhol"])
        with st.sidebar:
            if st.button("Sair"):
                logout()

        # Inicializa o histórico no estado da sessão para cada aba
        if "messages_estrategia" not in st.session_state:
            st.session_state.messages_estrategia = []
        if "messages_ingles" not in st.session_state:
            st.session_state.messages_ingles = []
        if "messages_espanhol" not in st.session_state:
            st.session_state.messages_espanhol = []

        # Seleciona o histórico e função da IA de acordo com a aba
        if aba == "I.A. - Estratégia":
            messages = st.session_state.messages_estrategia
            ask_gemini = ask_gemini_estrategia
            st.image("https://github.com/DiegoAlbano0/assistente_ia_strealit_personal_julianne/blob/main/julianne_teste.png?raw=true", width=200)
            st.title("Estratégia com IA")
            st.write("Converse sobre estratégias e planejamento.")
        elif aba == "I.A. - Inglês":
            messages = st.session_state.messages_ingles
            ask_gemini = ask_gemini_ingles
            st.title("Pratique seu Inglês com IA")
            st.write("Melhore suas habilidades de inglês.")
        elif aba == "I.A. - Espanhol":
            messages = st.session_state.messages_espanhol
            ask_gemini = ask_gemini_espanhol
            st.title("Pratique seu Espanhol com IA")
            st.write("Aprimore suas habilidades de espanhol.")

        # Função para injetar CSS customizado
        def inject_custom_css():
            st.markdown("""
            <style>
                .main, .stApp { background-color: #f7faf7; }
                .stApp, .stMarkdown, .stTextInput label, .stSelectbox label { color: black !important; }
                h1 { color: black !important; }
                .stFormSubmitButton button, .stButton > button { 
                    background-color: #ff0000; 
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

        # Exibe o histórico da conversa no formato de chat
        for message in messages:
            if message["role"] == "user":
                with st.chat_message("user"):
                    st.markdown(message["content"])
            elif message["role"] == "assistant":
                with st.chat_message("assistant"):
                    st.markdown(message["content"])

        # Campo de entrada do usuário
        user_input = st.chat_input("Digite sua pergunta ou mensagem:")

        if user_input:
            # Adiciona a mensagem do usuário ao histórico da aba atual
            messages.append({"role": "user", "content": user_input})
            with st.chat_message("user"):
                st.markdown(user_input)

            # Obtém a resposta da IA
            with st.spinner("A IA está pensando..."):
                try:
                    historico = "\n".join([f"{msg['role']}: {msg['content']}" for msg in messages])
                    bot_response = ask_gemini(historico)
                except Exception as e:
                    bot_response = f"Erro ao conectar com a IA: {e}"

            # Adiciona a resposta da IA ao histórico da aba atual
            messages.append({"role": "assistant", "content": bot_response})
            with st.chat_message("assistant", avatar="https://github.com/DiegoAlbano0/assistente_ia_strealit_personal_julianne/blob/main/julianne_teste.png?raw=true"):
                st.markdown(bot_response)
