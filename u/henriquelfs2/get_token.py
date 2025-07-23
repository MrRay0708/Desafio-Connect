import wmill
import json
import requests

def main():
    """
    Autentica na API da mostQI usando uma clientKey para obter um accessToken temporário.
    """
    api_url = "https://mostqiapi.com/user/authenticate"
    client_key = wmill.get_variable("u/henriquelfs2/api_key")

    payload = json.dumps({
    "token": client_key
    })
    headers = {
    'Content-Type': 'application/json'
    }

    try:
        response = requests.request("POST", api_url, headers=headers, data=payload, timeout=30)
        response.raise_for_status()
        
        # Extrai e retorna apenas o accessToken da resposta JSON
        token_data = response.json()
        return token_data.get("token")
        
    except Exception as e:
        return {"error": "Falha ao obter token", "details": str(e)}