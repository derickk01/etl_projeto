Projeto ETL - Dados de países IBGE

Projeto simples em Python para extrair, transformar e carregar os dados utilizando a API de países do IBGE.

Estrutura do Projeto:

 etl/extract.py: busca os dados da API do IBGE.

 etl/transform.py: transforma e limpa os dados, criando colunas auxiliares.

 etl/load.py: salva os dados processados em arquivo CSV na pasta output/.

 main.py: controla a execução do pipeline ETL.

 output/: pasta onde o arquivo CSV gerado fica salvo.

 requirements.txt: lista das bibliotecas Python usadas.

Tecnologias usadas:
Python 3 
Pandas
Requests
