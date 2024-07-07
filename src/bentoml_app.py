import bentoml
import pandas as pd
from bentoml.io import NumpyNdarray, JSON
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

class Customer(BaseModel):
    Income: float = 53138
    Recency: int = 58
    NumWebVisitsMonth: int = 7
    Complain: int = 0
    age: int = 64
    total_purchases: int = 25
    enrollment_years: int = 10
    family_size: int = 1

@service.api(input=JSON(pydantic_model=Customer), output=NumpyNdarray())
def predict(data: Customer) -> np.array:
    df = pd.DataFrame([data.dict()])
    
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
    return np.array(result)

print('----- Processamento iniciado -------' )
# # Chamada para testar a função predict
result = predict(Customer())
print(result)