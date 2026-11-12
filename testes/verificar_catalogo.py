import csv
import re
from collections import Counter

from banco import conectar

MINIMO_CURSOS = 200

conexao = conectar()
with conexao.cursor() as cursor:
    cursor.execute(
        "SELECT COUNT(*), COUNT(DISTINCT codigo), COUNT(DISTINCT eixo) FROM cursos"
    )
    total, codigos_distintos, eixos = cursor.fetchone()
    cursor.execute("SELECT codigo, nome, carga_horaria, ementa FROM cursos")
    linhas = cursor.fetchall()
conexao.close()

assert total >= MINIMO_CURSOS, f"a tabela tem menos de {MINIMO_CURSOS} cursos"
assert total == codigos_distintos, "há código repetido"
assert all(
    re.fullmatch(r"FIC\d{3}", codigo) for codigo, _, _, _ in linhas
), "há código fora do formato FIC000"
assert all(
    ementa.strip() and horas > 0 for _, _, horas, ementa in linhas
), "há ementa vazia ou carga horária zerada"
assert eixos >= 8, "há menos de 8 eixos"
assert any(
    "ç" in nome or "ç" in ementa for _, nome, _, ementa in linhas
), "os acentos não chegaram inteiros"

print(f"Tudo certo: {total} cursos verificados.")

with open("dados/cursos.csv", encoding="utf-8-sig", newline="") as arquivo:
    origens = Counter(linha["origem_ementa"].strip() for linha in csv.DictReader(arquivo))
print(f"Ementas guia: {origens['guia']} | propria: {origens['propria']}")
