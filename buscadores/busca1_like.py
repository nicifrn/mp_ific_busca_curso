from banco import conectar


def buscar(termo, limite=20):
    padrao = f"%{termo}%"
    conexao = conectar()
    with conexao.cursor() as cursor:
        cursor.execute(
            "SELECT codigo FROM cursos "
            "WHERE nome LIKE %s OR ementa LIKE %s "
            "ORDER BY nome, codigo "
            "LIMIT %s",
            (padrao, padrao, limite),
        )
        codigos = [linha[0] for linha in cursor.fetchall()]
    conexao.close()
    return codigos


if __name__ == "__main__":
    termo = input("Buscar: ")
    codigos = buscar(termo)
    print(len(codigos), "cursos:", codigos)
