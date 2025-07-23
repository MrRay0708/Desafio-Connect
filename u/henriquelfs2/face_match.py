import json
import requests

# Os inputs agora são duas strings em Base64, vindas dos resultados dos passos anteriores.
def main(rosto1_b64: str, rosto2_b64: str, token: str):
    """
    Recebe duas imagens de rosto em formato Base64 e as compara
    usando a API de FaceMatch 1:1.
    """
    api_key = token
    api_url = "https://mostqiapi.com/process-image/biometrics/face-compare" 
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # O payload da API espera receber as duas imagens em Base64
    payload = json.dumps({
        "faceFileBase64A": rosto1_b64,
        "faceFileBase64B": rosto2_b64
    })

    try:
        response = requests.request("POST", api_url, headers=headers, data=payload, timeout=30)
        response.raise_for_status()
        # Retorna o resultado da comparação (ex: score de similaridade)
        return response.json()
        
    except Exception as e:
        return {"error": "Erro no script FaceMatch", "details": str(e)}