import sys

import pymysql
import rank_bm25
import snowballstemmer

from banco import conectar

print("Python:", sys.version)
print("PyMySQL:", pymysql.__version__)

conexao = conectar(com_banco=False)
with conexao.cursor() as cursor:
    cursor.execute("SELECT VERSION()")
    print("MySQL:", cursor.fetchone()[0])

    cursor.execute("SELECT 'informática' = 'informatica'")
    print("Teste de acentos:", cursor.fetchone()[0])

    cursor.execute("SHOW VARIABLES LIKE 'innodb_ft_min_token_size'")
    print(cursor.fetchone())

    cursor.execute("SHOW VARIABLES LIKE 'innodb_ft_enable_stopword'")
    print(cursor.fetchone())

    cursor.execute("SHOW GRANTS")
    for linha in cursor.fetchall():
        print("Permissão:", linha[0])
conexao.close()

radicalizador = snowballstemmer.stemmer("portuguese")
for palavra in ["costureiras", "costureiro", "costura"]:
    print(palavra, "->", radicalizador.stemWord(palavra))
