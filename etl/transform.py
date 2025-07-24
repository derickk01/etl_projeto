import pandas as pd
import unicodedata
import re

def transform_name(nome):
    # Formatando o texto
    nome = unicodedata.normalize("NFD", nome)
    nome = ''.join(c for c in nome if unicodedata.category(c) != 'Mn')
    nome = nome.lower()

    # Tudo que não for letra minúscula ou número é colocado hífen
    nome = re.sub(r'[^a-z0-9]+', '-', nome)

    # Tirar hífen extra
    nome = nome.strip('-')

    # Retornando o nome formatado
    return nome


def transformar_dados(dados):
    # Transformando em um DataFrame
    df = pd.DataFrame(dados)

    # Verificando se o valor é um dicionário antes de tentar pegar o código do país 
    df['codigo_pais'] = df['id'].apply(lambda x: x.get('M49') if isinstance(x, dict) else None)
    
    df = df[['codigo_pais', 'nome']]

    # Renomeando para ficar mais simples de entender
    df = df.rename(columns={'nome': 'nome_pais'})

    # Colocando a função em prática para criar uma nova coluna com o nome formatado
    df['nome_transformado'] = df['nome_pais'].apply(transform_name)

    return df
