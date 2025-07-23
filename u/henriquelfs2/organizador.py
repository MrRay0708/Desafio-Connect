def main(resultado_liveness: dict, resultado_facematch_1: dict, resultado_facematch_2: dict):
    """
    Recebe os resultados dos processos de Liveness e FaceMatch e os
    consolida em um único objeto JSON de resposta final.
    """
    
    # Extrai o score de cada comparação para facilitar o acesso
    score_comparacao_1 = resultado_facematch_1.get("result", {}).get("similarity")
    score_comparacao_2 = resultado_facematch_2.get("result", {}).get("similarity")
    status_liveness = resultado_liveness.get("livenessScore")

    # Você pode adicionar uma lógica para decidir o status final
    status_final = "REPROVADO"
    # Exemplo de lógica: precisa de sucesso no liveness e score > 80% em ambas as comparações
    if status_liveness == "1" and score_comparacao_1 > 0.8 and score_comparacao_2 > 0.8:
        status_final = "APROVADO"
        
    # Monta o objeto de retorno final
    resposta_final = {
        "status_geral_da_validacao": status_final,
        "verificacao_liveness": {
            "status": status_liveness,
            "score": resultado_liveness.get("result", {}).get("livenessScore")
        },
        "comparacao_cnh_vs_liveness": {
            "similaridade": score_comparacao_1
        },
        "comparacao_cnh_vs_qrcode": {
            "similaridade": score_comparacao_2
        },
        "detalhes_completos": {
            "liveness": resultado_liveness,
            "facematch1": resultado_facematch_1,
            "facematch2": resultado_facematch_2
        }
    }
    
    return resposta_final