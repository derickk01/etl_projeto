import pandas as pd
import unicodedata
import re

def transform_name(nome):
    # Tirar acentos
    nome = unicodedata.normalize("NFD", nome)
    nome = ''.join(c for c in nome if unicodedata.category(c) != 'Mn')
    nome = nome.lower()

    nome = re.sub(r'[^a-z0-9]+', '-', nome)

    nome = nome.strip('-')

    return nome

def transformar_dados(dados):
    df = pd.DataFrame(dados)

    df['codigo_pais'] = df['id'].apply(lambda x: x.get('M49') if isinstance(x, dict) else None)
    
    df = df[['codigo_pais', 'nome']]

    
    df = df.rename(columns={'nome': 'nome_pais'})

    df['nome_transformado'] = df['nome_pais'].apply(transform_name)

    return df
