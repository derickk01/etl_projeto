from etl.extract import extrair_paises
from etl.transform import transformar_dados

if __name__ == "__main__":

    dados = extrair_paises()

    df = transformar_dados(dados)

    print(df.head())

