import requests
import pandas as pd

# URL do endpoint da API Gemini
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"

# Chave da API
api_key = DB_key_gemini  # Substitua pela sua chave da Google API

def ask_gemini(historico):
    
    # Corpo da solicitação JSON
    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": f"Considere o seguinte histórico de conversa: {historico}."
                                 "Você é a mentora b.ju, especializada no mundo de acessórios e bijuterias, focada no estado do Piauí."   
                                 " Responda à última mensagem levando em conta o contexto."
                                 " Não inclua códigos na resposta, mas seja detalhado, amigável e criativo."
                    }
                ]
            }
        ]
    }

    # Parâmetros de consulta
    params = {
        "key": api_key
    }

    try:
        # Fazendo a chamada à API usando requests
        response = requests.post(url, params=params, json=data)

        # Verificando se a solicitação foi bem-sucedida
        if response.status_code == 200:
            # Imprime o JSON completo da resposta para depuração
            resposta_json = response.json()
            print("Resposta completa da API:", resposta_json)

            # Extrai o texto da resposta da API
            resposta = resposta_json.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "Sem resposta")
            return resposta
        else:
            return f"Erro ao chamar a API: {response.status_code} - {response.text}"

    except Exception as e:
        return f"Erro ao se comunicar com a API Gemini: {e}"
