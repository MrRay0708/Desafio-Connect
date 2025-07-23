import requests
import json

def main(token: str):
    """
    Cria uma nova sessão de Liveness Streaming na API da mostQI,
    com o payload corrigido para evitar o erro 'Bad Request'.
    """
    
    api_url = "https://mostqiapi.com/liveness/streaming/async"
    temp_token = token

    if not temp_token:
        raise ValueError("Token temporário não foi fornecido.")

    headers = {"Authorization": f"Bearer {temp_token}", "Content-Type": "application/json"}

    # O dicionário Python que será convertido para JSON
    payload_dict = {
        "uiCustomization": {
            "defaultLanguage": "pt-BR",
            "theme": "dark",
            "primaryColor": "#820AD1",
            "hideTopbar": True,
            "welcomeMessage": {
                # Corrigido para "pt-BR" para corresponder ao padrão
                "pt-BR": "Bem-vindo à Certificação de Imagem!",
                "en": "Welcome to Image Verification!",
                "es": "¡Bienvenido a la Certificación de Imagen!",
                "fr": "Bienvenue sur la certification d'images !"
            },
            "successMessage": {
                # Corrigido para "pt-BR"
                "pt-BR": "Vivacidade confirmada!",
                "en": "Success: Liveness confirmed!",
                "es": "Éxito: ¡Vivacidad confirmada!",
                "fr": "Vivacité confirmée !"
            },
            "failureMessage": {
                # Corrigido para "pt-BR"
                "pt-BR": "Não foi possível comprovar a vivacidade.",
                "en": "Error: Unable to confirm liveness.",
                "es": "Error: No fue posible comprobar la vivacidad.",
                "fr": "Erreur : Impossible de confirmer la vivacité."
            }
        }
    }

    try:
        # Forma mais segura de enviar JSON com a biblioteca requests.
        # Ela automaticamente converte o dicionário e define o Content-Type.
        response = requests.post(api_url, headers=headers, json=payload_dict, timeout=30)
        response.raise_for_status()

        return response.json()

    except requests.exceptions.HTTPError as e:
        # Retorna o erro exato da API para facilitar a depuração
        return {"error": "Erro de API na criação da sessão Liveness", "status_code": e.response.status_code, "details": e.response.json()}
    except Exception as e:
        return {"error": "Erro geral no script", "details": str(e)}