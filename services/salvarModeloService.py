import pickle
from services.vetorizacaoService import vetorizador, encode_Y
from services.treinamentoService import treinar_modelo
import os


#Salvar o vetorizador

def salvar_vetorizador():
    """
    Salva o vetorizador como arquivo no diretório 'model/'.
    """
    vetorizador_criado = vetorizador()

    caminho_arquivo = 'model/vetorizador_HealthIA.pkl'

    #Confere se o diretório 'model/' existe, se não, cria
    os.makedirs(os.path.dirname(caminho_arquivo), exist_ok=True)

    with open(caminho_arquivo, 'wb') as f:
        pickle.dump(vetorizador_criado, f)
        print("Vetorizador salvo com sucesso em", caminho_arquivo)

if __name__ == "__main__":
    salvar_vetorizador()

#Salvar o encoder

def salvar_encoder():
    """
    Salva o encoder como arquivo no diretório 'model/'.
    """
    encoderY_criado = encode_Y()

    #Salva o encoder em um arquivo .pkl
    caminho_arquivo = 'model/encoder_HealthIA.pkl'

    #Confere se o diretório 'model/' existe, se não, cria
    os.makedirs(os.path.dirname(caminho_arquivo), exist_ok=True)

    with open(caminho_arquivo, 'wb') as f:
        pickle.dump(encoderY_criado, f)
        print("Encoder salvo com sucesso em", caminho_arquivo)

#Salvar o modelo treinado

def salvar_modelo():
    """
    Salva o modelo treinado como arquivo no diretório 'model/'.

    Return:
    model: XGBClassifier
       O modelo treinado - que se chama HealthIA.
    """
    HealthIA = treinar_modelo()

    #salva o modelo em um arquivo .json
    caminho_arquivo = 'model/modelo_HealthIA.json'

    #Confere se o diretório 'model/' existe, se não, cria
    os.makedirs(os.path.dirname(caminho_arquivo), exist_ok=True)

    booster = HealthIA.get_booster()
    booster.save_model(caminho_arquivo)
    print("Modelo salvo com sucesso em", caminho_arquivo)
    

