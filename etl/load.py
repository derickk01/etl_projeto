import pandas as pd

def carregar_dados(df, output):
    df.to_csv("output/paises.csv", index=False)
