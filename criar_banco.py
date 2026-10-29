import csv

from banco import conectar

CAMINHO_CSV = "dados/cursos.csv"


def criar_banco():
    conexao = conectar(com_banco=False)
    with conexao.cursor() as cursor:
        cursor.execute(
            "CREATE DATABASE IF NOT EXISTS ific_busca "
            "CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci"
        )
    conexao.close()


def criar_tabela(conexao):
    with conexao.cursor() as cursor:
        cursor.execute("DROP TABLE IF EXISTS cursos")
        cursor.execute(
            """
            CREATE TABLE cursos (
                id            INT AUTO_INCREMENT PRIMARY KEY,
                codigo        VARCHAR(20) NOT NULL UNIQUE,
                nome          VARCHAR(200) NOT NULL,
                eixo          VARCHAR(120) NOT NULL,
                carga_horaria INT NOT NULL,
                ementa        TEXT NOT NULL
            ) ENGINE=InnoDB
            """
        )


def ler_csv(caminho):
    tuplas = []
    with open(caminho, encoding="utf-8-sig", newline="") as arquivo:
        for linha in csv.DictReader(arquivo):
            tuplas.append(
                (
                    linha["codigo"].strip().replace(" ", "").upper(),
                    linha["nome"].strip(),
                    linha["eixo"].strip(),
                    int(linha["carga_horaria"]),
                    linha["ementa"].strip(),
                )
            )
    return tuplas


def main():
    criar_banco()
    conexao = conectar()
    criar_tabela(conexao)
    cursos = ler_csv(CAMINHO_CSV)
    with conexao.cursor() as cursor:
        cursor.executemany(
            "INSERT INTO cursos (codigo, nome, eixo, carga_horaria, ementa) "
            "VALUES (%s, %s, %s, %s, %s)",
            cursos,
        )
        conexao.commit()
        cursor.execute("SELECT COUNT(*) FROM cursos")
        total = cursor.fetchone()[0]
    conexao.close()
    print(total, "cursos carregados.")


if __name__ == "__main__":
    main()
