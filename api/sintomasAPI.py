from fastapi import APIRouter
from services.executarService import DiagnosticoIA




router = APIRouter()
diagnosticoIA = DiagnosticoIA(caminhoModelo='model')

@router.get('/')
async def raiz():
    return {"mensagem": "Bem vindo à API HealthIA"}

@router.get('/predict')
async def predict(sintomas: str):
    """
    Endpoint para predição de diagnóstico com base em sintomas fornecidos via query params.
    
    Paramêtros: 
    sintomas (str): Uma string contendo os sintomas separados por vírgulas.

    Retorna: 
    dict: Um dicionário contendo o diagnóstico previsto.
    """

    #Adicionar a lógica para carregar o modelo treinado e fazer a predição

    #Por enquanto, retornando um diagnóstico fictício
    sintomas_list = sintomas.split(',')

    #Simulação de predição
    diagnostico_previsto = diagnosticoIA.predict_simples(sintomas)

    return{
        "sintomas": sintomas_list,
        "diagnostico_previsto": diagnostico_previsto
        }