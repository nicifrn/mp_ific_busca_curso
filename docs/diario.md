# Diário

## Sprint 1 - 16/10 a 22/10
- Funcionou: Git, branch, .venv, MySQL 8.0.46 local, banco.py e verificar_ambiente.py rodando; a comparação ignorou acentos (resultado 1) e "costureiras" e "costureiro" deram o mesmo radical (costureir).
- Deu errado: o pymysql.__version__ mostrou 2.2.8, mas o pip show diz 1.2.3 (anotei a do pip show no ambiente.md).
- Aprendi: com innodb_ft_min_token_size = 3, palavras de 1 ou 2 letras (como "TI") não são indexadas; "costura" dá outro radical (costur), então a busca por radical não liga costura a costureira.

## Sprint 2 - 23/10 a 29/10
- Funcionou: criar_banco.py carregou 200 cursos e, rodado duas vezes, deu o mesmo número; a collation utf8mb4_0900_ai_ci ignorou o acento ("informatica" e "informática" deram o mesmo resultado); a Busca 1 achou "costura" também em ementas, não só nos títulos (7 cursos).
- Deu errado: a busca só acha a palavra exata, então "informática" voltou só 1 curso e "exel", "costureiras" e "faxina" não voltaram nenhum; a ordem é por nome, não por relevância.
- Aprendi: com LIKE, a ementa precisa ter as palavras que a pessoa digita; catálogo com 199 ementas do guia e 1 própria; collation utf8mb4_0900_ai_ci.

| Digite | O que você espera | O que aconteceu |
|---|---|---|
| informática | cursos de informática | 1 curso (FIC143): a palavra só aparece na ementa dele; Programador e Montador de Computadores não voltaram |
| informatica (sem acento) | os mesmos | os mesmos (FIC143): a collation ignora o acento |
| exel | cursos com Excel | 0 cursos: erro de digitação não é tratado |
| informática básica | cursos de informática básica | 0 cursos: só acha a frase exata |
| básica informática | os mesmos de cima | 0 cursos: a ordem das palavras importa |
| costureiras | cursos de costura | 0 cursos: não liga o plural/feminino a "costureiro" e "costura" |
| faxina | cursos de serviços domésticos ou de limpeza | 0 cursos: a palavra não aparece e o LIKE não conhece sinônimos |
