import pandas as pd

def carregar_dados(df):
    df.to_csv("output/paises.csv", index=False)
