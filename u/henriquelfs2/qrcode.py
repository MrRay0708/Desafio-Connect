import requests
import json

def main(cnh_verso_b64: str, token: str):
    """
    Recebe a imagem do verso da CNH em Base64, a envia para a API VIO
    através de um payload JSON para extração do QR Code.
    """
    api_key = token

    if not api_key:
        raise ValueError("A variável u/henrique/api_key não foi encontrada ou está vazia.")

    api_url = "https://mostqiapi.com/process-image/vio-extraction"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # --- LÓGICA DE LIMPEZA DO BASE64 ---
    # Verifica se o prefixo (ex: "data:image/jpeg;base64,") está presente e o remove.
    if "," in cnh_verso_b64:
        base64_dados_puros = cnh_verso_b64.split(',')[1]
    else:
        base64_dados_puros = cnh_verso_b64
    
    payload = json.dumps({
        "fileBase64": base64_dados_puros
    })

    try:
        response = requests.request("POST", api_url, headers=headers, data=payload, timeout=30)
        response.raise_for_status()
        
        return response.json()
        
    except requests.exceptions.HTTPError as e:
        return {"error": "Erro de API no script VIO", "status_code": e.response.status_code, "details": e.response.json()}
    except Exception as e:
        return {"error": "Erro geral no script VIO", "details": str(e)}