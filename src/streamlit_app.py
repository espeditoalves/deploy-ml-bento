import json
import math

import requests
import streamlit as st

import bentoml
import pandas as pd
from bentoml.io import NumpyNdarray, JSON, PandasDataFrame
import numpy as np
from pydantic import BaseModel
import pickle

from bentoml_app_pandas import load_pca, load_scaler

# Carrega o modelo
model = bentoml.sklearn.get("customer_segmentation_kmeans:latest").to_runner()
model.init_local()

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


st.title("Web App de Segmentação de Clientes")

# ---------------------------------------------------------------------------- #
# Recebe inputs do usuário
data = {}

data["Income"] = st.number_input(
    "Income",
    min_value=0,
    step=500,
    value=58138,
    help="Renda doméstica anual do cliente",
)
data["Recency"] = st.number_input(
    "Recency",
    min_value=0,
    value=58,
    help="Quantidade de dias desde a última compra do cliente",
)
data["NumWebVisitsMonth"] = st.number_input(
    "NumWebVisitsMonth",
    min_value=0,
    value=7,
    help="Quantidade de visitas ao site da empresa no último mês",
)
data["Complain"] = st.number_input(
    "Complain",
    min_value=0,
    value=7,
    help="1 se o cliente reclamou nos últimos 2 anos, 0 caso contrário",
)
data["age"] = st.number_input(
    "age",
    min_value=0,
    value=64,
    help="Idade do cliente",
)
data["total_purchases"] = st.number_input(
    "total_purchases",
    min_value=0,
    value=25,
    help="Quantidade total de compras através do site, catálogo ou loja",
)
data["enrollment_years"] = st.number_input(
    "enrollment_years",
    min_value=0,
    value=10,
    help="Quantidade de anos que o cliente manteve laços com a empresa",
)
data["family_size"] = st.number_input(
    "family_size",
    min_value=0,
    value=1,
    help="Quantidade de pessoas na família do cliente",
)

# Realiza a predição
if st.button("Prever a categoria desse cliente"):
    if not any(math.isnan(v) for v in data.values()):
        # Converte os dados de entrada para um DataFrame
        input_df = pd.DataFrame([data])

        # Realiza a previsão
        prediction = predict(input_df)[0]
        st.write(f"Esse cliente pertence à categoria {prediction}")