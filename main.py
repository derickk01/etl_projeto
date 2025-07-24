from etl.extract import extrair_paises
from etl.transform import transformar_dados
from etl.load import carregar_dados
if __name__ == "__main__":
    # Extraindo
    df_extract = extrair_paises()

    # Transformando
    df_transform = transformar_dados(df_extract)
    
    #Carregando
    carregar_dados(df_transform, "output/paises.csv")
    

