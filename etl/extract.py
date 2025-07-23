import pandas as pd
import requests 

def extrair_paises():
    url = 'https://servicodados.ibge.gov.br/api/v1/localidades/paises' 
    resultado = requests.get(url)
    if resultado.status_code != 200:
        raise Exception(f"Erro na API: {resultado.status_code}")
    dados = resultado.json()
    df = pd.DataFrame(dados)
    return df

if __name__ == "__main__":
    df = extrair_paises()
    print(df.head())