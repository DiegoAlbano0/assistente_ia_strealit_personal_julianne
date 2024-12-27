import customtkinter as ctk
import subprocess

# Criação das funcões de funcionalidades  
def validar_login():
    userario = entry_user.get()
    senha = entry_senha.get()

    #verificar se o user é diegoluz e a senha 1234
    if userario == 'diegoluz' and senha == '1234':
        app.destroy()
        subprocess.run(["streamlit", "run", "app_chat.py"])  # Substitua "app.py" pelo nome do seu arquivo
    else:
        label_erro.configure(text="Senha incorreta!")




# Criação da janela principal
app = ctk.CTk()
app.title('Login')
app.geometry('300x400')

# Criaçao dos campos
#Label
campo_user = ctk.CTkLabel(app,text='User')
campo_user.pack(pady=10)
#Entry
entry_user = ctk.CTkEntry(app,placeholder_text='Digite Aqui')
entry_user.pack(pady=10)

#Label
campo_senha = ctk.CTkLabel(app,text='Senha')
campo_senha.pack()
#Entry
entry_senha = ctk.CTkEntry(app,placeholder_text='Digite Aqui',show='*')
entry_senha.pack(pady=10)

#Button
botao_login = ctk.CTkButton(app,text='Login In',command=validar_login)
botao_login.pack(pady=10)


label_erro = ctk.CTkLabel(app,text='')
label_erro.pack(pady=10)

# Iniciar a aplicação
app.mainloop()

