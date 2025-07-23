import requests
import json

def main(cnh_frente_b64: str, token: str):
    """
    Recebe uma imagem em Base64, a envia para a API de Extração de
    Conteúdo através de um payload JSON, conforme a documentação.
    """
    # Busca a chave de API usando a função correta para variáveis
    api_key = token

    api_url = "https://mostqiapi.com/process-image/content-extraction"
    
    # O header agora especifica que estamos enviando dados no formato JSON
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # --- LÓGICA DE LIMPEZA DO BASE64 ---
    # Verifica se o prefixo (ex: "data:image/jpeg;base64,") está presente e o remove.
    if "," in cnh_frente_b64:
        base64_dados_puros = cnh_frente_b64.split(',')[1]
    else:
        base64_dados_puros = cnh_frente_b64

    
    # O corpo da requisição é um dicionário Python com a chave "fileBase64"
    payload = json.dumps({
        "fileBase64": base64_dados_puros,
        "returnCrops": True,  # Parâmetro opcional útil
        "returnMetadata": True
    })

    try:
        # Usamos o parâmetro 'json=payload' para enviar os dados em formato JSON
        response = requests.request("POST", api_url, headers=headers, data=payload, timeout=30)
        response.raise_for_status()
        
        return response.json()
        
    except requests.exceptions.HTTPError as e:
        return {"error": "Erro de API no script IDP", "status_code": e.response.status_code, "details": e.response.json()}
    except Exception as e:
        return {"error": "Erro geral no script IDP", "details": str(e)}