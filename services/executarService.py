import os
import joblib
import xgboost as xgb
import numpy as np
from services.datasetService import dataset_completo




#Classe com os métodos para executar o modelo treinado

class DiagnosticoIA:
    def __init__(self, caminhoModelo: str):
        self.caminhoModelo = caminhoModelo
        self.HealthIA = xgb.XGBClassifier()
        self.HealthIA.load_model(os.path.join(self.caminhoModelo, "modelo_HealthIA.json"))  
        self.vetorizadortfidf = joblib.load(os.path.join(self.caminhoModelo, "vetorizador_HealthIA.pkl"))
        self.encoderYPronto = joblib.load(os.path.join(self.caminhoModelo, "encoder_HealthIA.pkl"))

    def predict_simples(self, sintomas:  str):
        """
        Função para fazer a predição do diagnóstico com base nos sintomas fornecidos.
        """

        #Converter lista para string se necessario
        if isinstance(sintomas, list):
            sintomas_string = " ".join(sintomas)
        else:
            sintomas_string = sintomas

        #Vetorizar os sintomas usando o vetorizador carregado
        sintomas_vetorizados = self.vetorizadortfidf.transform([sintomas])

        #Fazer a predição usando o modelo carregado
        predicao = self.HealthIA.predict(sintomas_vetorizados)

        #Decodificar o rótulo previsto usando o encoder carregado
        pred_nome = self.encoderYPronto.classes_[int(predicao[0])] if hasattr(self.encoderYPronto, 'classes_') else str(predicao[0])

        LabelY = dataset_completo()["diagnostico"].astype(str).unique()

        label_pred = [LabelY[int(pred_nome[0])]]

        return label_pred
        