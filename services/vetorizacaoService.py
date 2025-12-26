#1 - Chamar o famework que tem o TF-IDF - ok
#2 - Instanciar o modelo de vetorização - ok
#3 - Pegar os dados e vetorizar - ok

from sklearn.feature_extraction.text import TfidfVectorizer
from services.datasetService import dataset_completo
from sklearn.preprocessing import LabelEncoder

#Vetorizador 
def vetorizador():
    """
    Função que cria o vetorizador TF-IDF e o ajusta aos dados de entrada.
    
    Returns:
        Vetorizador ajustado com os dados pronto para ser usado.
    """
    tfidf = TfidfVectorizer()
    
    df = dataset_completo()
    X = df["sintomas"].astype(str)

    tfidf.fit(X)

    return tfidf

#Vetorizador vetorizando os dados
#Retorno dados vetorizados
def vetorizacao():    
    tfidf = vetorizador()

    df = dataset_completo()
    X = df["sintomas"].astype(str)

    tfidf.fit(X)

    X_tfidf = tfidf.transform(X)

    return X_tfidf

def encode_Y():
    """
    Função para codificar as labels de diagnóstico em valores numéricos.

    Return:
        Array de labels codificados numericamente.
    """
    label_encoder = LabelEncoder()
    df = dataset_completo()

    Y = df["diagnostico"].astype(str)

    Y_encoded = label_encoder.fit_transform(Y)
    return Y_encoded


