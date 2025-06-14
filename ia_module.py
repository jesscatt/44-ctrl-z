import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# Exemplo de IA simples que prevê pontuação com base em histórico
def prever_pontuacao(dados_historicos):
    if not dados_historicos:
        return 0
    df = pd.DataFrame(dados_historicos)
    X = df[['tentativas']].values
    y = df['pontuacao'].values

    modelo = LinearRegression()
    modelo.fit(X, y)

    nova_tentativa = np.array([[len(dados_historicos) + 1]])
    predicao = modelo.predict(nova_tentativa)
    return float(predicao[0])
