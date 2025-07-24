import pandas as pd
from config.settings import caminho_output

# Função para carregar em um arquivo csv
def carregar_dados(df, output):
    df.to_csv(caminho_output, index=False)
