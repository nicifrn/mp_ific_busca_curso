# Diário

## Sprint 1 - 16/10 a 22/10
- Funcionou: Git, branch, .venv, MySQL 8.0.46 local, banco.py e verificar_ambiente.py rodando; a comparação ignorou acentos (resultado 1) e "costureiras" e "costureiro" deram o mesmo radical (costureir).
- Deu errado: o pymysql.__version__ mostrou 2.2.8, mas o pip show diz 1.2.3 (anotei a do pip show no ambiente.md).
- Aprendi: com innodb_ft_min_token_size = 3, palavras de 1 ou 2 letras (como "TI") não são indexadas; "costura" dá outro radical (costur), então a busca por radical não liga costura a costureira.
