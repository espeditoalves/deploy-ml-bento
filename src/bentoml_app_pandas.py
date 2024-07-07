import bentoml
import pandas as pd
from bentoml.io import NumpyNdarray, JSON, PandasDataFrame
import numpy as np
from pydantic import BaseModel
import pickle
  
def load_scaler():
    try:
        with open("processors/scaler.pkl", "rb") as s:
            scaler = pickle.load(s)
        print("Scaler carregado com sucesso.")
        return scaler  # Retorna o scaler carregado
    except FileNotFoundError:
        print("Arquivo não encontrado. Verifique o caminho do arquivo.")
        return None
    except Exception as e:
        print(f"Erro ao carregar scaler: {e}")
        return None

def load_pca():
    try:
        with open("processors/PCA.pkl", "rb") as p:
            pca = pickle.load(p)
        print("PCA carregado com sucesso.")
        return pca  # Retorna o PCA carregado
    except FileNotFoundError:
        print("Arquivo não encontrado. Verifique o caminho do arquivo.")
        return None
    except Exception as e:
        print(f"Erro ao carregar PCA: {e}")
        return None

# Carrega o modelo
model = bentoml.sklearn.get("customer_segmentation_kmeans:latest").to_runner()

# Cria um serviço com o modelo
service = bentoml.Service("customer_segmentation_kmeans", runners=[model])


@service.api(input=PandasDataFrame(), output=NumpyNdarray())
def predict(df: pd.DataFrame) -> np.ndarray:
# Carrega o Scaler e processa
    scaler = load_scaler()
    scaled_df = pd.DataFrame(scaler.transform(df), columns=df.columns)
    print(f"Shape scaled_df: {scaled_df.shape}")
    print('---'*10)

    # Carrega o PCA e processa
    pca = load_pca()
    pca_df = pd.DataFrame(pca.transform(scaled_df), columns=["col1", "col2", "col3"])
    print(f"Shape pca_df: {pca_df.shape}")
    print('---'*10)

    # Predição
    result = model.predict.run(pca_df)
    print(f'Classificação: {np.array(result)}')
    print('---'*10)
    return np.array(result)
