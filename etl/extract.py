import pandas as pd
import requests 
from config.settings import URL_API


def extrair_paises():
    # Extraindo os dados da API do IBGE
    url = URL_API
    resultado = requests.get(url)
    
    # Verificando se o status code retorna diferente de 200, se isso acontecer, retorna um erro na API
    if resultado.status_code != 200:
        raise Exception(f"Erro na API: {resultado.status_code}")
    
    # Colocando o resultado da extração em um json
    dados = resultado.json()

    # Criando um DataFrame
    df = pd.DataFrame(dados)
    return df

