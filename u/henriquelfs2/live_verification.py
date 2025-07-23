import requests
import json


def main(session_id: str, token: str):
    """
    Cria uma nova sessão de Liveness Streaming na API da mostQI.
    Retorna o sessionToken para a UI e o sessionId para verificação posterior.
    """
    api_url = "https://mostqiapi.com/liveness/streaming/async/status"

    api_key = token

    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    payload = json.dumps({
   "processId": session_id
    })

    try:
        response = requests.request("POST", api_url, headers=headers, data=payload, timeout=10)
        response.raise_for_status()
        data = response.json()

        #status_do_processo = data.get("result", {}).get("status")

        return data

    except requests.exceptions.RequestException as err:
        return {"error": "Request Error on Liveness Check", "details": str(err)}
