# Ambiente de execução

## Máquina
- Identificação: kelly-pc (notebook pessoal)
- Processador: AMD Ryzen 5 7520U with Radeon Graphics
- Memória RAM: 5,5 GiB
- Sistema operacional: Ubuntu 24.04.5 LTS

## Versões
- Python: 3.12.3
- MySQL: 8.0.46
- PyMySQL: 1.2.3 (pelo pip show; o pymysql.__version__ mostra 2.2.8)
- rank-bm25: 0.2.2
- snowballstemmer: 3.1.1
- matplotlib: 3.11.2
- numpy: 2.5.4
- pillow: 13.0.0
- kiwisolver: 1.5.1
- fonttools: 4.67.0
- contourpy: 1.4.0
- cycler: 0.12.1
- packaging: 26.3
- pyparsing: 3.3.3
- python-dateutil: 2.9.0.post0
- six: 1.17.0
- pip: 24.0

## Configuração do MySQL
- Teste de acentos ('informática' = 'informatica'): 1 (a comparação ignora acentos)
- innodb_ft_min_token_size: 3
- innodb_ft_enable_stopword: ON
- Charset da conexão: utf8mb4
- Collation do banco ific_busca e da tabela cursos: utf8mb4_0900_ai_ci (compara texto ignorando acentos e maiúsculas/minúsculas)
- Catálogo carregado: 200 cursos em 12 eixos (ementas: 199 do guia e 1 própria)

## Onde o MySQL roda
- O MySQL roda na mesma máquina que o Python (host localhost).
