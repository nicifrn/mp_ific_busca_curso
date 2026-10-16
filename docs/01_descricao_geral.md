# Plano de trabalho - Busca de cursos no iFIC: busca textual do MySQL e camada de busca em Python

**Estudante:** Kelly (@Kcallvs) - Tecnologia em Sistemas para Internet

**Orientadores:** Prof. Bruno Gomes (@brunogomesifrn) e Entony (@franciscoentony) - NIC/IFRN

**Repositório:** https://github.com/nicifrn/mp_ific_busca_curso

**Período:** 16/10/2026 a 10/12/2026: 8 sprints de 1 semana (de sexta a quinta-feira)

**Projeto pai:** iFIC, plataforma de gestão e divulgação dos Cursos de Formação Inicial e Continuada (FIC) do IFRN (resumo em [`docs/projeto_ific.md`](projeto_ific.md)).

**Trabalho escrito:** um **artigo**, escrito no **modelo de TCC do IFRN**, seguindo as normas de [`docs/orientacoes_escrita_tcc.md`](orientacoes_escrita_tcc.md).

> **Leia este documento inteiro antes de começar a Sprint 1.** Ele é a referência completa do seu trabalho: tudo o que você vai programar, pesquisar e escrever está aqui, sprint por sprint. As *issues* do GitHub são o resumo de cada semana e sempre apontam para a seção correspondente deste documento. Se uma *issue* e este documento parecerem dizer coisas diferentes, **vale este documento**.

---

## Sumário

- [1. Como usar este documento e o quadro de tarefas](#como-usar)
- [2. A ideia do trabalho](#ideia)
- [3. Decisões já tomadas](#decisoes)
- [4. Cronograma](#cronograma)
- [5. Como trabalhar no repositório (fluxo do NIC)](#fluxo-git)
- [6. A estrutura de pastas que você vai construir](#estrutura)
- [7. Combinados que valem para todas as sprints](#combinados)
- [8. Como escrever o artigo](#escrita-geral)
- [Sprint 1 - Ambiente e conexão com o MySQL](#sprint-1-dev)
- [Sprint 2 - O catálogo de cursos e a Busca 1](#sprint-2-dev)
- [Sprint 3 - A coleção de teste e o script de avaliação](#sprint-3-dev)
- [Sprint 4 - Busca 2: o FULLTEXT do MySQL](#sprint-4-dev)
- [Sprint 5 - Busca 3: índice invertido, radical das palavras e BM25](#sprint-5-dev)
- [Sprint 6 - Busca 3: erro de digitação e sinônimos](#sprint-6-dev)
- [Sprint 7 - Rodada oficial, tempo, espaço, gráficos e análise de erros](#sprint-7-dev)
- [Sprint 8 - Página web, README e fechamento](#sprint-8-dev)
- [9. Quadro-resumo](#quadro-resumo)
- [10. Riscos e planos B](#riscos)
- [11. Se sobrar tempo](#extras)
- [12. Referências mínimas do artigo](#referencias-minimas)

---

<a id="como-usar"></a>
## 1. Como usar este documento e o quadro de tarefas

### As *issues* e o quadro (kanban)

Eu cadastrei as suas tarefas como *issues* no repositório. Toda semana tem:

- **uma *issue* com a etiqueta `Desenvolvimento`**: o que você vai programar e medir;
- **uma *issue* com a etiqueta `Escrita`**: o que você vai pesquisar e escrever no artigo. Em seis semanas ela é a entrega de uma parte do texto. Em duas semanas (Sprints 1 e 6) não há entrega de seção nova, e a *issue* é uma tarefa menor: na Sprint 1, preparar o documento e fichar as leituras; na Sprint 6, colocar no documento as tabelas com as notas que você já mediu. Essas tarefas pequenas existem para o texto não ficar parado, porque **quem deixa os Resultados para o fim não entrega**.

As *issues* de uma semana estão agrupadas em um **marco** (*milestone*) com o nome e a data da sprint, por exemplo `Sprint 04 - Busca 2 com FULLTEXT (06/11 a 12/11)`. A página **Milestones** do repositório mostra quanto de cada sprint já foi concluído.

O **quadro do projeto** (aba *Projects* do repositório) tem quatro colunas:

| Coluna | Quando o card fica aqui |
|---|---|
| **A fazer** | a tarefa ainda não começou |
| **Em andamento** | você está trabalhando nela. **Mova o card assim que começar** |
| **Em revisão** | você terminou e avisou os orientadores |
| **Concluído** | os orientadores aprovaram e fecharam a *issue* |

### Como cada sprint está organizada neste documento

Cada sprint tem duas partes, **Desenvolvimento** e **Escrita**, e cada uma tem um endereço próprio (`#sprint-4-dev`, `#sprint-4-escrita`), que é para onde as *issues* apontam.

A parte de desenvolvimento tem sempre os mesmos blocos:

- **O que você vai entregar**: em uma frase, o que precisa estar funcionando no fim da semana;
- **Passo a passo**: a lista numerada do que fazer, na ordem. Siga na ordem, sem pular;
- **Como saber que deu certo**: o que você deve ver na tela ou no arquivo. Se não vir isso, ainda não terminou;
- **Entrega da sprint**: a lista de conferência que também está na *issue*.

**Neste documento eu não te dou os programas prontos.** Você já sabe Python, então eu te digo o que cada programa precisa fazer, em que ordem, quais funções e bibliotecas usar e o que pesquisar. Quem escreve o código é você, e é isso que faz o trabalho ser seu. Os comandos **SQL** aparecem completos, porque são o objeto de estudo e você vai explicá-los no artigo; os trechos de **Python** são **peças** (uma assinatura de função, uma chamada de biblioteca, um esqueleto com comentários), não a solução montada.

### Como entregar

**Desenvolvimento:**

1. abra um *pull request* (PR) da sua *branch* para a `develop`, seguindo a [seção 5](#fluxo-git), com `Closes #N` na descrição (o número N de cada sprint está indicado na própria sprint);
2. comente na *issue*: `@brunogomesifrn @franciscoentony entrega da Sprint N pronta para revisão - PR #X`;
3. mova o card para **Em revisão**.

Quando um de nós aprovar e fizer o *merge* do PR, a *issue* fecha sozinha e o card vai para **Concluído**. Se pedirmos ajustes, faça os ajustes na mesma *branch* (o PR se atualiza sozinho) e comente de novo.

**Escrita:**

1. escreva no documento do Google Drive (veja a [seção 8](#escrita-geral));
2. nomeie a versão no histórico do Drive (*Arquivo → Histórico de versões → Nomear versão atual*), por exemplo `Entrega 1 - Introdução - 29/10`;
3. comente na *issue*: `@brunogomesifrn @franciscoentony Introdução pronta para revisão - versão "Entrega 1 - Introdução - 29/10"`;
4. mova o card para **Em revisão**.

Nós comentamos no próprio documento do Drive. Quando a seção estiver aprovada, fechamos a *issue*.

### Regras de ouro

- **Entregue no prazo, mesmo incompleto.** Trabalho pela metade dá para revisar; trabalho que não chega, não. Na *issue*, diga o que ficou faltando.
- **Terminou antes? Não comece a próxima sprint.** Use o tempo para entender melhor o que fez e para adiantar a escrita.
- **Travou mais de 40 minutos no mesmo erro? Pare e peça ajuda.** Comente na *issue* da semana, marcando nós dois, com: o que você estava tentando fazer, o comando que rodou e **a mensagem de erro inteira, copiada e colada** (não um resumo, nem um print cortado). Pedir ajuda depois de 40 minutos não é desistir, é administrar o tempo.

---

<a id="ideia"></a>
## 2. A ideia do trabalho

O iFIC vai reunir em um só lugar os cursos FIC do IFRN. São centenas de cursos, de eixos muito diferentes (informática, alimentos, construção civil, beleza, gestão), procurados por um público amplo, com escolaridade e familiaridade digital variadas, muitas vezes pelo celular. Para esse público, **a caixa de busca é a porta de entrada**: um curso que existe mas não é encontrado é, para quem procura, um curso que não existe.

Quando alguém começa a programar essa busca, a saída natural é escrever `WHERE nome LIKE '%termo%'` (no Django, que é o que a plataforma usa, isso se escreve `icontains`). Funciona na demonstração. O problema aparece com gente de verdade digitando: "exel" não encontra Excel, "costureiras" não encontra o curso de Costureiro, "faxina" não encontra Serviços domésticos, e "básica informática" não encontra "Informática básica".

A pergunta que o seu trabalho responde é:

> **Para o catálogo de cursos FIC, o que se ganha, e a que custo, ao trocar a busca simples do banco pela busca textual do próprio MySQL ou por uma camada de busca dedicada?**

Para responder, você vai comparar **três formas de buscar um curso**, sobre o **mesmo catálogo**, com as **mesmas consultas**, no **mesmo computador**, todas lendo os dados do **MySQL**, que é o banco do iFIC:

| Nome | O que é | Onde a busca acontece |
|---|---|---|
| **Busca 1** | `LIKE '%termo%'` em SQL: o jeito mais simples e mais comum | dentro do MySQL, sem índice de texto |
| **Busca 2** | **`FULLTEXT` do MySQL**, com `MATCH ... AGAINST` | dentro do MySQL, com índice invertido e pontuação de relevância |
| **Busca 3** | um buscador escrito por você em Python, com índice invertido próprio, BM25, radical das palavras, sinônimos e tolerância a erro de digitação | fora do banco, em uma camada separada |

**Use sempre esses nomes** (Busca 1, Busca 2, Busca 3) no código, nas planilhas, nos gráficos e no texto do artigo.

E você vai medir:

| O que é medido | Como |
|---|---|
| **Qualidade dos resultados** | 30 consultas de teste em seis categorias, com um gabarito das respostas certas, e três notas: **P@5**, **revocação** e **MRR** |
| **Efeito de cada recurso** | a Busca 3 é construída um recurso por vez (radical, correção de digitação, sinônimos), e cada versão é medida separadamente |
| **Tempo de resposta** | 6 execuções por consulta, descartando a primeira, com a mediana, em três tamanhos de catálogo |
| **Custo** | o espaço ocupado pelos índices e o tempo e a memória para montar o índice da Busca 3 |

### Um aviso que já adianta um resultado

A Busca 3 **não vai ganhar em tudo**, e isso é bom. Nas consultas em que a pessoa digita exatamente o nome do curso, as três buscas devem acertar. A diferença vai se concentrar em **algumas categorias** de consulta (erro de digitação, plural, sinônimo). E a Busca 3 tem um custo que a Busca 2 não tem: o índice dela vive fora do banco e precisa ser refeito quando um curso muda.

**Isso não é defeito do seu trabalho.** É exatamente o tipo de achado que dá valor a um artigo: não "a minha busca é melhor", mas "**a diferença está aqui, custa isto, e vale a pena nesta situação**".

### O que este trabalho **não** é

**Não é "fazer a busca do iFIC".** A plataforma é o **contexto** que justifica a pergunta; o objeto do seu trabalho é o **experimento comparativo**. Você não altera o código da plataforma: tudo acontece no seu repositório.

Guarde esta frase, porque ela vale para o código e para o texto:

> O seu trabalho **não é** "fiz uma busca que funciona". O seu trabalho é **"medi qual forma de busca encontra melhor os cursos FIC, em que tipo de consulta e a que custo, sobre o mesmo banco que a plataforma usa"**.

### O que o seu trabalho tem a favor

1. **Ele produz números.** Não é "eu achei a Busca 3 melhor", é "a Busca 3 obteve P@5 de 0,68 contra 0,31 da Busca 1, nas mesmas 30 consultas".
2. **Ele mede o banco que o projeto usa de verdade.** Como o experimento roda sobre o **MySQL**, a conclusão vale diretamente para o iFIC.
3. **Ele explica, e não só compara.** Como a Busca 3 é construída um recurso por vez, você vai conseguir dizer **quanto cada recurso rendeu sozinho**.

---

<a id="decisoes"></a>
## 3. Decisões já tomadas

Para você não perder tempo escolhendo ferramenta:

| Item | Decisão |
|---|---|
| Linguagem | **Python 3.10 ou mais novo** |
| Onde você trabalha | **computadores do laboratório (Windows)**. Não é possível instalar programas, mas o `pip install` e o Git funcionam |
| Editor | **VS Code** |
| Banco de dados | **MySQL 8 do laboratório**. Você tem um usuário com permissão para criar bancos; o seu banco se chama `ific_busca` |
| Acesso ao MySQL | endereço, porta, usuário e senha eu te envio por mensagem em **16/10**, primeiro dia da Sprint 1. A senha **nunca** vai para o repositório ([seção 5.6](#fluxo-git)) |
| Driver | `PyMySQL` (veja abaixo por quê) |
| Busca 3 | `rank_bm25` (cálculo do BM25), `snowballstemmer` (radical das palavras em português) e `difflib` (correção de digitação, já vem com o Python) |
| Gráficos | `matplotlib` |
| Página web | **Django**, só na Sprint 8, uma página simples |
| Planilhas e estatística | módulos `csv` e `statistics`, que já vêm com o Python |
| Testes | programas curtos de verificação com o comando `assert` ([seção 5.5](#fluxo-git)) |
| Catálogo | de 200 a 300 cursos do **Guia Pronatec de Cursos FIC**, documento público do MEC |
| Repositório | `nicifrn/mp_ific_busca_curso`, só seu, seguindo a política de desenvolvimento do NIC ([seção 5](#fluxo-git)) |
| Texto | **artigo**, no **modelo de TCC do IFRN**, em um documento do Google Drive que eu compartilho com você |
| O que **não** entra | Docker, Elasticsearch, Meilisearch, Solr, busca semântica, busca vetorial e modelos de linguagem. Tudo isso vira "trabalho futuro" no artigo |

### Por que MySQL?

A temática original previa PostgreSQL, mas o iFIC usa **MySQL**, e o trabalho existe para informar uma decisão desse projeto. Medir sobre o banco que a plataforma realmente usa é o que torna o resultado aplicável sem reconfirmação. Isso é um ponto forte do seu artigo, e você vai escrever essa justificativa em Materiais e Métodos.

### Por que a camada de busca é feita em Python, e não com uma ferramenta pronta?

Ferramentas de busca de mercado (Elasticsearch, Meilisearch, Solr) rodam como um serviço separado e precisariam ser instaladas, o que não é possível no laboratório. Por isso a Busca 3 é **construída por você em Python**, com bibliotecas instaladas por `pip`.

Isso não empobrece o trabalho. A Busca 3 usa os mesmos mecanismos que existem dentro das ferramentas grandes: índice invertido, BM25, radical das palavras, sinônimos e tolerância a erro de digitação. **Você vai entender melhor** do que se apenas configurasse uma ferramenta pronta, porque vai construir cada peça e medir o efeito de cada uma separadamente. O custo dessa escolha (os números não se transferem diretamente para uma ferramenta de mercado) vai para as limitações do artigo.

### Por que `PyMySQL` e não `mysqlclient`?

Os dois conectam o Python ao MySQL. O `mysqlclient` é mais rápido, mas precisa ser compilado e falha com frequência ao instalar no Windows. O `PyMySQL` é Python puro e instala sempre. Como **as três buscas usam o mesmo driver**, essa escolha não favorece nenhuma delas. Essa justificativa também vai para Materiais e Métodos.

### Uso de inteligência artificial

- **Pode:** usar uma ferramenta de IA para entender uma mensagem de erro ou um conceito, como faria com um colega.
- **Não pode:** pedir para a IA escrever os seus programas ou o texto do artigo. O código e o texto têm de ser seus, e você precisa saber explicar cada linha na apresentação.
- **Nunca:** colocar no artigo uma referência que você não abriu e leu. Ferramentas de IA inventam referências com naturalidade.

---

<a id="cronograma"></a>
## 4. Cronograma

Cada sprint vai de **sexta a quinta-feira**. O prazo de tudo é a **quinta-feira** que fecha a sprint.

| Sprint | Período | Desenvolvimento | Escrita |
|---|---|---|---|
| 1 | 16/10 a 22/10 | Ambiente e conexão com o MySQL | Preparar o documento e fichar as leituras da Introdução |
| 2 | 23/10 a 29/10 | Catálogo de cursos e Busca 1 (`LIKE`) | **Entrega 1:** Introdução e Objetivo geral |
| 3 | 30/10 a 05/11 | Coleção de teste e script de avaliação | **Entrega 2:** Referencial 2.1, 2.2 e 2.3 |
| 4 | 06/11 a 12/11 | Busca 2 (`FULLTEXT` do MySQL) | **Entrega 3:** Referencial 2.4, 2.5 e 2.6 |
| 5 | 13/11 a 19/11 | Busca 3: índice invertido, radical e BM25 | **Entrega 4:** Metodologia e Materiais e Métodos |
| 6 | 20/11 a 26/11 | Busca 3: correção de digitação e sinônimos | Tarefa curta: tabelas de qualidade no documento |
| 7 | 27/11 a 03/12 | Rodada oficial, tempo, espaço, gráficos e análise de erros | **Entrega 5:** Resultados e Discussão |
| 8 | 04/12 a 10/12 | Página web, README e fechamento | **Entrega 6:** Conclusão, Objetivos específicos, Resumo e Título |

**Tudo termina em 10/12.**

**Feriados:** 02/11 (segunda, Sprint 3) e 20/11 (sexta, primeiro dia da Sprint 6). Nenhum prazo cai em feriado, mas nessas duas semanas o laboratório fica fechado um dia: **a semana tem um dia útil a menos**, então comece cedo.

**Três avisos sobre o cronograma:**

1. **A Sprint 3 é a mais importante do trabalho** e tem um dia a menos. Comece o gabarito na sexta, 30/10.
2. **Os Resultados vencem em 03/12, na mesma semana da rodada oficial e dos gráficos.** Por isso a Sprint 6 já manda colocar as tabelas de qualidade no documento, e a Sprint 7 manda terminar a rodada oficial e os gráficos **até segunda-feira, 30/11**: a terça, a quarta e a quinta ficam para escrever.
3. **A última semana é cheia.** A Conclusão precisa estar escrita até **segunda-feira, 07/12**, para sobrar a terça, a quarta e a quinta para o Resumo, o *Abstract*, o Título e a revisão final.

---

<a id="fluxo-git"></a>
## 5. Como trabalhar no repositório (fluxo do NIC)

O NIC tem uma política de desenvolvimento que vale para todos os projetos. Abaixo está o que ela significa no seu trabalho.

### 5.1 As *branches*

| *Branch* | Para que serve | Quem mexe |
|---|---|---|
| `main` | versão estável e aprovada | só os orientadores, no fim do trabalho |
| `develop` | onde as sprints aprovadas vão se juntando. É a *branch* padrão do repositório | ninguém envia direto: só entra por PR aprovado |
| `feature/...` | uma por sprint, onde você trabalha | você |

Os nomes das *branches* das sprints já estão definidos em cada sprint (por exemplo, `feature/busca2-fulltext`). Se precisar corrigir algo de uma sprint que já foi aprovada, use `fix/` (por exemplo, `fix/leitura-csv`).

### 5.2 O ciclo de cada sprint

**No começo da sprint** (sexta-feira), crie a *branch* da semana a partir da `develop` atualizada:

```
git checkout develop
git pull
git checkout -b feature/nome-da-sprint
```

**Durante a semana**, envie o trabalho **ao fim de cada dia**. Código que só existe na máquina do laboratório não foi entregue, e a máquina pode ser formatada.

```
git status
git add (os arquivos do assunto)
git commit -m "feat: adiciona busca 2 com FULLTEXT"
git push
```

Na primeira vez que der `git push` em uma *branch* nova, o Git pede `git push -u origin feature/nome-da-sprint`. Use exatamente o comando que ele mostrar.

**Antes de todo `git add`, olhe o `git status`.** Se aparecer `config.py`, `.venv/` ou `__pycache__/`, o seu `.gitignore` está errado: corrija antes de continuar. **O `config.py` tem a senha do banco e nunca vai para o Git.**

**No fim da sprint**, abra o PR (seção 5.4).

### 5.3 Mensagens de *commit*

Os *commits* devem ser **pequenos, objetivos e frequentes**: pelo menos 3 por semana. Use o padrão abaixo, com a mensagem em português e o verbo no presente:

```
feat: adiciona busca 2 com FULLTEXT
fix: corrige leitura do CSV com ponto e vírgula
docs: registra configuração do MySQL
test: adiciona testes das métricas
refactor: separa a preparação do texto em funções
```

| Prefixo | Quando usar |
|---|---|
| `feat:` | algo novo funcionando (um script, uma busca, o catálogo) |
| `fix:` | correção de algo que estava errado |
| `docs:` | documentação, diário, `README.md`, prints, planilhas de resultado |
| `test:` | testes |
| `refactor:` | reorganizar código sem mudar o que ele faz |

**Mensagens proibidas pela política do NIC:** `ajustes`, `mudanças`, `update`, `correções`. Se você não consegue dizer em uma frase o que o *commit* faz, ele está grande demais.

### 5.4 O *pull request* do fim da sprint

1. Confira se tudo foi enviado (`git status` deve dizer `nothing to commit`).
2. Rode as verificações que já existirem (seção 5.5). Todas precisam terminar com a mensagem `Tudo certo`.
3. No GitHub, abra o repositório. Vai aparecer uma faixa amarela com o botão **Compare & pull request**. Se não aparecer: aba **Pull requests → New pull request**, com **base: `develop`** e **compare: a sua *branch***.
4. Preencha a descrição. O repositório já traz um modelo com os campos que a política do NIC exige:
   - **Objetivo:** o que esta sprint entrega, em uma ou duas frases;
   - **O que foi feito:** a lista do que foi implementado;
   - **Possíveis impactos:** o que muda para quem roda o projeto (um script novo, uma tabela nova, uma biblioteca nova);
   - **Evidências de teste:** a saída das verificações (copiada do terminal), as tabelas e os prints;
   - **Issue:** `Closes #N`, com o número indicado na sprint.
5. Em **Reviewers**, marque `brunogomesifrn` e `franciscoentony`.
6. Comente na *issue* e mova o card para **Em revisão** (veja a [seção 1](#como-usar)).

**Você não faz o *merge* do seu próprio PR.** A política do NIC exige que pelo menos um revisor aprove antes da integração. **Um PR por sprint**: não acumule duas sprints no mesmo PR.

### 5.5 Testes

A política do NIC pede que toda funcionalidade tenha testes compatíveis com a sua complexidade. No seu trabalho, isso significa **três programas curtos de verificação**, na pasta `testes/`, que conferem sozinhos se as coisas estão certas:

| Programa | Sprint | O que confere |
|---|---|---|
| `testes/verificar_catalogo.py` | 2 | se o catálogo no MySQL tem o número certo de cursos, códigos sem repetição, ementas preenchidas |
| `testes/testar_metricas.py` | 3 | se as funções de P@5, revocação e RR calculam certo, usando exemplos feitos à mão |
| `testes/testar_buscas.py` | 4 (e cresce nas 5 e 6) | se as três buscas respeitam o combinado (lista de códigos, no máximo 20) e se a preparação do texto funciona |

Os três usam só um comando do Python, o **`assert`**:

```python
assert len(resultado) <= 20, "a busca devolveu mais de 20 cursos"
```

Se a condição for **verdadeira**, nada acontece e o programa segue. Se for **falsa**, o programa para na hora e mostra `AssertionError: a busca devolveu mais de 20 cursos`. Ou seja: se o programa chegar até a última linha e mostrar `Tudo certo`, todas as conferências passaram.

Rode sempre **a partir da raiz do repositório**, com o `.venv` ativo, **com a opção `-m` e sem o `.py`**:

```
python -m testes.verificar_catalogo
python -m testes.testar_metricas
python -m testes.testar_buscas
```

Os programas de teste ficam dentro de `testes/`, mas precisam importar o `banco.py` e a pasta `buscadores/`, que estão na raiz. Rodando com `-m` a partir da raiz, o Python procura os módulos a partir da pasta onde você está, e os *imports* funcionam. Se você rodar `python testes\testar_buscas.py`, vai dar `ModuleNotFoundError`. Para isso funcionar, a pasta `testes/` precisa de um arquivo vazio chamado `__init__.py`. *Pesquise:* a opção `-m` do Python e o que ela muda no `sys.path`.

### 5.6 Segurança

A política do NIC proíbe enviar para o repositório senhas, *tokens*, chaves ou arquivos `.env`. No seu trabalho existe **uma** senha: a do MySQL. Ela fica **só** no arquivo `config.py`, que está no `.gitignore`. No repositório vai o `config_exemplo.py`, igual, mas com o texto `coloque-a-senha-aqui` no lugar da senha (é o equivalente do `.env.example` da política).

Se por acidente a senha for enviada, **avise na hora** na *issue* da semana: apagar o arquivo depois não resolve, porque ele continua no histórico do Git, e a senha precisa ser trocada.

---

<a id="estrutura"></a>
## 6. A estrutura de pastas que você vai construir

Você não precisa criar tudo de uma vez: cada sprint cria a sua parte. Esta é a figura final, para você saber aonde está indo. Tudo fica **na raiz do repositório** `mp_ific_busca_curso/`:

```
mp_ific_busca_curso/
├── .github/
│   └── pull_request_template.md  ← já existe (modelo do PR)
├── dados/
│   ├── cursos.csv                ← o catálogo (Sprint 2)
│   ├── consultas.csv             ← as 30 consultas de teste (Sprint 3)
│   ├── gabarito.csv              ← as respostas certas (Sprint 3)
│   ├── criterio.md               ← o critério de relevância (Sprint 3)
│   └── sinonimos.csv             ← a lista de sinônimos (Sprint 6)
├── buscadores/
│   ├── __init__.py
│   ├── busca1_like.py            ← Sprint 2
│   ├── busca2_fulltext.py        ← Sprint 4
│   ├── busca3_python.py          ← Sprints 5 e 6
│   └── busca3_v1.py ... busca3_v4.py  ← Sprint 6 (as quatro versões)
├── testes/
│   ├── __init__.py
│   ├── verificar_catalogo.py     ← Sprint 2
│   ├── testar_metricas.py        ← Sprint 3
│   └── testar_buscas.py          ← Sprints 4, 5 e 6
├── web/                          ← a página em Django (Sprint 8)
├── resultados/
│   ├── qualidade.csv             ← uma linha por consulta e por busca (Sprint 3 em diante)
│   ├── oficial_qualidade.csv     ← a rodada oficial (Sprint 7)
│   ├── oficial_tempos.csv        ← os tempos da rodada oficial (Sprint 7)
│   └── espaco.md                 ← espaço dos índices e memória da Busca 3 (Sprint 7)
├── graficos/                     ← as figuras do artigo (Sprint 7)
├── docs/
│   ├── 01_descricao_geral.md     ← este documento (já existe)
│   ├── projeto_ific.md           ← já existe
│   ├── orientacoes_escrita_tcc.md ← já existe
│   ├── ambiente.md               ← Sprint 1
│   ├── diario.md                 ← Sprint 1 em diante
│   ├── leituras.md               ← Sprint 1 em diante
│   ├── analise_erros.md          ← Sprint 7
│   └── evidencias/               ← prints de tela
├── banco.py                      ← a conexão com o MySQL (Sprint 1)
├── config.py                     ← usuário e senha: NÃO vai para o Git
├── config_exemplo.py             ← modelo sem a senha: esse vai
├── verificar_ambiente.py         ← Sprint 1
├── criar_banco.py                ← Sprints 2, 4 e 7
├── avaliar.py                    ← Sprint 3
├── medir_tempo.py                ← Sprint 7
├── medir_espaco.py               ← Sprint 7
├── graficos.py                   ← Sprint 7
├── .gitignore
├── requirements.txt
└── README.md
```

---

<a id="combinados"></a>
## 7. Combinados que valem para todas as sprints

- **Rode tudo a partir da raiz do repositório:** `python avaliar.py`, e não de dentro de outra pasta. Todos os caminhos dos programas (`dados/`, `resultados/`) partem da raiz.
- **O combinado das três buscas** (vale a partir da Sprint 2 e não muda mais): cada busca é um arquivo em `buscadores/` com uma função **`buscar(termo, limite=20)`**, que devolve **uma lista de códigos de curso, em ordem, com no máximo 20**. Nada de imprimir dentro dela, nada de devolver outro formato. É essa padronização que faz o mesmo script avaliar as três buscas sem mudar nada.
- **Diário (`docs/diario.md`):** no fim de cada sprint, escreva 3 linhas: o que funcionou, o que deu errado e o que aprendi. Leva cinco minutos e vai escrever a sua Conclusão por você no fim do trabalho. Use este formato:

  ```
  ## Sprint 4 - 06/11 a 12/11
  - Funcionou: ...
  - Deu errado: ...
  - Aprendi: ...
  ```

- **Nunca apague uma linha de `resultados/qualidade.csv`, e nunca mude o gabarito depois da Sprint 3.** A confiabilidade do trabalho inteiro está nesses dois arquivos. Se uma medição saiu estranha, ela fica na planilha e você anota o motivo no diário.
- **Anote todo erro e toda surpresa.** Neste trabalho, **surpresa é resultado**. Se a Busca 2 não achou "TI", se a correção trocou uma palavra pela errada, isso vai para o artigo.
- **Prints (`docs/evidencias/`):** sempre que algo funcionar (ou falhar de um jeito interessante), tire um print (`Win + Shift + S`). Dê nomes que digam o que é: `s04_busca2_computador.png`. Eles viram figuras do artigo.
- **Acompanhamento semanal:** no começo de cada sprint, você mostra aos orientadores o que fez na anterior, **rodando na tela**. A partir da Sprint 3, "está funcionando" não basta: tem que ter número.

---

<a id="escrita-geral"></a>
## 8. Como escrever o artigo

### 8.1 Onde escrever: o documento compartilhado no Google Drive

Na Sprint 1 eu compartilho com você um documento do Google Drive que **já está no modelo de TCC do IFRN** (capa, folha de rosto, resumo, sumário e as seções). O seu trabalho é um **artigo**: o modelo é o do TCC, mas o texto é mais curto e mais direto (veja o tamanho na seção 8.3). Você não cria arquivo novo nem trabalha em cópia local.

- **Escreva sempre no documento compartilhado.** Nada de escrever no Word e colar depois: o histórico do Drive é o que nos permite ver o que mudou de uma semana para outra.
- **Não crie cópias** ("Artigo v2", "Artigo final", "Artigo final revisado"). O Drive já guarda tudo em **Arquivo → Histórico de versões**.
- **Marque cada entrega no histórico:** *Arquivo → Histórico de versões → Nomear versão atual*, com um rótulo como `Entrega 1 - Introdução - 29/10`.
- **Avise na *issue* quando entregar**, como explicado na [seção 1](#como-usar). Nós não ficamos olhando o documento: precisamos saber que há algo novo para ler.
- **Comentário se responde, não se apaga.** Responda a cada comentário dizendo o que você fez e só então marque como resolvido.
- **Resolva todos os comentários da entrega anterior antes de avisar sobre a próxima.**
- **Figuras e tabelas** vão dentro do documento, no lugar certo, com a identificação em cima e a fonte embaixo.
- **Não dê acesso ao documento a outras pessoas.**

### 8.2 As normas

Todas as regras de escrita e de ABNT estão em [`docs/orientacoes_escrita_tcc.md`](orientacoes_escrita_tcc.md): estrutura, citações, referências, figuras, tabelas, formatação e linguagem. **Leia esse arquivo inteiro na Sprint 1.** Ele foi escrito para o TCC, e vale para o seu artigo do mesmo jeito; a única diferença é o tamanho de cada seção. Este plano não repete as regras da ABNT; ele diz **o que pesquisar e o que escrever** em cada seção do seu trabalho.

> **Importante:** o que está neste plano são **orientações**, não o texto pronto. Não copie estas frases para o artigo. Elas dizem sobre o que é cada parágrafo; o texto tem de ser escrito por você, com as suas palavras e com as referências que você leu.

### 8.3 A estrutura do seu artigo

```
1 INTRODUÇÃO
1.1 Objetivo geral
1.2 Objetivos específicos
2 REFERENCIAL TEÓRICO
2.1 Recuperação da informação
2.2 Índice invertido e preparação do texto
2.3 Como se avalia um sistema de busca
2.4 Busca textual no MySQL
2.5 Camada de busca dedicada
2.6 Trabalhos relacionados
3 METODOLOGIA
3.1 Classificação da pesquisa
3.2 Perguntas de pesquisa
3.3 Desenho da comparação
3.4 Coleção de teste
4 MATERIAIS E MÉTODOS
4.1 Materiais e ambiente
4.2 O catálogo e as três buscas
4.3 Como as notas, o tempo e o espaço foram medidos
5 RESULTADOS E DISCUSSÃO
5.1 Catálogo e coleção de teste
5.2 Qualidade geral das três buscas
5.3 Qualidade por categoria de consulta
5.4 Tempo de resposta e espaço
5.5 Análise das falhas
5.6 Quadro-síntese e recomendação para o iFIC
5.7 Limitações
6 CONCLUSÃO
REFERÊNCIAS
APÊNDICE A - Consultas de teste
```

Tamanho de referência da parte textual (da Introdução à Conclusão): **de 12 a 18 páginas**, mais ou menos assim: Introdução, 2; Referencial, 4 a 5; Metodologia e Materiais e Métodos, 3 a 4; Resultados, 4 a 6; Conclusão, 1. Artigo é texto enxuto: cada parágrafo tem de ter um motivo para estar ali.

### 8.4 As três perguntas de pesquisa

O trabalho inteiro gira em torno de três perguntas, que saem da pergunta principal da [seção 2](#ideia). Elas aparecem na Metodologia, organizam os Resultados e são respondidas na Conclusão:

1. qual das três buscas encontra melhor os cursos relevantes, medido por **P@5, revocação e MRR**?
2. **em quais tipos de consulta** cada busca se mostra superior, e por quê?
3. qual o **custo** de cada busca em tempo de resposta, espaço ocupado e esforço de manutenção?

A segunda é a mais interessante do trabalho: é ela que gera a figura por categoria.

### 8.5 Regras que valem para o texto inteiro

- **Toda afirmação técnica precisa de referência.**
- **Não empilhe citações.** Explique com as suas palavras, relacione os autores e amarre ao seu trabalho.
- **Documentação oficial** (MySQL, Python, bibliotecas) serve para descrever a ferramenta, não para fundamentar conceito. Para conceito, use livro ou artigo.
- **Nada de blog, Stack Overflow ou site sem autoria** nas Referências. Você vai usar muito esse material para resolver problemas de programação (isso é normal), mas ele não entra na lista.
- **Nunca cite uma referência que você não leu.**
- **Crie a seção "Referências" no primeiro dia** e acrescente cada obra assim que ler.
- O Zotero e o Mendeley (gratuitos, funcionam no navegador) ajudam a montar as referências, mas confira cada entrada com a NBR 6023:2018: esses programas erram com frequência.
- **Meta:** de 12 a 18 referências (lista mínima na [seção 12](#referencias-minimas)).
- **Fichamento:** tudo o que você ler vai para `docs/leituras.md`, no formato abaixo. É ele que transforma leitura em texto:

  ```
  ## MANNING; RAGHAVAN; SCHÜTZE (2008)
  - Referência completa (ABNT): ...
  - Onde achei: (endereço)
  - Ideia principal, com as minhas palavras: ...
  - Trecho que posso citar (com página): "..." (p. X)
  - Vou usar na seção: 2.1 e 2.3
  ```

---

# Sprint 1: 16/10 a 22/10/2026

<a id="sprint-1-dev"></a>
## Sprint 1 · Desenvolvimento: ambiente e conexão com o MySQL

**Branch:** `feature/ambiente-mysql` · **No PR:** `Closes #1`

**O que você vai entregar:** o Git configurado, o repositório clonado, o ambiente virtual com as bibliotecas, a estrutura de pastas, a senha guardada fora do código, um script que conecta no MySQL e responde três perguntas sobre ele, a descrição da máquina e o `README.md` inicial.

Esta sprint é curta de propósito. O objetivo é **eliminar todas as surpresas de ambiente agora**, e não na semana em que você precisar entregar resultado.

**Divida a semana assim:**

| Dia | O que fazer |
|---|---|
| sexta, 16/10 | passos 1 a 6 (Git, repositório, ambiente, pastas) |
| segunda, 19/10 | passos 7 a 9 (senha, conexão e verificação do ambiente) |
| terça, 20/10 | passos 10 e 11 (entender as respostas e preencher o `ambiente.md`) |
| quarta e quinta, 21 e 22/10 | passos 12 e 13 (`README.md`, diário, *commits* e PR) e a escrita da semana |

### Passo a passo

**1. Se você nunca usou Git e GitHub,** assista antes às aulas iniciais do Curso de Git e GitHub do Curso em Vídeo (https://www.cursoemvideo.com/curso/curso-de-git-e-github/), até a parte em que o repositório é enviado para o GitHub. Depois leia a [seção 5](#fluxo-git) deste documento inteira.

**2. Configure o Git** na máquina do laboratório (uma vez só por máquina), com o mesmo e-mail da sua conta do GitHub. Abra o Prompt de Comando (tecle `Win`, digite `cmd`, Enter):

```
git config --global user.name "Seu Nome Completo"
git config --global user.email "seu-email-do-github@exemplo.com"
```

**3. Aceite o convite do repositório.** Você recebeu por e-mail um convite para o `nicifrn/mp_ific_busca_curso`. Aceite-o (ou abra https://github.com/nicifrn/mp_ific_busca_curso/invitations). Aceite também o convite do quadro do projeto, que chega no mesmo e-mail.

**4. Clone o repositório e crie a *branch* da sprint:**

```
cd %USERPROFILE%
git clone https://github.com/nicifrn/mp_ific_busca_curso.git
cd mp_ific_busca_curso
git checkout develop
git checkout -b feature/ambiente-mysql
```

Na primeira vez que o Git falar com o GitHub, abre uma janela do navegador pedindo login. Entre com a sua conta e autorize. Depois abra a pasta `mp_ific_busca_curso` no VS Code (*File → Open Folder*). A partir de agora, **é sempre essa pasta que você abre**.

**5. Crie o ambiente virtual e instale as bibliotecas.** Na raiz do repositório, **no Prompt de Comando** (e não no PowerShell):

```
python -m venv .venv
.venv\Scripts\activate
pip install PyMySQL rank_bm25 snowballstemmer matplotlib
pip freeze > requirements.txt
```

Depois de ativar, o começo da linha passa a mostrar `(.venv)`. **Se não mostrar, o ambiente não está ativo**, e o que você instalar vai para o lugar errado. Toda vez que abrir um terminal novo, ative de novo. O Django fica para a Sprint 8.

> No terminal do VS Code (`` Ctrl + ` ``), abra o seletor de terminal (setinha ao lado do `+`) e escolha **Command Prompt**. No PowerShell, o `activate` costuma dar erro de "execução de scripts desabilitada".
>
> Se o comando `python` não for reconhecido, tente `py`. Se o `py` funcionar, use `py` no lugar de `python` em todos os comandos deste documento, e anote isso no diário.

Repare que o `pip` instalou mais pacotes do que os quatro que você pediu (por exemplo, o `numpy`, que a `rank_bm25` usa). Abra o `requirements.txt` e veja: é para isso que ele existe, para outra pessoa instalar exatamente as mesmas versões.

**6. Crie as pastas e o `.gitignore`.**

1. Crie as pastas `dados`, `buscadores`, `testes`, `resultados`, `graficos` e `docs\evidencias` (veja a [seção 6](#estrutura)). *Pesquise:* o comando `mkdir` no Windows. O Git não guarda pastas vazias; por isso, coloque dentro de cada pasta vazia um arquivo `.gitkeep` vazio.
2. Crie o arquivo `.gitignore` na raiz, com este conteúdo:

   ```
   .venv/
   __pycache__/
   *.pyc
   config.py
   web/db.sqlite3
   ```

**7. Guarde a senha fora do código.** Eu te envio por mensagem, em 16/10, o endereço do servidor, a porta, o usuário e a senha do MySQL do laboratório. Crie na raiz o arquivo `config.py` com **um dicionário** chamado `BANCO`, com estas chaves:

| Chave | Valor |
|---|---|
| `"host"` | o endereço que eu te enviei |
| `"port"` | a porta (um número inteiro, normalmente `3306`) |
| `"user"` | o seu usuário |
| `"password"` | a sua senha |
| `"database"` | `"ific_busca"` |
| `"charset"` | `"utf8mb4"` |

Crie também o `config_exemplo.py`, **igual**, mas com `"password": "coloque-a-senha-aqui"`. Rode `git status`: o `config_exemplo.py` deve aparecer, e o `config.py` **não**. Se o `config.py` aparecer, o `.gitignore` está errado. Pare e corrija antes de qualquer `git add`.

> **Por que `utf8mb4` e não `utf8`?** No MySQL, o `utf8` antigo só guarda caracteres de até 3 bytes. O `utf8mb4` é o UTF-8 completo. *Pesquise:* "MySQL utf8 vs utf8mb4". Uma frase sobre isso vai para Materiais e Métodos.

**8. Escreva o módulo de conexão, `banco.py`.** Todos os outros programas vão abrir a conexão com o MySQL por ele, e nunca diretamente. Ele precisa de uma função `conectar(com_banco=True)` que:

1. faz uma **cópia** do dicionário `BANCO` do `config.py` (para não alterar o original);
2. se `com_banco` for `False`, **remove** a chave `"database"` da cópia (isso serve para conectar antes de o banco existir, na Sprint 2);
3. devolve `pymysql.connect(...)` passando o dicionário como argumentos nomeados.

*Pesquise:* `dict(...)` e `.pop()` para copiar e remover chaves; o operador `**` para passar um dicionário como argumentos nomeados; a documentação de `pymysql.connect`.

**9. Escreva o script `verificar_ambiente.py`.** Ele confere, de uma vez, tudo o que o trabalho precisa. Na ordem:

1. mostrar a versão do Python (`sys.version`) e a do PyMySQL (`pymysql.__version__`);
2. conectar no MySQL **sem escolher banco** (`conectar(com_banco=False)`, porque o `ific_busca` ainda não existe) e, com um cursor, rodar e mostrar a resposta de cada comando abaixo:

   ```sql
   SELECT VERSION();
   SELECT 'informática' = 'informatica';
   SHOW VARIABLES LIKE 'innodb_ft_min_token_size';
   SHOW VARIABLES LIKE 'innodb_ft_enable_stopword';
   SHOW GRANTS;
   ```

3. fechar a conexão;
4. importar `rank_bm25` e `snowballstemmer`, criar o radicalizador de português com `snowballstemmer.stemmer("portuguese")` e mostrar o radical de `"costureiras"`, de `"costureiro"` e de `"costura"` (método `stemWord`).

*Pesquise:* `with conexao.cursor() as cursor:`, `cursor.execute(...)`, `cursor.fetchone()` e `cursor.fetchall()` no PyMySQL. Rode com `python verificar_ambiente.py`.

**10. Entenda o que cada resposta significa**, porque todas vão para o artigo:

- **`VERSION()`:** precisa começar com `8.`. É a versão que vai em Materiais e Métodos;
- **`'informática' = 'informatica'`:** se der `1`, o servidor compara texto **ignorando acentos**. Isso vem da *collation*, a regra de comparação de texto do banco, e é um recurso que você vai ganhar de graça na Busca 1 e na Busca 2. *Pesquise:* "MySQL collation utf8mb4_0900_ai_ci" e o que significam o `ai` e o `ci`;
- **`innodb_ft_min_token_size`:** é o tamanho mínimo de palavra que o índice de texto do MySQL guarda. O padrão é 3, ou seja, palavras de 1 ou 2 letras (como "TI" ou "3D") **não são indexadas**. Mudar isso exige alterar a configuração do servidor e reiniciá-lo, o que você não pode fazer no laboratório. **Não tem problema: vira uma limitação declarada no artigo**, e limitação declarada fortalece o texto;
- **`innodb_ft_enable_stopword`:** se estiver `ON`, o índice de texto ignora uma lista de "palavras vazias". Na Sprint 4 você vai descobrir de que idioma é essa lista;
- **`SHOW GRANTS`:** mostra as suas permissões. Procure `CREATE` (ou `ALL PRIVILEGES`) na resposta: é ela que deixa você criar o banco na Sprint 2;
- **os três radicais:** compare. "costureiras" e "costureiro" dão o mesmo radical? E "costura"? Anote no diário o que você viu: na Sprint 5 isso vai explicar um resultado.

**11. Preencha `docs/ambiente.md`** com a configuração da máquina onde as medições oficiais serão feitas (a do laboratório que você usa sempre; anote também o número ou a identificação dela):

- processador e memória RAM: tecle `Win`, digite "Sobre o seu PC" e anote "Processador" e "RAM instalada";
- sistema operacional e versão: na mesma tela, "Edição" e "Versão";
- versão do Python, do PyMySQL e do MySQL (a saída do `verificar_ambiente.py`), e das outras bibliotecas (`pip list`);
- o resultado do teste de acentos, o valor de `innodb_ft_min_token_size` e o de `innodb_ft_enable_stopword`;
- se o MySQL roda **na mesma máquina** que o Python (o endereço é `localhost` ou `127.0.0.1`) ou em outra máquina da rede. Isso muda o tempo de resposta das Buscas 1 e 2, e precisa estar no artigo.

Sem isso, os tempos medidos na Sprint 7 não significam nada: é a primeira coisa que um avaliador procura em trabalho que mede desempenho.

**12. Escreva o `README.md`** do repositório (se o GitHub já tiver criado um, substitua o conteúdo). Por enquanto, quatro partes, que a política do NIC exige:

1. **o que é este projeto**, em três linhas;
2. **responsáveis:** você e os dois orientadores, com os usuários do GitHub;
3. **instalação:** como criar o ambiente virtual, instalar com `pip install -r requirements.txt` e criar o `config.py` a partir do `config_exemplo.py`;
4. **como rodar:** por enquanto, só o `verificar_ambiente.py`. A cada sprint você acrescenta os programas novos.

**13. Faça os *commits*, um por assunto, e abra o PR.**

1. Crie `docs/diario.md` com as 3 linhas da semana ([seção 7](#combinados)).
2. Faça os *commits* separados, por exemplo:

   ```
   git status
   git add .gitignore requirements.txt config_exemplo.py
   git commit -m "feat: adiciona gitignore, dependências e modelo de configuração"
   git add banco.py verificar_ambiente.py
   git commit -m "feat: adiciona conexão com o MySQL e verificação do ambiente"
   git add docs README.md
   git commit -m "docs: adiciona ambiente, diário, leituras e README"
   git push -u origin feature/ambiente-mysql
   ```

   Inclua também as pastas com `.gitkeep` em um desses *commits*. **Antes de cada `git add`, confira no `git status` que o `config.py` não aparece.**
3. Abra o PR para a `develop`, seguindo a [seção 5.4](#fluxo-git), com `Closes #1`. Em **Evidências de teste**, cole a saída do `verificar_ambiente.py`.

### Como saber que deu certo

Você deve ver na tela algo parecido com isto (os números de versão podem ser outros):

```
Python: 3.11.5 ...
PyMySQL: 1.1.1
MySQL: 8.0.36
Acentos ignorados: 1
('innodb_ft_min_token_size', '3')
('innodb_ft_enable_stopword', 'ON')
Permissões: ...
Radicais: costureiras=..., costureiro=..., costura=...
```

- O terminal mostra `(.venv)` no começo da linha.
- O `git status` **não** mostra `config.py`, `.venv/` nem `__pycache__/`.
- Print da saída guardado em `docs/evidencias/s01_verificar_ambiente.png`.

### Entrega da sprint

- [ ] Git configurado, repositório clonado e *branch* `feature/ambiente-mysql` criada.
- [ ] Ambiente virtual com as quatro bibliotecas e `requirements.txt` gerado.
- [ ] Estrutura de pastas e `.gitignore`.
- [ ] `config.py` criado e **fora do Git**; `config_exemplo.py` dentro.
- [ ] `banco.py` e `verificar_ambiente.py` funcionando, com print em `docs/evidencias/`.
- [ ] `docs/ambiente.md` com máquina, versões, teste de acentos, `innodb_ft_min_token_size`, `innodb_ft_enable_stopword` e onde o MySQL roda.
- [ ] `README.md` com as quatro primeiras partes.
- [ ] `docs/diario.md` com a Sprint 1.
- [ ] PR aberto para a `develop`, com `Closes #1`.

### Erros comuns

- **`Access denied for user`:** usuário ou senha errados no `config.py`.
- **`Can't connect to MySQL server`:** o endereço ou a porta estão errados, ou o servidor não está no ar. Confira o `config.py` com a mensagem que eu te enviei.
- **`ModuleNotFoundError: No module named 'pymysql'`:** o ambiente virtual não está ativo (veja se aparece `(.venv)` na linha).
- **`ModuleNotFoundError: No module named 'config'`:** você rodou o script de dentro de outra pasta. Rode sempre da raiz do repositório.

<a id="sprint-1-escrita"></a>
## Sprint 1 · Escrita: preparar o documento e fichar as leituras da Introdução

**O que você vai entregar:** o documento do artigo aberto e preparado, as normas lidas e as leituras da Introdução fichadas. Nesta semana não há entrega de seção.

### Passo a passo

**1. Abra o documento do artigo** que eu compartilhei com você no Google Drive (o convite chega no seu e-mail). Preencha a capa e a folha de rosto com o seu nome, o curso, o nome dos orientadores e o título provisório: *Busca de cursos de formação inicial e continuada: comparação entre a busca textual do MySQL e uma camada de busca em Python*.

**2. Crie a seção "REFERÊNCIAS"** no fim do documento, ainda vazia. A partir de hoje, toda obra que você ler entra nela no mesmo dia.

**3. Leia as normas.** Leia [`docs/orientacoes_escrita_tcc.md`](orientacoes_escrita_tcc.md) inteiro, com atenção especial a: estrutura do trabalho, Introdução, objetivo geral, como citar e como referenciar.

**4. Leia o resumo do projeto pai** em [`docs/projeto_ific.md`](projeto_ific.md). Ele é o ponto de partida da sua Introdução e já traz referências que você vai reaproveitar.

**5. Pesquise e leia, fichando em `docs/leituras.md`** (no formato da [seção 8.5](#escrita-geral); este arquivo entra no PR de desenvolvimento da semana):

- **as referências do projeto:** Dos Santos e Alliprandini (2023), Lopes, De Fatima Bertini e Borelli (2023) e Laudon e Laudon (2022). As referências completas estão no fim de `docs/projeto_ific.md`. Procure os dois artigos pelo título no **Google Acadêmico** (`scholar.google.com.br`); são de revista e têm o PDF aberto. O livro de Laudon e Laudon tem edição em português (*Sistemas de informação gerenciais*), na biblioteca do campus;
- **a Lei nº 11.892, de 29 de dezembro de 2008,** que criou os Institutos Federais: procure no portal da legislação federal (`planalto.gov.br`) e leia o artigo 7º, que lista os objetivos dos Institutos, entre eles os cursos de formação inicial e continuada;
- **o Guia Pronatec de Cursos FIC**, do Ministério da Educação: procure pelo nome exato no buscador e baixe o PDF da edição mais recente que encontrar no portal do MEC. Leia a apresentação e anote **quantos cursos** ele traz e **quantos eixos tecnológicos**. Você vai usar esse guia de novo na Sprint 2, para montar o catálogo;
- **um número sobre a oferta de cursos FIC:** na **Plataforma Nilo Peçanha** (`plataformanilopecanha.mec.gov.br`), procure o número de matrículas em cursos FIC da Rede Federal no ano mais recente, e, se conseguir filtrar, as do IFRN. Anote o número, o ano dos dados e a data da consulta. Número concreto vale mais que adjetivo;
- **um dado sobre o acesso à internet no Brasil:** na pesquisa **TIC Domicílios**, do Cetic.br (`cetic.br`), procure a proporção de usuários de internet que acessam **apenas pelo celular**. Isso sustenta o argumento de que o público digita no celular e erra mais;
- **o problema do vocabulário:** procure o artigo de **Furnas, Landauer, Gomez e Dumais (1987)**, *The vocabulary problem in human-system communication*, publicado na revista *Communications of the ACM*. Leia o resumo e a conclusão: a ideia central é que pessoas diferentes usam palavras diferentes para a mesma coisa, e que isso derruba a busca por palavra exata. É a base científica do exemplo "faxina" contra "Serviços domésticos";
- **o livro-texto de recuperação da informação:** *Introduction to Information Retrieval*, de **Manning, Raghavan e Schütze (2008)**. A versão completa está disponível gratuitamente no site da Universidade de Stanford (procure pelo título e por "nlp.stanford.edu"). Leia o capítulo 1 (*Boolean retrieval*): ele explica, já nas primeiras páginas, por que ler o texto inteiro a cada busca não funciona e o que é um índice invertido.

### Como saber que deu certo

- O documento do Drive tem capa, folha de rosto e a seção de Referências criadas.
- O `docs/leituras.md` tem pelo menos **8 obras fichadas**, cada uma com a referência completa no formato ABNT.
- Você tem anotados: o número de cursos e de eixos do Guia, o número de matrículas FIC da Plataforma Nilo Peçanha e o dado da TIC Domicílios, cada um com a data da consulta.

### Entrega

- [ ] Documento do Drive com capa, folha de rosto, título provisório e seção de Referências.
- [ ] `docs/orientacoes_escrita_tcc.md` e `docs/projeto_ific.md` lidos.
- [ ] Pelo menos 8 obras fichadas em `docs/leituras.md`, com referência ABNT.
- [ ] Os três números (Guia, Nilo Peçanha, TIC Domicílios) anotados com a data da consulta.
- [ ] As obras lidas lançadas na seção de Referências do documento.

Para entregar, comente na *issue* dizendo quantas obras você fichou e mova o card para **Em revisão**.

---

# Sprint 2: 23/10 a 29/10/2026

<a id="sprint-2-dev"></a>
## Sprint 2 · Desenvolvimento: o catálogo de cursos e a Busca 1

**Branch:** `feature/catalogo-busca1` · **No PR:** `Closes #3`

**O que você vai entregar:** um arquivo com 200 a 300 cursos, carregado em uma tabela do MySQL, a primeira busca funcionando no terminal, a verificação do catálogo terminando com `Tudo certo` e uma tabela com o que a Busca 1 não consegue fazer.

**Aviso:** montar o catálogo dá mais trabalho do que parece, e **tudo** depois depende dele. Comece por ele na sexta-feira.

**Divida a semana assim:**

| Dia | O que fazer |
|---|---|
| sexta a terça, 23 a 27/10 | passo 1 (o catálogo). É a parte que mais demora |
| quarta, 28/10 | passos 2 e 3 (`criar_banco.py` e a Busca 1) |
| quinta, 29/10 | passos 4 a 6 (verificação, testes manuais, diário e PR) |

### Passo a passo

**1. Monte o arquivo de cursos.** Abra o **Guia Pronatec de Cursos FIC** que você baixou na Sprint 1 e, como complemento, a página de cursos FIC do portal do IFRN. Copie os cursos para uma planilha (Excel ou Planilhas Google) com **exatamente** estas colunas, nesta ordem:

```
codigo,nome,eixo,carga_horaria,ementa,origem_ementa
```

Preencha assim:

| Coluna | O que colocar |
|---|---|
| `codigo` | um sequencial que você inventa: `FIC001`, `FIC002`, ... Vai ser a identidade do curso no trabalho inteiro |
| `nome` | o nome do curso, como está no guia |
| `eixo` | o eixo tecnológico (Informação e Comunicação, Produção Alimentícia, Infraestrutura, etc.) |
| `carga_horaria` | o número de horas, só o número |
| `ementa` | **2 a 4 frases** descrevendo o que a pessoa aprende no curso |
| `origem_ementa` | `guia`, se a ementa veio do guia (mesmo resumida), ou `propria`, se você escreveu ou completou |

**Sobre a ementa: leia com atenção, é o ponto mais importante da semana.** É na ementa que estão as palavras que a pessoa digita e que **não** aparecem no título. O guia traz, para cada curso, a descrição do perfil profissional: use essa descrição como base, resumindo em 2 a 4 frases. Se a descrição for muito curta ou genérica, **complete a descrição** com as palavras que uma pessoa comum usaria, e marque `propria`.

Exemplo do que funciona:

> **Nome:** Operador de Computador
> **Ementa:** Curso voltado a quem quer aprender a usar o computador no dia a dia e no trabalho. Aborda Windows, digitação de textos no Word, planilhas no Excel, navegação na internet e uso de e-mail. Indicado para quem tem pouca ou nenhuma experiência com informática.

Repare: a palavra "Excel" não está no título, mas está na ementa. É exatamente esse tipo de caso que o seu trabalho vai medir.

**Três regras que não podem ser quebradas:**

- **a ementa tem que ter relação real com o nome do curso.** Texto aleatório destrói o trabalho inteiro;
- **distribua os cursos por vários eixos** (pelo menos 8). Um catálogo só de informática não representa o iFIC;
- **a coluna `origem_ementa` tem que ser verdadeira.** O número de ementas próprias vai para o artigo. Declarar isso é honestidade científica, e fortalece o texto em vez de enfraquecer.

Salve como **CSV UTF-8** em `dados/cursos.csv`. No Excel: *Salvar como → CSV UTF-8 (delimitado por vírgula)*. Nas Planilhas Google: *Arquivo → Fazer download → Valores separados por vírgula*. Abra o arquivo no VS Code e confira: os acentos aparecem certos, e os campos estão separados por **vírgula**. Se o seu Excel tiver separado por ponto e vírgula, você vai tratar isso no passo 2.

**Meta: 200 cursos bastam.** Se chegar a 300, melhor. **Não pare o trabalho para chegar a 500**: o objeto de estudo é a qualidade da busca, não o tamanho do catálogo.

**2. Escreva `criar_banco.py`.** Ele cria o banco, a tabela e carrega o CSV. Rodar duas vezes não pode quebrar nada (por isso o `IF NOT EXISTS` e o `DROP TABLE IF EXISTS`). O programa faz, nesta ordem:

**a)** conecta **sem banco** (`conectar(com_banco=False)`) e cria o banco:

```sql
CREATE DATABASE IF NOT EXISTS ific_busca
  CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
```

**b)** fecha essa conexão, conecta **com o banco** (`conectar()`) e recria a tabela:

```sql
DROP TABLE IF EXISTS cursos;

CREATE TABLE cursos (
    id            INT AUTO_INCREMENT PRIMARY KEY,
    codigo        VARCHAR(20) NOT NULL UNIQUE,
    nome          VARCHAR(200) NOT NULL,
    eixo          VARCHAR(120) NOT NULL,
    carga_horaria INT NOT NULL,
    ementa        TEXT NOT NULL
) ENGINE=InnoDB;
```

**c)** lê o `dados/cursos.csv` com `csv.DictReader` e, para cada linha, prepara uma tupla com: o código **sem espaços e em maiúsculas**, o nome, o eixo e a ementa **sem espaços nas pontas**, e a carga horária **convertida para `int`**;

**d)** insere todas as tuplas de uma vez, com o comando abaixo e o método `executemany` do cursor:

```sql
INSERT INTO cursos (codigo, nome, eixo, carga_horaria, ementa)
VALUES (%s, %s, %s, %s, %s)
```

**e)** faz o `commit()`, conta os cursos (`SELECT COUNT(*) FROM cursos`) e mostra `N cursos carregados.`

Quatro detalhes que você precisa entender (e que vão para o artigo ou para o diário):

- **abra o CSV com `encoding="utf-8-sig"`**, e não só `"utf-8"`. O Excel grava no começo do "CSV UTF-8" um caractere invisível (o BOM), e com `"utf-8"` o nome da primeira coluna vira `"﻿codigo"`, o que dá `KeyError: 'codigo'`. Se o arquivo estiver separado por ponto e vírgula, passe `delimiter=";"` ao `DictReader`. *Pesquise:* "utf-8-sig python BOM";
- **nunca monte o `INSERT` com f-string.** Os `%s` são preenchidos pelo próprio PyMySQL, que trata aspas e caracteres especiais. Montar SQL juntando texto é a porta da **injeção de SQL**. *Pesquise:* "SQL injection" e "consulta parametrizada". (O nome do banco no `CREATE DATABASE` não pode ser parâmetro, mas ele está escrito no próprio código, não vem de fora: aí não há risco.);
- **`COLLATE utf8mb4_0900_ai_ci`** é o que faz "informatica" encontrar "informática" sem você escrever nenhum código para isso. **Esse detalhe é conteúdo do seu artigo**, não configuração burocrática;
- **`ENGINE=InnoDB`** é o mecanismo de armazenamento do MySQL que suporta o índice `FULLTEXT`, que você vai criar na Sprint 4. Normalmente já é o padrão, mas deixar escrito evita surpresa.

Rode com `python criar_banco.py`, duas vezes seguidas: as duas devem mostrar o mesmo número.

**3. Escreva a Busca 1, em `buscadores/busca1_like.py`.** Crie também o arquivo **vazio** `buscadores/__init__.py`: é ele que faz o Python enxergar a pasta como um pacote (sem ele, o script da Sprint 3 não consegue importar as buscas).

A função segue o combinado da [seção 7](#combinados): `buscar(termo, limite=20)`, devolvendo a lista de códigos. Ela:

1. monta o padrão `%termo%` (o texto digitado entre dois sinais de porcentagem);
2. abre a conexão com `conectar()`;
3. executa o comando abaixo, passando o padrão duas vezes e o limite como parâmetros;
4. fecha a conexão e devolve **só os códigos**, em uma lista.

```sql
SELECT codigo FROM cursos
WHERE nome LIKE %s OR ementa LIKE %s
ORDER BY nome, codigo
LIMIT %s
```

Repare no `ORDER BY nome`: a Busca 1 **não tem noção de relevância**, então a ordem é alfabética. É de propósito: é assim que a busca simples funciona, e é a linha de base da comparação. O `codigo` no fim serve de **desempate**: se dois cursos tiverem o mesmo nome, a ordem fica sempre a mesma. Sem desempate, o banco pode devolver empates em ordem diferente a cada execução, e a nota mudaria sem nada ter mudado. Vale para as três buscas.

No fim do arquivo, coloque um bloco `if __name__ == "__main__":` que pede um termo com `input("Buscar: ")` e mostra quantos cursos voltaram e quais. *Pesquise:* para que serve o `if __name__ == "__main__"`. Rode com `python -m buscadores.busca1_like` (a partir da raiz).

**4. Escreva a verificação `testes/verificar_catalogo.py`** (e crie o `testes/__init__.py` vazio). Leia a [seção 5.5](#fluxo-git). O programa conecta no banco e confere, com `assert`:

1. a tabela tem **pelo menos 200 cursos**;
2. **não há código repetido** (compare `COUNT(*)` com `COUNT(DISTINCT codigo)`);
3. **todo código** tem o formato `FIC` seguido de três dígitos (*pesquise:* `re.fullmatch`);
4. **nenhuma ementa está vazia** e toda carga horária é maior que zero;
5. há **pelo menos 8 eixos diferentes** (`COUNT(DISTINCT eixo)`);
6. os acentos chegaram inteiros: pelo menos um nome ou ementa contém o caractere `ç` (confira no Python, lendo as ementas, e não com `LIKE`: lembre que a collation ignora acentos na comparação).

No fim, mostra `Tudo certo: N cursos verificados.` Além disso, leia o `dados/cursos.csv` e mostre **quantas ementas são `guia` e quantas são `propria`**: esse número vai para o artigo.

**Teste a verificação:** troque, só por um instante, o 200 por 5000 e rode. O programa tem que parar com `AssertionError`. Volte ao valor certo. Uma verificação que nunca falha não verifica nada.

**5. Teste a Busca 1 e anote o que dá errado.** Rode a busca e teste, no mínimo:

| Digite | O que você espera | O que aconteceu |
|---|---|---|
| `informática` | cursos de informática | |
| `informatica` (sem acento) | os mesmos | |
| `exel` | cursos com Excel | |
| `informática básica` | cursos de informática básica | |
| `básica informática` | os mesmos de cima | |
| `costureiras` | cursos de costura | |
| `faxina` | cursos de serviços domésticos ou de limpeza | |

Preencha a coluna da direita e **cole essa tabela no diário**. Ela é ouro: cada linha que deu errado vira um exemplo concreto na problemática da Introdução, que você escreve nesta mesma semana. Exemplo concreto convence muito mais do que frase genérica.

> Repare que a linha do "sem acento" provavelmente **vai funcionar**, por causa da collation. Registre isso: é um recurso que o banco já dá de graça, e saber disso é resultado.

**6. Atualize o `README.md`** (como criar o banco e como testar a Busca 1), escreva o diário, faça os *commits* por assunto (catálogo, `criar_banco.py`, Busca 1, verificação, documentação) e abra o PR com `Closes #3`. Em **Evidências de teste**, cole a saída do `criar_banco.py`, a do `verificar_catalogo` e a tabela do passo 5.

### Como saber que deu certo

- `python criar_banco.py` mostra algo como `247 cursos carregados.`, e rodar de novo mostra o mesmo número.
- `python -m buscadores.busca1_like`, digitando `costura`, mostra uma lista de códigos.
- `python -m testes.verificar_catalogo` mostra `Tudo certo: N cursos verificados.` e a contagem `guia`/`propria`.
- A tabela de testes está preenchida, e você sabe apontar pelo menos **quatro coisas que a Busca 1 não consegue fazer**.

### Entrega da sprint

- [ ] `dados/cursos.csv` com 200 ou mais cursos, de pelo menos 8 eixos, todos com ementa.
- [ ] Coluna `origem_ementa` preenchida e a contagem `guia`/`propria` anotada no diário.
- [ ] `criar_banco.py` funcionando; rodar duas vezes não quebra nada.
- [ ] Collation usada registrada em `docs/ambiente.md`.
- [ ] `buscadores/busca1_like.py` e `buscadores/__init__.py` criados.
- [ ] `testes/verificar_catalogo.py` terminando com `Tudo certo` (e a falha proposital testada).
- [ ] Tabela de testes manuais preenchida em `docs/diario.md`.
- [ ] Print da busca funcionando em `docs/evidencias/`.
- [ ] `README.md` atualizado e PR aberto com `Closes #3`.

### Erros comuns

- **`KeyError: 'codigo'`:** o BOM do Excel. Abra o CSV com `encoding="utf-8-sig"`.
- **`ValueError: invalid literal for int()`:** alguma carga horária está com texto (`"160 horas"`) ou vazia. Corrija no CSV.
- **`IntegrityError: Duplicate entry`:** dois cursos com o mesmo código. Corrija no CSV.
- **`ModuleNotFoundError: No module named 'buscadores'`:** falta o `buscadores/__init__.py`, ou você não está na raiz do repositório.

<a id="sprint-2-escrita"></a>
## Sprint 2 · Escrita: Introdução e Objetivo geral (Entrega 1)

**Prazo:** 29/10/2026

**O que você vai entregar:** a Introdução, em cinco blocos de parágrafos, e o Objetivo geral. Cerca de 2 páginas no total.

A Introdução segue a sequência definida em [`docs/orientacoes_escrita_tcc.md`](orientacoes_escrita_tcc.md): contextualização, problemática, caminho para a solução, apresentação da solução e vínculo com o projeto. Escreva nessa ordem.

### Bloco 1: Contextualização (1 a 2 parágrafos)

**Use as leituras da Sprint 1:** a Lei nº 11.892/2008, o Guia Pronatec de Cursos FIC, o número da Plataforma Nilo Peçanha e o dado da TIC Domicílios.

**Escreva sobre:** a oferta de cursos FIC pela Rede Federal e pelo IFRN, com o número de matrículas; o público desses cursos (amplo, com escolaridade e familiaridade digital variadas, muitas vezes no celular); e o iFIC como plataforma que centraliza e divulga esses cursos. Depois estreite para o ponto: um catálogo com centenas de cursos só é realmente acessível se a pessoa **conseguir encontrar** o curso que procura. Feche com a ideia de que a busca não é um detalhe de interface, é a porta de entrada: um curso que existe mas não é encontrado é, para o candidato, um curso que não existe.

Essa ligação entre **qualidade da busca e acesso à qualificação profissional** é o que faz o seu trabalho ser mais do que um exercício técnico. Ela conversa direto com o objetivo social do iFIC. Use-a aqui e retome na Conclusão.

### Bloco 2: Problemática (1 a 2 parágrafos)

**Pesquise sobre:** as limitações da busca com `LIKE` (procure por "*full table scan*" e "*leading wildcard*": por que o índice comum não ajuda quando o texto procurado pode estar no meio do campo); o problema do vocabulário (Furnas *et al.*, 1987); e erros de digitação em buscas (procure por "*spelling errors in search queries*").

**Escreva sobre:** o problema concreto, **usando a tabela de testes que você fez no passo 5 desta sprint**. A busca simples falha de quatro maneiras, e vale nomear cada uma, com um exemplo do seu catálogo:

1. **não ordena por relevância:** o curso que tem o termo no título aparece depois de outro que o cita de passagem;
2. **não trata consulta de várias palavras:** "básica informática" não encontra "Informática básica";
3. **não tolera erro de digitação:** "exel" devolve tela vazia;
4. **não conhece o vocabulário de quem busca:** "faxina" não chega a "Serviços domésticos".

Explique a consequência: **tela vazia**. E tela vazia, para quem está tentando se inscrever, não é um erro técnico, é uma desistência.

Termine com o que ainda não se sabe: existem duas famílias de solução (usar a busca textual do **próprio banco de dados** ou construir uma **camada de busca separada**), e a escolha entre elas costuma ser feita por preferência da equipe, não por medição. Há pouca avaliação publicada que compare as duas sobre o mesmo catálogo, com as mesmas consultas e **medindo a qualidade dos resultados**, ainda menos em português.

**Evite:** dizer que "a busca do iFIC é ruim". Você não mediu o iFIC em funcionamento. Fale do problema como um fenômeno conhecido da literatura, aplicado a um cenário representativo.

### Bloco 3: Caminho para a solução (1 parágrafo)

**Escreva sobre:** o leque de alternativas como um **gradiente**: começa no que já existe no banco e não custa nada (`LIKE`), passa pelo que o MySQL oferece sem componente novo (o índice `FULLTEXT`) e chega ao que resolve mais problemas ao preço de uma camada a mais para construir e manter (radical das palavras, sinônimos, tolerância a erro de digitação).

Diga também o que o trabalho **não** faz: não trata de busca semântica, busca vetorial nem modelos de linguagem, porque exigem infraestrutura fora do alcance desta etapa. **Recorte declarado é recorte defendido.**

### Bloco 4: Apresentação da solução (1 a 2 parágrafos)

Escreva **no futuro** ("serão comparadas..."); na revisão final, na Sprint 8, você passa para o passado.

**Escreva sobre:** o que será construído e como será avaliado: um protótipo com o catálogo de cursos FIC no **MySQL** e **três formas de busca que convivem no mesmo sistema**; uma **coleção de teste** com 30 consultas em seis categorias e um **gabarito** com as respostas certas; as notas **P@5, revocação e MRR**; e a medição de tempo e espaço.

Destaque duas coisas: **as três buscas convivem no mesmo sistema** para responderem às mesmas consultas, sobre o mesmo catálogo, na mesma máquina, no mesmo dia; e **o banco é o MySQL, o mesmo do iFIC**, o que torna o resultado aproveitável pela plataforma.

Registre que o catálogo parte de fonte pública (Guia Pronatec de Cursos FIC), que **não há dado pessoal** envolvido (Lei nº 13.709/2018, a LGPD) e que **não há participantes de pesquisa**: os julgamentos de relevância são feitos por você, como parte da construção do instrumento de medida, o que dispensa submissão ao Comitê de Ética em Pesquisa.

### Bloco 5: Vínculo com o projeto e escopo (1 parágrafo)

**Escreva sobre:** o vínculo com o projeto iFIC, do IFRN, cuja etapa atual trata de autenticação, painel administrativo e gerenciamento de cursos FIC ([`docs/projeto_ific.md`](projeto_ific.md)). Explique que o protótipo é construído **de forma independente**, para avaliar as abordagens antes de decidir qual adotar, e que a **incorporação ao iFIC é trabalho futuro**.

Feche a Introdução com um parágrafo curto dizendo como o texto está organizado (o que vem na seção 2, na 3, e assim por diante).

### 1.1 Objetivo geral

Uma **única frase**, com **uma única ação principal**, no modelo de [`docs/orientacoes_escrita_tcc.md`](orientacoes_escrita_tcc.md):

> "O objetivo principal do presente trabalho consiste no [ação] de [o quê] para [finalidade]."

- o verbo principal **não** é "desenvolver". O protótipo é meio, não fim: o que o trabalho entrega é conhecimento medido. Use **comparar**, **avaliar** ou **analisar**;
- nomeie **o que** é comparado (as três abordagens de busca), **sobre o quê** (o catálogo de cursos FIC) e **em que dimensão** (qualidade dos resultados e custo);
- **não** empilhe ações ("desenvolver, comparar e integrar" são três objetivos, não um).

**Teste:** leia o objetivo e depois o título provisório. Os dois têm de falar da mesma coisa.

### 1.2 Objetivos específicos

Deixe só o título e a frase "(a ser escrito na Sprint 8)". Eles ficam para o fim de propósito: precisam descrever o que foi **realmente** feito.

### Entrega

- [ ] Os cinco blocos da Introdução, na ordem, com citações.
- [ ] Pelo menos dois exemplos reais da tabela de testes da Busca 1 na problemática.
- [ ] Objetivo geral em uma frase, com um verbo só.
- [ ] Seção 1.2 com "(a ser escrito na Sprint 8)".
- [ ] Obras citadas lançadas nas Referências.
- [ ] Versão nomeada no histórico: `Entrega 1 - Introdução - 29/10`.

Para entregar, comente na *issue* com o nome da versão e mova o card para **Em revisão**.

---

# Sprint 3: 30/10 a 05/11/2026

<a id="sprint-3-dev"></a>
## Sprint 3 · Desenvolvimento: a coleção de teste e o script de avaliação

**Branch:** `feature/colecao-teste` · **No PR:** `Closes #5`

**O que você vai entregar:** 30 consultas de teste, o gabarito das respostas certas, o critério de relevância escrito, a conferência de 10 consultas com o Entony, um script que dá nota para qualquer busca, os testes das notas e as primeiras notas da Busca 1.

**Esta é a sprint mais importante do trabalho.** Sem ela, tudo o que você disser depois é opinião. Com ela, vira medição.

**A ideia, em uma frase:** para saber se uma busca é boa, você precisa de (1) uma lista de buscas que as pessoas fariam e (2) uma lista do que seria a resposta certa para cada uma. Depois é só comparar o que a busca devolveu com o que deveria ter devolvido. Essa forma de avaliar tem nome e quase 60 anos: chama-se **paradigma de Cranfield**, e vai para o seu Referencial Teórico nesta mesma semana.

**Divida a semana assim** (segunda, 02/11, é feriado):

| Dia | O que fazer |
|---|---|
| sexta, 30/10 | passo 1 (as 30 consultas) |
| terça, 03/11 | passos 2 e 3 (o gabarito, o critério e o envio das 10 consultas ao Entony, **até o meio-dia**) |
| quarta, 04/11 | passos 4 a 6 (entender as notas, testes das notas, `avaliar.py`) |
| quinta, 05/11 | passos 7 e 8 (comparar com o Entony, rodar a Busca 1, diário e PR) |

### Passo a passo

**1. Escreva 30 consultas de teste**, cinco de cada uma destas seis categorias:

| Categoria | O que testa | Como escolher | Exemplos |
|---|---|---|---|
| `exato` | o básico: o termo está no título | uma palavra que aparece no nome de algum curso | `eletricista`, `panificação` |
| `generico` | palavras que estão na ementa, não no título | uma palavra que aparece em ementas, mas em nenhum nome | `computador`, `excel` |
| `sem_acento` | a pessoa digita sem acento | uma palavra que tem acento no catálogo, digitada sem | `informatica`, `mecanica` |
| `erro_digitacao` | a pessoa erra ao digitar | uma palavra do catálogo, com 4 letras ou mais, com **uma** letra a mais, a menos ou trocada | `exel`, `eletrisista` |
| `plural` | variação da palavra | plural ou outra forma de uma palavra do catálogo, que **não aparece** nessa forma | `eletricistas`, `padeiros` |
| `sinonimo` | o nome popular, diferente do oficial | uma palavra que **não aparece em lugar nenhum** do catálogo, mas que uma pessoa usaria | `faxina` |

Para conferir cada consulta, abra o `dados/cursos.csv` no VS Code e use `Ctrl + F`: na categoria `generico`, a palavra não pode estar em nenhum nome; na `plural`, a forma digitada não pode aparecer no catálogo; na `sinonimo`, a palavra não pode aparecer em lugar nenhum. Se aparecer, a consulta está na categoria errada: troque.

**Por que categorias, e não 30 consultas soltas?** Porque o resultado mais interessante do seu trabalho não vai ser "a Busca 3 é melhor". Vai ser "**a Busca 3 é melhor exatamente nestas categorias, e empata nas outras**". Isso só aparece se as consultas estiverem organizadas assim desde o começo. **Varie os eixos:** não faça as 30 consultas sobre informática.

Salve em `dados/consultas.csv`:

```
id_consulta,texto,categoria
q01,eletricista,exato
q02,computador,generico
q03,exel,erro_digitacao
```

**2. Monte o gabarito e escreva o critério.** Para cada consulta, leia o catálogo e anote **quais cursos seriam uma resposta certa** para quem digitou aquilo. Salve em `dados/gabarito.csv`, uma linha por par consulta e curso:

```
id_consulta,codigo_curso
q01,FIC014
q01,FIC052
q02,FIC003
```

Uma consulta pode ter 1 curso certo ou 8; o que não pode é ter zero. Se não tiver nenhum, troque a consulta.

**Três regras do gabarito, leia antes de começar:**

1. **Monte o gabarito ANTES de rodar qualquer busca com estas consultas.** Se você rodar uma busca, olhar o resultado e só então decidir o que é relevante, está fazendo um gabarito que favorece aquela busca, e isso invalida o experimento inteiro. Monte lendo o **catálogo**, não os resultados. A Busca 1 já existe: **não a use com estas consultas até o passo 8**;
2. **não procure só pela palavra.** Com `Ctrl + F` você acha os cursos que contêm a palavra, mas a pergunta é outra: *quem digitou isso se inscreveria neste curso?* Leia também os nomes dos cursos do mesmo eixo. Para `faxina`, por exemplo, o curso certo não contém a palavra "faxina", e é justamente isso que a consulta testa;
3. **escreva o seu critério** em `dados/criterio.md`, em cinco linhas: o que você considerou "resposta certa". Por exemplo: *"Considerei relevante todo curso em que uma pessoa que digitou aquele termo se inscreveria, ou que consideraria seriamente. Não considerei cursos que apenas mencionam a palavra de passagem."* Esse texto vai para a Metodologia do artigo.

**3. Envie 10 consultas para o Entony conferir** (terça, 03/11, até o meio-dia). A conferência por uma segunda pessoa dá **muita** credibilidade ao trabalho, e vai ser descrita no artigo.

1. Sorteie as 10 consultas, para a escolha não ser sua: no terminal do Python, use `random.seed(42)` e depois `random.sample(...)` sobre a lista dos 30 identificadores. *Pesquise:* `random.sample`. Anote no `criterio.md` quais saíram e que você usou a semente 42.
2. Envie os arquivos para a sua *branch* (`git add dados`, *commit*, `git push`), **sem o gabarito** nesse *commit*: o `gabarito.csv` vai em um *commit* separado, depois.
3. Comente na *issue* da sprint: `@franciscoentony conferência do gabarito: consultas q04, q11, ... (as 10 sorteadas). O catálogo está em dados/cursos.csv na branch feature/colecao-teste.` Escreva também o texto de cada consulta e o seu critério (copie do `criterio.md`). **Não mande o seu gabarito**: ele julga sem ver o seu, senão a conferência não vale.
4. O Entony responde na própria *issue*, até quarta, 04/11, com os códigos que ele considera certos para cada uma das 10.

**4. Entenda as três notas antes de programá-las.** Suponha que a consulta `q02` tenha 4 cursos certos no gabarito, e que a busca tenha devolvido 20 resultados, dos quais os das posições 1, 2 e 7 estão certos.

- **P@5 (precisão nos 5 primeiros)** = quantos dos 5 primeiros estão certos, dividido por 5. Aqui: 2 certos entre os 5 primeiros = **0,40**.
  *Responde: o que apareceu na primeira tela presta?* É a nota mais importante, porque quem procura curso não rola a página. **Divida sempre por 5**, mesmo que a busca tenha devolvido menos de 5 cursos: tela vazia ou quase vazia tem que ser punida.
- **Revocação** = quantos dos certos a busca achou (nos até 20 que devolveu), dividido pelo total de certos. Aqui: achou 3 dos 4 = **0,75**.
  *Responde: deixou passar algum curso bom?* Como as buscas devolvem no máximo 20, no artigo o nome exato é **revocação nos 20 primeiros (R@20)**.
- **RR (inverso da posição do primeiro acerto)** = 1 dividido pela posição do primeiro resultado certo. Aqui: o primeiro certo está na posição 1 = **1,00**. Se estivesse na posição 4, seria 0,25. Se nenhum estiver certo, 0.
  *Responde: a pessoa achou logo de cara?* A média do RR de todas as consultas chama-se **MRR** (*mean reciprocal rank*).

Faça a conta deste exemplo à mão, no papel, antes de seguir. Se você não consegue calcular à mão, não vai conseguir conferir o programa.

**5. Escreva primeiro os testes das notas, em `testes/testar_metricas.py`.** Sim, antes das funções. Você já sabe as respostas certas (passo 4), então escreva os `assert` primeiro e depois programe até eles passarem. *Pesquise:* "desenvolvimento orientado a testes" (TDD), só para saber o nome do que você está fazendo.

O programa importa de `avaliar.py` as três funções (`precisao_em_5`, `revocacao`, `rr`) e confere, com `assert`, pelo menos estes casos:

| Caso | `resultados` | `certos` | P@5 | revocação | RR |
|---|---|---|---|---|---|
| o exemplo do passo 4 | `["A","B","X","Y","Z","W","C"]` | `{"A","B","C","D"}` | 0,40 | 0,75 | 1,00 |
| primeiro acerto na posição 4 | `["X","Y","Z","A"]` | `{"A"}` | 0,20 | 1,00 | 0,25 |
| busca vazia | `[]` | `{"A"}` | 0,00 | 0,00 | 0,00 |
| tudo certo | `["A","B","C","D","E"]` | `{"A","B","C","D","E"}` | 1,00 | 1,00 | 1,00 |

Número decimal no computador não é exato (`0.1 + 0.2` não dá `0.3`). Compare com `math.isclose(...)`, e não com `==`. *Pesquise:* `math.isclose`. No fim, mostre `Tudo certo: metricas conferidas.`

**6. Escreva `avaliar.py`.** Ele precisa ter estas funções:

| Função | O que faz |
|---|---|
| `carregar_consultas()` | lê `dados/consultas.csv` e devolve uma lista de dicionários |
| `carregar_gabarito()` | lê `dados/gabarito.csv` e devolve um **dicionário** `{id_consulta: conjunto de códigos}`, com os códigos sem espaços e em maiúsculas |
| `precisao_em_5(resultados, certos)` | a P@5 do passo 4 |
| `revocacao(resultados, certos)` | a revocação do passo 4 |
| `rr(resultados, certos)` | o RR do passo 4 |
| `avaliar(nome_do_modulo, rotulo)` | importa o módulo da busca pelo nome, roda **todas** as consultas, calcula as três notas de cada uma e devolve uma lista de dicionários, **um por consulta** |
| `salvar(linhas)` | acrescenta as linhas no fim de `resultados/qualidade.csv`, escrevendo o cabeçalho só se o arquivo ainda não existir |

Cada linha salva tem estas colunas: `data_hora`, `busca` (o rótulo), `id_consulta`, `categoria`, `p5`, `revocacao`, `rr`, `qtd_resultados`. A `data_hora` diferencia uma rodada da outra, já que **nenhuma linha é apagada**.

Ao terminar, o programa mostra na tela a **média geral** das três notas e a **média de P@5 por categoria**.

O programa é chamado assim, com o módulo e o rótulo na linha de comando:

```
python avaliar.py buscadores.busca1_like busca1_like
```

*Pesquise:* `importlib.import_module` (importar um módulo a partir do nome em texto), `sys.argv`, `csv.DictReader` e `csv.DictWriter`, `os.path.exists`, `statistics.mean`, `collections.defaultdict` (para agrupar por categoria) e `datetime.now().isoformat()`.

Dois cuidados:

- **padronize os códigos que a busca devolve** (sem espaços e em maiúsculas) antes de comparar com o gabarito. Em Python, `"FIC001"` e `"fic001"` são textos diferentes;
- **guarde uma linha por consulta, nunca só a média.** É esse detalhe que vai produzir a análise por categoria, o melhor resultado do seu trabalho.

Rode os testes até passarem: `python -m testes.testar_metricas`.

**7. Compare o seu julgamento com o do Entony** (quinta, 05/11). Para cada uma das 10 consultas, calcule a concordância: o número de cursos que **os dois** marcaram, dividido pelo número de cursos que **pelo menos um** marcou. Isso se chama **coeficiente de Jaccard**; *pesquise* o nome e a fórmula com conjuntos (`&` e `|` em Python). Anote no `criterio.md`:

- a concordância de cada consulta e a média das 10;
- em quais vocês divergiram e por quê;
- o que você mudou no gabarito depois da conversa (se mudou).

Ajustar o gabarito **agora**, depois da conferência e antes de rodar as buscas, é legítimo e deve ser relatado. Depois do passo 8, o gabarito **não muda mais**.

**8. Meça a Busca 1.** Só agora rode:

```
python avaliar.py buscadores.busca1_like busca1_like
```

As médias provavelmente vão ser **baixas**. É isso mesmo: a Busca 1 é a linha de base e ela é fraca de propósito. **Anote os três números e a P@5 por categoria no diário**: eles são o ponto de partida de toda a comparação.

Faça os *commits* por assunto (consultas, gabarito, critério, `avaliar.py`, testes, resultados), atualize o `README.md` (como rodar a avaliação e os testes) e abra o PR com `Closes #5`.

### Como saber que deu certo

- `python -m testes.testar_metricas` mostra `Tudo certo: metricas conferidas.`
- `python avaliar.py buscadores.busca1_like busca1_like` mostra as três médias e a P@5 de cada categoria.
- O `resultados/qualidade.csv` tem 30 linhas (mais o cabeçalho).
- O `criterio.md` tem o critério, as 10 consultas sorteadas, a concordância com o Entony e os ajustes.

### Entrega da sprint

- [ ] `dados/consultas.csv` com 30 consultas, 5 de cada categoria, conferidas com `Ctrl + F`.
- [ ] `dados/gabarito.csv` completo, sem consulta com zero cursos certos.
- [ ] `dados/criterio.md` com o critério, o sorteio, a concordância com o Entony e os ajustes.
- [ ] `testes/testar_metricas.py` com os quatro casos, terminando com `Tudo certo`.
- [ ] `avaliar.py` rodando de ponta a ponta.
- [ ] Notas da Busca 1 em `resultados/qualidade.csv` e no diário.
- [ ] PR aberto com `Closes #5`.

### Erros comuns

- **Revocação maior que 1:** você está contando resultados repetidos, ou dividindo pelo número errado. Confira com o caso "tudo certo" do teste.
- **Todas as notas zero:** os códigos da busca e os do gabarito não estão no mesmo formato (espaço, maiúscula). Padronize os dois lados.
- **`ModuleNotFoundError: No module named 'buscadores'`:** rode da raiz do repositório.

<a id="sprint-3-escrita"></a>
## Sprint 3 · Escrita: Referencial Teórico, seções 2.1, 2.2 e 2.3 (Entrega 2)

**Prazo:** 05/11/2026

**O que você vai entregar:** as três primeiras seções do Referencial, cerca de 2,5 páginas.

**Explicação em vídeo (assista antes de começar):** https://youtu.be/8Qztq1Q5vb0

Neste trabalho o referencial não é enfeite: ele **define as notas** que você vai apresentar e **explica** por que cada busca acerta ou erra. Se você apresentar MRR nos Resultados sem ter definido antes, o texto trava. **Esta entrega cai de propósito na semana em que você programa as notas**: escrever sobre P@5 enquanto programa a P@5 é muito mais fácil.

**Comece pelos livros-texto, não pelo Google.** Recuperação da informação é uma área madura, com livros consagrados: Manning, Raghavan e Schütze (*Introduction to Information Retrieval*, que você já começou a ler), Baeza-Yates e Ribeiro-Neto (*Recuperação de informação: conceitos e tecnologia das máquinas de busca*, com edição em português) e Croft, Metzler e Strohman (*Search engines: information retrieval in practice*, disponível gratuitamente no site dos autores). **Com dois desses livros você cobre quase todo o referencial com fonte de primeira linha.**

Escreva **apenas sobre o que reaparece** na Metodologia ou nos Resultados.

### 2.1 Recuperação da informação (cerca de 0,75 página)

**Pesquise:** "recuperação da informação", "*information retrieval*", "*ranking*", "*relevance*", "*TF-IDF*", "*BM25*".

**Escreva:** o que é recuperação da informação e **como ela difere de uma consulta comum a banco de dados**. Este é o parágrafo mais importante da subseção: em um `SELECT ... WHERE`, a resposta é exata e binária (a linha satisfaz ou não a condição); em recuperação da informação, a resposta é **ordenada por relevância**, aproximada, e o que interessa é o que está no topo. Observe que **o mesmo SGBD oferece os dois modos**: o `LIKE` responde do primeiro jeito; o `MATCH ... AGAINST` responde do segundo.

Depois explique o que é uma **pontuação de relevância** e apresente o **TF-IDF** e o **BM25**. Não precisa deduzir fórmula; precisa explicar a ideia: uma palavra **rara** no catálogo, que aparece **várias vezes** em um documento **curto**, pesa mais que uma palavra comum.

### 2.2 Índice invertido e preparação do texto (cerca de 1 página)

**Pesquise:** "*inverted index*", "*tokenization*", "*stop words*", "*stemming*", o algoritmo **Snowball** para português e o **RSLP** (removedor de sufixos da língua portuguesa, de Orengo e Huyck). Procure também "*edit distance*" e "**distância de Levenshtein**".

**Escreva:** o que é um **índice invertido** e por que ele permite buscar em milhares de documentos sem ler todos. Compare explicitamente com o que o `LIKE '%termo%'` faz, que é ler todos. Depois, a cadeia de preparação do texto:

- **tokenização:** separar o texto em palavras;
- **normalização:** minúsculas e remoção de acentos;
- **palavras vazias** (*stop words*): por que "de", "para" e "curso" não ajudam a distinguir nada;
- **redução ao radical** (*stemming*): por que "costureiras" e "costureiro" deveriam casar, e o que é preciso para que casem. Diferencie de **lematização** (reduzir à forma de dicionário), em uma frase.

Termine com a **distância de Levenshtein**: a definição, um exemplo mínimo (de "exel" para "excel" é uma inserção) e por que os buscadores não corrigem palavras muito curtas.

**Escreva pensando na análise de erros da Sprint 7:** cada conceito daqui vai ser usado lá para explicar uma falha. É o vocabulário do seu trabalho.

### 2.3 Como se avalia um sistema de busca (cerca de 0,75 página)

**Esta é a subseção que sustenta a validade do trabalho inteiro.**

**Pesquise:** "*Cranfield paradigm*", "*test collection*", "*relevance judgments*", "*precision*", "*recall*", "*precision at k*", "*mean reciprocal rank*". O capítulo 8 do livro de Manning, Raghavan e Schütze cobre tudo isso.

**Escreva:** o **paradigma de Cranfield** e as suas três peças (a coleção de documentos, o conjunto de consultas e o gabarito de relevância). Depois **cada nota que você usou**, com a definição e o significado prático:

- **precisão** e **revocação**, e a tensão entre as duas;
- **P@5**, e por que ela é a nota mais adequada quando a pessoa olha só a primeira tela;
- **MRR**, e o que ela captura que a precisão não captura: a **posição** do primeiro acerto.

Trate também das **limitações do método**: o julgamento de relevância é subjetivo, e uma coleção pequena limita a generalização. Diga como isso se atenua: **critério escrito** e **conferência por um segundo avaliador**, medida pela concordância. Você fez as duas coisas nesta semana; fundamentá-las aqui é o que permite afirmá-las na Metodologia.

### Entrega

- [ ] Seções 2.1, 2.2 e 2.3, com toda afirmação técnica referenciada.
- [ ] P@5, revocação e MRR definidas com as suas palavras, com o significado prático de cada uma.
- [ ] Pelo menos dois livros-texto de recuperação da informação citados e lançados nas Referências.
- [ ] Comentários da Entrega 1 respondidos e resolvidos.
- [ ] Versão nomeada no histórico: `Entrega 2 - Referencial 2.1 a 2.3 - 05/11`.

Para entregar, comente na *issue* com o nome da versão e mova o card para **Em revisão**.

---

# Sprint 4: 06/11 a 12/11/2026

<a id="sprint-4-dev"></a>
## Sprint 4 · Desenvolvimento: Busca 2, o FULLTEXT do MySQL

**Branch:** `feature/busca2-fulltext` · **No PR:** `Closes #7`

**O que você vai entregar:** a segunda busca funcionando, usando o índice de texto do próprio MySQL, a escolha do peso do nome feita por medição, a comparação com a Busca 1, as limitações do MySQL investigadas e o teste das buscas.

**A ideia, em uma frase:** em vez de varrer todas as linhas procurando um pedaço de texto, o MySQL monta antes uma lista de "em quais cursos cada palavra aparece" (isso é o **índice invertido**) e usa essa lista para responder **ordenado por relevância**.

**Divida a semana assim:**

| Dia | O que fazer |
|---|---|
| sexta, 06/11 | passos 1 e 2 (índices e Busca 2) |
| segunda, 09/11 | passos 3 e 4 (pesos e medição) |
| terça, 10/11 | passo 5 (comparação) |
| quarta, 11/11 | passos 6 e 7 (limitações e plano de execução) |
| quinta, 12/11 | passo 8 (teste das buscas, diário e PR) |

### Passo a passo

**1. Crie os índices `FULLTEXT`.** No `criar_banco.py`, **depois** de carregar os cursos e fazer o `commit`, execute:

```sql
ALTER TABLE cursos ADD FULLTEXT INDEX ft_nome (nome);
ALTER TABLE cursos ADD FULLTEXT INDEX ft_ementa (ementa);
```

e mostre `Indices FULLTEXT criados.` Rode `python criar_banco.py` de novo. Pode aparecer um aviso (*warning*) dizendo que o InnoDB vai reconstruir a tabela para acrescentar a coluna `FTS_DOC_ID`: é normal, é a coluna interna que o índice de texto usa.

Confira no MySQL que os índices existem:

```sql
SHOW INDEX FROM cursos;
```

Devem aparecer `ft_nome` e `ft_ementa`, com `Index_type` igual a `FULLTEXT`.

**Por que dois índices separados, e não um só sobre as duas colunas?** No MySQL, o `MATCH()` só funciona se existir um índice `FULLTEXT` **exatamente** sobre as colunas que ele cita. Com dois índices separados, dá para calcular uma pontuação para o nome e outra para a ementa, e somar as duas com **pesos diferentes**: casar no título deve valer mais do que casar na ementa. Com um índice só, não haveria como priorizar o título.

**2. Escreva a Busca 2, em `buscadores/busca2_fulltext.py`.** Ela tem duas funções.

**a) `limpar(termo)`:** devolve o termo só com letras, números e espaços. Sinais como `+`, `-`, `*`, `"`, `(` e `@` têm significado especial na busca de texto do MySQL e podem causar erro ou resultado estranho quando vêm do usuário. *Pesquise:* `re.sub` com a classe `[^\w\s]`; confirme que `\w` aceita letras acentuadas em Python 3.

**b) `buscar(termo, limite=20)`:** limpa o termo; se ficar vazio, devolve lista vazia; senão, executa o comando abaixo e devolve a lista de códigos.

```sql
SELECT codigo,
       MATCH(nome)   AGAINST (%s IN NATURAL LANGUAGE MODE) * %s
     + MATCH(ementa) AGAINST (%s IN NATURAL LANGUAGE MODE) * %s
       AS relevancia
FROM cursos
HAVING relevancia > 0
ORDER BY relevancia DESC, codigo
LIMIT %s
```

Os parâmetros, na ordem: o termo limpo, o peso do nome, o termo limpo de novo, o peso da ementa e o limite. Coloque os pesos como **constantes no topo do arquivo**, `PESO_NOME = 3` e `PESO_EMENTA = 1`, para poder trocá-los no passo 3. Acrescente o mesmo bloco `if __name__ == "__main__":` da Busca 1.

Quatro pontos para entender (e escrever no artigo):

- **o que mudou de verdade:** agora existe uma **pontuação de relevância** calculada pelo banco, e os resultados vêm ordenados por ela. Deixou de ser "contém este texto" e passou a ser "o quanto este curso combina com a busca". **Esse salto conceitual é mais importante que o ganho numérico**;
- **`IN NATURAL LANGUAGE MODE`** é o modo padrão: o MySQL separa a busca em palavras e procura cada uma. É por isso que "básica informática" passa a encontrar "Informática básica";
- **no MySQL a pontuação é positiva, e quanto maior, melhor**: daí o `ORDER BY relevancia DESC`;
- **`HAVING` em vez de `WHERE`:** como `relevancia` é um apelido criado na própria consulta, o MySQL só permite filtrá-lo no `HAVING`. *Pesquise:* "MySQL HAVING alias", e anote no diário.

**3. Escolha o peso do nome pela medição.** Rode a avaliação três vezes, mudando só a constante `PESO_NOME` (1, depois 3, depois 5, sempre com `PESO_EMENTA = 1`), com um rótulo diferente em cada uma:

```
python avaliar.py buscadores.busca2_fulltext busca2_peso1
python avaliar.py buscadores.busca2_fulltext busca2_peso3
python avaliar.py buscadores.busca2_fulltext busca2_peso5
```

Monte uma tabelinha no diário (peso × P@5 × revocação × MRR) e **escolha pelo número, não pela intuição**. Em caso de empate na P@5, desempate pelo MRR. Essa tabela vira um parágrafo de Materiais e Métodos.

> **Um cuidado para o artigo:** você está escolhendo o peso com as mesmas consultas que vai usar para comparar as buscas. Isso favorece um pouco a Busca 2 (e, na Sprint 5, a Busca 3, que passa pelo mesmo ajuste). Como as duas são ajustadas do mesmo jeito, a comparação continua justa, mas **declare isso nas limitações**. *Pesquise:* "*overfitting* ao conjunto de teste".

**4. Meça a versão escolhida.** Deixe `PESO_NOME` no valor vencedor e rode com o rótulo definitivo:

```
python avaliar.py buscadores.busca2_fulltext busca2_fulltext
```

**5. Compare as duas buscas.** No diário, monte as duas tabelas:

| Busca | P@5 | Revocação | MRR |
|---|---|---|---|
| Busca 1 (LIKE) | | | |
| Busca 2 (FULLTEXT) | | | |

| Categoria | P@5 Busca 1 | P@5 Busca 2 |
|---|---|---|
| exato | | |
| generico | | |
| sem_acento | | |
| erro_digitacao | | |
| plural | | |
| sinonimo | | |

Depois olhe o detalhe no `resultados/qualidade.csv`: **em quais consultas a Busca 2 ganhou muito, e em quais não mudou nada?** Anote pelo menos 3 de cada, com o motivo.

**O que você deve investigar** (e, se conseguir explicar, terá entendido a semana):

- houve melhora nas consultas de termo genérico e nas de duas palavras? Se houve, por quê?
- as consultas sem acento continuam funcionando? Qual recurso do banco explica isso?
- o que acontece com `exel` e com os plurais? O índice guarda a palavra inteira ou o radical?

Se os erros de digitação e os plurais **não melhorarem**, isso **não é um defeito do seu trabalho**. É a descoberta que justifica a Busca 3. Anote com destaque.

**6. Investigue três limitações do MySQL e registre as três.** São material de primeira qualidade para o artigo:

**a) Palavras curtas não são indexadas.** Busque `TI` e `3D` na Busca 2 e veja o que volta. Relacione com o valor de `innodb_ft_min_token_size` que você anotou na Sprint 1. Mudar esse valor exige alterar a configuração do servidor e reiniciá-lo. **Declare como limitação.**

**b) A lista de palavras vazias é em inglês.** Rode:

```sql
SELECT * FROM INFORMATION_SCHEMA.INNODB_FT_DEFAULT_STOPWORD;
```

Anote quantas palavras são e de que idioma. Repare se "de", "para" e "com" estão nela. Se não estiverem, elas **são indexadas** no seu catálogo, mesmo não distinguindo nada. O MySQL permite trocar essa lista por uma tabela própria, mas isso exige configurar o banco **antes** de criar o índice; neste trabalho você mantém o padrão, que é o que a plataforma teria se ninguém mexesse. *Pesquise:* `innodb_ft_user_stopword_table` e escreva no diário, em duas linhas, como seria a troca (é a extra E2 da [seção 11](#extras)). Note também que a Busca 3, em Python, vai ter a lista em português com poucas linhas de código: esse contraste é um bom parágrafo do artigo.

**c) Palavra muito frequente vale quase nada.** Busque `curso` na Busca 2 e veja o que acontece. *Pesquise:* o IDF e por que uma palavra que aparece em quase todos os documentos recebe pontuação perto de zero. É assim que o cálculo de relevância funciona: é resultado, não defeito.

**7. Olhe o plano de execução.** O `EXPLAIN` mostra **como** o MySQL vai executar uma consulta, sem executá-la. Rode e compare:

```sql
EXPLAIN SELECT codigo FROM cursos WHERE nome LIKE '%eletricista%';

EXPLAIN SELECT codigo FROM cursos
WHERE MATCH(nome) AGAINST ('eletricista' IN NATURAL LANGUAGE MODE);
```

Para cada um, anote no diário as colunas `type`, `key` e `rows`. *Pesquise:* o que significam `type = ALL` e `type = fulltext` no `EXPLAIN` do MySQL. Depois rode o `EXPLAIN` da consulta da Busca 2 (a do passo 2, com valores no lugar dos `%s`) e anote o que aparece: ela usa o índice da mesma forma que a consulta com `WHERE MATCH`? Guarde as três saídas em `docs/evidencias/` (print ou texto): na Sprint 7 elas vão explicar os tempos.

**8. Escreva `testes/testar_buscas.py`.** Ele confere o combinado da [seção 7](#combinados) para as buscas que já existem (Busca 1 e Busca 2), com `assert`:

1. para cada uma das 30 consultas de `dados/consultas.csv`, o `buscar()` devolve uma **lista**, com **no máximo 20** itens, todos **textos** no formato `FICnnn`, e **sem códigos repetidos**;
2. a Busca 1 e a Busca 2 encontram pelo menos um curso para uma consulta da categoria `exato` (escolha uma e escreva qual no código);
3. a Busca 2 devolve lista vazia para um termo vazio e para um termo só com símbolos (`"+++"`);
4. a Busca 2 encontra `"basica informatica"` e `"informática básica"` **nos mesmos cursos** (compare como conjuntos).

No fim, `Tudo certo: buscas conferidas.` Nas Sprints 5 e 6 você acrescenta as conferências da Busca 3. Faça o mesmo teste de sabotagem da Sprint 2.

Atualize o `README.md` e o diário, faça os *commits* por assunto e abra o PR com `Closes #7`.

### Como saber que deu certo

- `python -m buscadores.busca2_fulltext`, digitando `computador`, devolve cursos de informática **mesmo que "computador" não esteja no nome deles**.
- Digitando `basica informatica`, devolve os cursos de informática básica.
- `python -m testes.testar_buscas` mostra `Tudo certo: buscas conferidas.`
- O `resultados/qualidade.csv` tem agora 150 linhas (30 da Busca 1, 90 do teste de pesos e 30 da versão escolhida).

### Entrega da sprint

- [ ] Índices `FULLTEXT` criados pelo `criar_banco.py` e conferidos com `SHOW INDEX`.
- [ ] `buscadores/busca2_fulltext.py` funcionando, com `limpar()` e `buscar()`.
- [ ] Teste dos pesos do nome (1, 3, 5) feito e a escolha justificada no diário.
- [ ] Busca 2 medida com o rótulo `busca2_fulltext`.
- [ ] Tabelas Busca 1 × Busca 2 (geral e por categoria) e as 3 + 3 consultas comentadas no diário.
- [ ] As três limitações (palavra curta, palavras vazias, palavra frequente) testadas e registradas.
- [ ] Os três `EXPLAIN` guardados em `docs/evidencias/`.
- [ ] `testes/testar_buscas.py` terminando com `Tudo certo`.
- [ ] PR aberto com `Closes #7`.

### Erros comuns

- **A Busca 2 devolve vazio para quase tudo:** confira, nesta ordem, (a) se os índices existem (`SHOW INDEX FROM cursos`); (b) se as palavras da busca têm 3 letras ou mais; (c) se a palavra não aparece em quase todos os cursos (passo 6c).
- **`Can't find FULLTEXT index matching the column list`:** o `MATCH()` está citando colunas diferentes das de um índice. Cada `MATCH` cita uma coluna só, igual ao índice.
- **`Duplicate key name 'ft_nome'`:** o `criar_banco.py` está tentando criar o índice em uma tabela que já o tem. Confira se o `DROP TABLE IF EXISTS` roda antes.

<a id="sprint-4-escrita"></a>
## Sprint 4 · Escrita: Referencial Teórico, seções 2.4, 2.5 e 2.6 (Entrega 3)

**Prazo:** 12/11/2026

**O que você vai entregar:** as três últimas seções do Referencial, cerca de 2,5 páginas, incluindo o quadro de trabalhos relacionados.

### 2.4 Busca textual no MySQL (cerca de 1 página)

**Esta subseção é o centro técnico do seu artigo.** Escreva na mesma semana em que você está mexendo no `FULLTEXT`, com o diário aberto.

**Pesquise:** a documentação do MySQL 8 sobre *full-text search* (índice `FULLTEXT`, `MATCH ... AGAINST`, modo de linguagem natural, modo booleano, `innodb_ft_min_token_size`, palavras vazias) e o conceito de **collation** (procure por "*accent-insensitive collation*"). Para dar panorama, veja também o `tsvector` do PostgreSQL e o FTS5 do SQLite: citar os três mostra que o suporte varia bastante entre bancos.

**Escreva:** o que os bancos relacionais oferecem de busca textual e no que isso difere do `LIKE`: há um índice invertido, há separação em palavras e há pontuação de relevância. Explique o `FULLTEXT` do MySQL: como o índice é construído, o que é o modo de linguagem natural e como a pontuação é obtida. Trate da **collation**, que é ela que faz "informatica" casar com "informática" sem nenhum código adicional.

E então o ponto central: o que o `FULLTEXT` do MySQL **não** oferece, ou oferece só com configuração adicional:

- **redução ao radical:** o índice guarda a palavra inteira;
- **palavras vazias em português:** a lista padrão é em inglês, e trocá-la exige configuração antes de criar o índice;
- **palavras curtas:** por padrão, palavras de 1 ou 2 letras não são indexadas, e mudar isso exige reiniciar o servidor;
- **tolerância a erro de digitação:** não há mecanismo equivalente à distância de edição.

**Formule isso de forma neutra e comparativa, não como reclamação.** O suporte a busca textual **varia entre SGBDs**: esse é um fato relevante para quem escolhe arquitetura. Dito assim, informa; dito como crítica, enfraquece o texto. Acrescente o argumento prático: parte dessas limitações exige alterar a configuração do servidor, o que nem sempre está ao alcance da equipe de desenvolvimento.

### 2.5 Camada de busca dedicada (cerca de 0,75 página)

**Pesquise:** o que ferramentas de busca oferecem além do banco ("*search engine*", "*typo tolerance*", "*synonym expansion*") e as ferramentas do mercado (Elasticsearch, Solr, Meilisearch, Typesense), ainda que você não as use. O livro de Croft, Metzler e Strohman trata da arquitetura de um buscador.

**Escreva:** o que caracteriza uma camada de busca separada do banco e quais recursos ela acrescenta, exatamente os que faltam no `FULLTEXT` e que você vai implementar: radical das palavras, sinônimos e tolerância a erro de digitação. **Amarre esta subseção à anterior:** cada recurso apresentado aqui responde a uma limitação nomeada lá.

E, com o mesmo destaque, **o que essa camada custa**: o índice passa a viver **fora do banco**, o que cria um problema que antes não existia, mantê-lo **sincronizado** com os dados. Se um curso muda e o índice não é refeito, a busca passa a devolver resultados errados sem dar erro nenhum. Apresente as formas usuais de tratar isso (refazer o índice a cada alteração, ou periodicamente).

### 2.6 Trabalhos relacionados (cerca de 0,75 página)

**Pesquise:** trabalhos que **comparem** formas de busca textual: banco relacional contra ferramenta de busca, avaliações de busca em catálogos e bibliotecas digitais, trabalhos brasileiros sobre busca em português. Onde procurar: SBC OpenLib (`sol.sbc.org.br`), BDTD (`bdtd.ibict.br`), repositório do IFRN (`memoria.ifrn.edu.br`), Google Acadêmico, SciELO, ACM DL e IEEE Xplore. Termos úteis: "busca textual MySQL", "*MySQL full-text search*", "avaliação de sistema de busca", "*full-text search comparison*", "recuperação da informação em português".

**Escreva:** de **3 trabalhos**, um parágrafo curto cada, dizendo o que foi comparado, **como foi avaliado** (esta é a informação que mais importa) e qual a limitação. Feche com um **quadro comparativo** entre eles e o seu trabalho, com as colunas: abordagens comparadas, SGBD, idioma, domínio, número de consultas, existe gabarito?, o que foi medido (só tempo, ou também qualidade?).

**Esse quadro é o argumento de originalidade do seu artigo.** É muito comum que trabalhos comparando busca em banco com ferramenta de busca meçam **apenas tempo de resposta**, e não a **qualidade dos resultados**. Se for o caso do que você encontrar, **diga isso explicitamente**: a sua contribuição passa a ser medir a qualidade, com gabarito documentado, em português, em domínio educacional e sobre o MySQL.

### Regras que valem para o referencial inteiro

- **Documentação oficial** (MySQL, bibliotecas) serve para descrever a ferramenta, **não** para fundamentar conceito.
- **Nunca cite uma referência que você não leu.**
- Ao fim desta entrega, você deve ter **pelo menos 10 referências** na lista.

### Entrega

- [ ] Seções 2.4, 2.5 e 2.6, com toda afirmação técnica referenciada.
- [ ] As limitações do `FULLTEXT` descritas de forma neutra, com a documentação do MySQL citada.
- [ ] Quadro comparativo dos trabalhos relacionados com o seu.
- [ ] Comentários da Entrega 2 respondidos e resolvidos.
- [ ] Versão nomeada no histórico: `Entrega 3 - Referencial 2.4 a 2.6 - 12/11`.

Para entregar, comente na *issue* com o nome da versão e mova o card para **Em revisão**.

---

# Sprint 5: 13/11 a 19/11/2026

<a id="sprint-5-dev"></a>
## Sprint 5 · Desenvolvimento: Busca 3, índice invertido, radical das palavras e BM25

**Branch:** `feature/busca3-radical` · **No PR:** `Closes #9`

**O que você vai entregar:** a terceira busca funcionando, feita por você em Python, com índice invertido próprio, pontuação BM25 e redução das palavras ao radical; a escolha de duas decisões de projeto por medição; e a comparação das três buscas.

**A ideia, em uma frase:** em vez de guardar a palavra inteira, guardar só o **radical** dela. Assim "eletricistas" e "eletricista" viram a mesma coisa e passam a casar entre si.

Esta sprint tem bastante código novo, mas é código curto. **Escreva uma função por vez e teste cada uma antes de passar para a próxima.**

**Divida a semana assim:**

| Dia | O que fazer |
|---|---|
| sexta, 13/11 | passo 1 (preparação do texto) |
| segunda, 16/11 | passos 2 e 3 (índice invertido, BM25 e `buscar`) |
| terça, 17/11 | passo 4 (as duas decisões por medição) |
| quarta, 18/11 | passos 5 e 6 (medição e comparação das três) |
| quinta, 19/11 | passo 7 (testes, diário e PR) |

### Passo a passo

**1. Escreva as funções de preparação do texto**, no começo de `buscadores/busca3_python.py`. São quatro peças, e cada uma é um conceito do seu Referencial:

| Função ou constante | O que faz | Exemplo |
|---|---|---|
| `separar_palavras(texto)` | põe em minúsculas e quebra o texto em palavras, descartando pontuação | `"Informática Básica!"` → `["informática", "básica"]` |
| `sem_acento(texto)` | tira os acentos | `"informática"` → `"informatica"` |
| `PALAVRAS_VAZIAS` | um conjunto (`set`) de palavras que não distinguem nada, **sem acento** | `"de"`, `"para"`, `"com"`, `"curso"`... |
| `RADICALIZADOR` | o radicalizador de português do `snowballstemmer` | `stemWord("eletricistas")` → `"eletric"` |

E a função que junta tudo: **`preparar(texto)`**, que recebe um texto e devolve a lista de radicais, sem as palavras vazias e sem as palavras de 1 letra.

*Pesquise:* `re.findall` com `\w+`; `unicodedata.normalize("NFKD", ...)` e `unicodedata.combining` (é o jeito padrão de tirar acentos em Python); listas de *stop words* em português (monte a sua com 20 a 30 palavras: artigos, preposições, contrações como "do", "na", "pelo", e as palavras "curso" e "cursos", que aparecem em quase todo o catálogo).

**Uma decisão que você vai medir, e não adivinhar: a ordem entre tirar o acento e tirar o radical.** O radicalizador de português foi feito para palavras **com** acento. Veja o que acontece com duas ordens diferentes:

| Palavra | Ordem A: tira o acento e depois o radical | Ordem B: tira o radical e depois o acento do radical |
|---|---|---|
| `panificação` | `panificaca` | `panific` |
| `panificacao` (digitada sem acento) | `panificaca` | `panificaca` |
| `instalação` | `instalaca` | `instal` |
| `instalações` | `instalaco` | `instal` |

Repare na tensão: na **ordem A**, a palavra com e sem acento sempre dá o mesmo radical, mas o singular e o plural de "instalação" se separam. Na **ordem B**, singular e plural se juntam, mas quem digita "panificacao" sem acento não encontra "panificação". Qual é melhor para o seu catálogo e as suas consultas? **Não decida agora: escreva `preparar` com um parâmetro `ordem="A"` ou `ordem="B"`** e meça as duas no passo 4.

Confira no terminal do Python os valores da tabela antes de seguir (os seus devem bater). Teste também:

```
preparar("Curso de Eletricistas")    → um radical só
preparar("de para com")              → lista vazia
preparar("informática") == preparar("informatica")    → na ordem A, sempre True
```

**Só continue quando as funções estiverem dando o que você espera.** E anote no diário uma descoberta da Sprint 1: "costureiras" e "costureiro" têm o mesmo radical, mas "costura" tem outro. O *stemming* junta variações da **palavra**, não palavras de **mesmo assunto**. Isso vai explicar um resultado da categoria `sinonimo`.

**2. Monte o índice invertido e o modelo BM25.** Acrescente ao mesmo arquivo:

**a) `carregar_cursos()`:** busca no MySQL (pelo `conectar()` do `banco.py`) o código, o nome e a ementa de todos os cursos, **ordenados por código**:

```sql
SELECT codigo, nome, ementa FROM cursos ORDER BY codigo
```

**b) `montar_indice(repeticoes_nome=2, ordem="A")`:** para cada curso, monta o texto juntando o nome repetido `repeticoes_nome` vezes e a ementa, passa por `preparar` e guarda:

- `CODIGOS`: a lista dos códigos, na ordem (a posição de um curso nessa lista é o "número do documento");
- `DOCUMENTOS`: a lista das listas de radicais, na mesma ordem;
- `INDICE`: o **índice invertido**, um dicionário `{radical: conjunto das posições dos cursos que têm esse radical}`. Por exemplo, `INDICE["eletric"]` pode ser `{3, 17, 42}`;
- `MODELO`: `BM25Okapi(DOCUMENTOS)`, da biblioteca `rank_bm25`.

Guarde os quatro em variáveis globais do módulo e chame `montar_indice()` uma vez no fim do arquivo, para o índice ficar pronto quando o módulo for importado. *Pesquise:* `dict.setdefault`, `set.add` e a palavra-chave `global`.

> **Por que repetir o nome?** É a forma mais simples de dar mais peso ao título, equivalente ao `PESO_NOME` da Busca 2. É uma decisão de projeto, e **precisa estar declarada no artigo**. Você vai escolher o número de repetições pela medição, no passo 4.

> **Repare em uma diferença importante:** a Busca 3 lê os cursos **do MySQL** e monta o índice **na memória do Python**. Ou seja, o índice passa a viver **fora do banco**. Se um curso mudar no banco, o índice em memória fica desatualizado até ser montado de novo. Guarde essa observação: na Sprint 7 você vai demonstrá-la na prática.

**3. Escreva `buscar(termo, limite=20)`.** Ela faz, nesta ordem:

1. prepara o termo com a mesma função (e a mesma ordem) usada no índice; se não sobrar nenhum radical, devolve lista vazia;
2. **usa o índice invertido** para achar os **candidatos**: a união dos conjuntos de posições de cada radical da consulta (radical que não está no índice não contribui com nada). Se não houver candidato, devolve lista vazia;
3. calcula a nota BM25 **só dos candidatos**, com `MODELO.get_batch_scores(radicais, lista_de_candidatos)`;
4. descarta as notas menores ou iguais a zero, ordena da **maior nota para a menor**, com **desempate pelo código** (como nas outras duas buscas), e devolve os códigos dos primeiros `limite`.

*Pesquise:* `set.union` (ou o operador `|`), `sorted` com `key=lambda ...` e ordenação por dois critérios (nota decrescente e código crescente).

**Por que o índice invertido, se a `rank_bm25` já calcula as notas?** Abra o código da biblioteca (no VS Code, segure `Ctrl` e clique em `BM25Okapi`, ou abra `.venv\Lib\site-packages\rank_bm25.py`) e leia os métodos `get_scores` e `get_batch_scores`. Você vai ver que o `get_scores` calcula a nota de **todos** os cursos, a cada busca, mesmo os que não têm nenhuma palavra da consulta. Os buscadores de verdade não fazem isso: usam o índice invertido para olhar só os candidatos. Com o índice, a sua Busca 3 funciona como eles. **Escreva no diário o que você viu no código da biblioteca**: isso vai para Materiais e Métodos e explica os tempos da Sprint 7.

Acrescente o bloco `if __name__ == "__main__":` igual ao das outras buscas e teste com `python -m buscadores.busca3_python`.

**4. Tome as duas decisões pela medição.** Primeiro a ordem (com 2 repetições do nome), depois as repetições (com a ordem vencedora). Mude os valores padrão de `montar_indice` entre uma rodada e outra:

```
python avaliar.py buscadores.busca3_python busca3_ordemA_rep2
python avaliar.py buscadores.busca3_python busca3_ordemB_rep2
python avaliar.py buscadores.busca3_python busca3_ordem?_rep1
python avaliar.py buscadores.busca3_python busca3_ordem?_rep3
```

(troque o `?` pela ordem vencedora). Monte as tabelas no diário e escolha pelo número, com o mesmo critério da Sprint 4 (P@5, e o MRR no desempate). Olhe também a P@5 **por categoria** de cada ordem: em quais categorias a ordem fez diferença? É um achado pequeno, mas original, e cabe em um parágrafo dos Resultados.

**5. Meça a versão escolhida.** Deixe os valores vencedores como padrão e rode com o rótulo definitivo:

```
python avaliar.py buscadores.busca3_python busca3_v1_radical
```

**6. Compare as três.** Atualize no diário as duas tabelas da Sprint 4 (geral e por categoria) com a coluna da Busca 3. Investigue:

- a Busca 3 ganhou na categoria `plural`? Se ganhou, você acabou de medir o efeito do *stemming*, isoladamente;
- e no `erro_digitacao`? E no `sinonimo`? (Ainda não devem ter melhorado: são a Sprint 6.)
- houve alguma categoria em que a Busca 3 ficou **pior** que a Busca 2? Se houve, abra as consultas no `qualidade.csv` e descubra por quê.

Preencha também, no diário, a tabela que vai virar uma figura do artigo:

| Peça | Conceito | O que resolve | O MySQL faz? |
|---|---|---|---|
| `separar_palavras` | tokenização | quebrar a frase em palavras | |
| `sem_acento` | normalização | "informatica" casar com "informática" | |
| `PALAVRAS_VAZIAS` | *stop words* | "de", "para", "curso" não distinguem nada | |
| `RADICALIZADOR` | *stemming* | "eletricistas" casar com "eletricista" | |
| `INDICE` | índice invertido | olhar só os cursos que têm alguma palavra da busca | |

A coluna da direita você preenche com o que descobriu nas Sprints 1 e 4 (sim, não, ou "só com configuração").

**7. Acrescente ao `testes/testar_buscas.py`** as conferências da Busca 3:

1. o mesmo combinado das outras duas (lista, no máximo 20, códigos `FICnnn`, sem repetição), para as 30 consultas;
2. `preparar("Curso de Eletricistas")` é igual a `preparar("eletricista")`;
3. `preparar("de para com")` é lista vazia;
4. buscar duas vezes o mesmo termo devolve **exatamente** a mesma lista (a ordem não pode variar);
5. todo código devolvido pela Busca 3 existe no banco.

Atualize o `README.md` e o diário, faça os *commits* por assunto e abra o PR com `Closes #9`.

### Como saber que deu certo

- `preparar("Curso de Eletricistas")` devolve um radical só.
- `python -m buscadores.busca3_python`, digitando `eletricistas`, devolve cursos de eletricista.
- `python -m testes.testar_buscas` mostra `Tudo certo: buscas conferidas.`, agora com a Busca 3.
- O diário tem a decisão da ordem, a das repetições e a tabela das três buscas.

### Entrega da sprint

- [ ] `separar_palavras`, `sem_acento`, `PALAVRAS_VAZIAS` e `preparar` escritas e testadas separadamente.
- [ ] Índice invertido e modelo BM25 montados a partir dos dados do MySQL.
- [ ] `buscar()` usando o índice invertido e `get_batch_scores`, com desempate pelo código.
- [ ] Ordem A × B e repetições do nome (1, 2, 3) medidas e escolhidas pelo número.
- [ ] Busca 3 medida com o rótulo `busca3_v1_radical`.
- [ ] Tabelas das três buscas e tabela "peça × o MySQL faz?" no diário.
- [ ] O que você leu no código da `rank_bm25` anotado no diário.
- [ ] `testes/testar_buscas.py` com as conferências da Busca 3, terminando com `Tudo certo`.
- [ ] PR aberto com `Closes #9`.

### Erros comuns

- **A Busca 3 vem pior que a Busca 2 em tudo:** confira, nesta ordem, (a) se a lista está ordenada da maior nota para a menor; (b) se o `preparar()` é o mesmo (e na mesma ordem) para os cursos e para a consulta; (c) se a lista de palavras vazias não está jogando fora algo importante. Se ainda assim vier pior, **isso é um resultado legítimo**: **não mexa no gabarito**, e leve os números para a reunião semanal.
- **`AssertionError` dentro do `get_batch_scores`:** alguma posição de candidato é maior que o número de cursos. O `INDICE` foi montado com posições de outra lista.
- **Toda busca devolve vazio:** a consulta preparada ficou vazia, ou os radicais da consulta não estão no `INDICE`. Imprima os dois e compare.

<a id="sprint-5-escrita"></a>
## Sprint 5 · Escrita: Metodologia e Materiais e Métodos (Entrega 4)

**Prazo:** 19/11/2026

**O que você vai entregar:** as seções 3 e 4 do artigo, cerca de 3 a 4 páginas no total.

Metodologia e Materiais e Métodos dizem **como** o trabalho foi feito, com detalhe suficiente para outra pessoa repetir. Verbos no passado e linguagem impessoal ("foram elaboradas 30 consultas"). O que ainda não aconteceu (a correção de digitação, os sinônimos, a medição de tempo) você escreve **como planejado**, e completa com os valores reais na Sprint 6 e na revisão final.

**Pasta com metodologias prontas para consulta:** https://drive.google.com/drive/folders/1OwAjk47aQWuRKLf-ktesizSax9csEtXO?usp=sharing

### 3.1 Classificação da pesquisa

**Pesquise:** Gil (2017) e Prodanov e Freitas (2013), com as referências completas em [`docs/orientacoes_escrita_tcc.md`](orientacoes_escrita_tcc.md). Leia os capítulos de classificação antes de escrever.

**Escreva:** a classificação pelos quatro critérios, **justificando cada uma** com uma frase que ligue o critério ao seu trabalho:

- **natureza:** aplicada, porque gera conhecimento para uma decisão concreta do iFIC, sobre o mesmo SGBD que a plataforma utiliza;
- **objetivos:** explicativa, porque busca relacionar a forma de busca adotada à qualidade dos resultados;
- **abordagem:** quantitativa, porque os resultados são notas numéricas, apoiadas por uma análise qualitativa dos erros;
- **procedimentos:** experimental, combinada com pesquisa bibliográfica. Você muda uma coisa (a forma de busca), mantém tudo o mais igual e observa o efeito nas notas.

Aproveite para **dizer quais são as variáveis**: o que você mudou (a forma de busca e, na Busca 3, cada recurso acrescentado), o que você mediu (P@5, revocação, MRR, tempo e espaço) e o que manteve fixo (catálogo, consultas, gabarito, limite de 20 resultados, servidor MySQL, máquina).

### 3.2 Perguntas de pesquisa

Enuncie as **três perguntas** da [seção 8.4](#escrita-geral), com as suas palavras. Os Resultados vão responder uma a uma, e a Conclusão também.

### 3.3 Desenho da comparação

**Escreva:** a lógica das **três buscas convivendo no mesmo sistema**: mesmo catálogo, mesmo servidor MySQL, mesmas consultas, mesma máquina, mesmo dia. Dedique um parágrafo a isso. Depois, as **padronizações** que tornam a comparação justa:

- o mesmo limite de 20 resultados;
- a mesma forma de resposta (lista ordenada de códigos), avaliada pelo mesmo script;
- o mesmo critério de desempate (o código do curso);
- o mesmo driver de acesso ao banco nas três buscas.

E explique a lógica de **acrescentar um recurso por vez** na Busca 3 (primeiro o radical, depois a correção de digitação, depois os sinônimos), medindo cada versão separadamente, e **por quê**: assim é possível atribuir o ganho a cada recurso. Se tudo entrasse de uma vez, você saberia que melhorou, mas não saberia por causa de quê.

Faça uma **figura** com o desenho do experimento (o catálogo no MySQL, as consultas, as três buscas, o gabarito, o script de avaliação e as notas), no draw.io (`app.diagrams.net`, funciona no navegador).

### 3.4 Coleção de teste

Subseção própria, porque a coleção **é** uma contribuição do trabalho. Descreva:

- **as consultas:** quantas, como foram elaboradas e o critério das seis categorias, com um quadro da distribuição. **Justifique as categorias**: cada uma corresponde a um fenômeno do Referencial (vocabulário, acentuação, erro de digitação, variação da palavra). As 30 consultas vão completas no Apêndice A;
- **o gabarito:** como foi montado, **o critério escrito**, e o fato de ter sido feito **antes** de rodar as buscas, explicando por quê;
- **a conferência:** a amostra de 10 consultas sorteadas, julgadas pelo segundo avaliador sem ver o seu gabarito, a concordância medida pelo coeficiente de Jaccard e os ajustes feitos;
- **a declaração ética:** não há participantes de pesquisa; o julgamento de relevância faz parte da construção do instrumento de medida; não há dado pessoal no catálogo (LGPD); logo, não há submissão ao Comitê de Ética.

### 4.1 Materiais e ambiente

Vale a analogia de [`docs/orientacoes_escrita_tcc.md`](orientacoes_escrita_tcc.md): **lista de ingredientes** mais **modo de preparo**. Para **cada** ferramenta, diga **o que é** (uma frase), **para que foi usada** e a **versão** (do `docs/ambiente.md`): Python, MySQL, o índice `FULLTEXT`, PyMySQL, `rank_bm25`, `snowballstemmer`, `difflib`, `matplotlib`, Django e Git. Uma tabela resolve.

**Três justificativas são obrigatórias** (estão na [seção 3](#decisoes) deste plano): por que MySQL; por que `PyMySQL`; e por que uma camada de busca em Python, e não uma ferramenta pronta, com o custo dessa escolha em generalização.

**A configuração do banco, sem a qual o artigo não é reproduzível:** a collation (e o que ela implica para os acentos), o `innodb_ft_min_token_size`, a lista de palavras vazias do servidor e o mecanismo de armazenamento (InnoDB). E o ambiente: processador, memória, sistema operacional, e se banco e aplicação rodam na mesma máquina. Registre também que os parâmetros do índice de texto do MySQL foram **mantidos no padrão**, que é a condição de uma plataforma em que ninguém mexeu na configuração.

### 4.2 O catálogo e as três buscas

**a) O catálogo:** quantos cursos, de onde vieram, quais campos, quantos eixos, **quantas ementas são do guia e quantas foram escritas ou completadas por você**. Uma figura com um curso completo ajuda o leitor a entender o que está sendo buscado.

**b) As três buscas:** um parágrafo por busca, dizendo **exatamente** o que foi feito, com um trecho curto de SQL ou de código quando ele esclarecer:

- **Busca 1:** o `LIKE` sobre nome e ementa, com ordenação alfabética;
- **Busca 2:** os dois índices `FULLTEXT` e **por que foram separados**, o modo de linguagem natural, a fórmula de combinação e **o peso escolhido para o nome, com a tabela da escolha**;
- **Busca 3:** a preparação do texto (com a **ordem escolhida e a tabela da escolha**), o índice invertido, o BM25 calculado só para os candidatos, a repetição do nome (com o número escolhido), e, **como planejado**, a correção de digitação e os sinônimos (você completa com os valores na Sprint 6).

Seja preciso. "As palavras foram reduzidas ao radical com o algoritmo Snowball para português" é informação reproduzível; "o texto foi tratado adequadamente" não é.

### 4.3 Como as notas, o tempo e o espaço foram medidos

- **as notas:** o script de avaliação lê as consultas, chama cada busca, compara com o gabarito e calcula P@5, revocação e RR, gravando uma linha por consulta; as notas de qualidade não variam entre execuções, então foram calculadas uma vez, na rodada oficial;
- **o tempo (como planejado):** 6 execuções por consulta, descartando a primeira (aquecimento) e usando a mediana das outras cinco; três tamanhos de catálogo; o tempo de montagem do índice da Busca 3 medido à parte; e que **nos catálogos ampliados só se mede tempo**, porque o gabarito não vale para eles;
- **o espaço (como planejado):** o tamanho dos índices no MySQL e a memória ocupada pelo índice da Busca 3.

### Entrega

- [ ] Seções 3.1 a 3.4, com a figura do desenho do experimento.
- [ ] Seções 4.1 a 4.3, com as três justificativas e a configuração do banco.
- [ ] Tabelas das escolhas (peso do nome, ordem, repetições) em 4.2.
- [ ] Apêndice A com as 30 consultas.
- [ ] Comentários da Entrega 3 respondidos e resolvidos.
- [ ] Versão nomeada no histórico: `Entrega 4 - Metodologia e Materiais e Métodos - 19/11`.

Para entregar, comente na *issue* com o nome da versão e mova o card para **Em revisão**.

---

# Sprint 6: 20/11 a 26/11/2026

<a id="sprint-6-dev"></a>
## Sprint 6 · Desenvolvimento: Busca 3, erro de digitação e sinônimos

**Branch:** `feature/busca3-correcao-sinonimos` · **No PR:** `Closes #11`

**O que você vai entregar:** a Busca 3 corrigindo o que a pessoa digitou errado e entendendo termos populares, e a medição do efeito de cada um desses dois recursos, **separadamente**, nas quatro versões da Busca 3.

**A ideia, em uma frase:** antes de buscar, olhar cada palavra digitada e perguntar "existe alguma palavra parecida no meu catálogo?"; se existir, trocar.

**Atenção:** sexta, 20/11, é feriado. A semana começa na segunda.

**Divida a semana assim:**

| Dia | O que fazer |
|---|---|
| segunda, 23/11 | passos 1 e 2 (vocabulário e correção) |
| terça, 24/11 | passos 3 e 4 (sinônimos e a nova `buscar`) |
| quarta, 25/11 | passos 5 e 6 (as quatro versões e a análise) |
| quinta, 26/11 | passo 7 (testes, diário e PR) e a escrita da semana |

### Passo a passo

**1. O vocabulário do catálogo.** Você já tem: são as **chaves do `INDICE`**, ou seja, todos os radicais que existem nos cursos. Guarde em uma variável global `VOCABULARIO`, como **lista ordenada**, montada no fim do `montar_indice`.

**2. Escreva `corrigir(radicais, corte=0.8)`.** Para cada radical da consulta:

- se ele **está** no vocabulário, passa sem alteração;
- se tem **menos de 4 letras**, passa sem alteração (uma letra de diferença em palavra curta muda o sentido: "mala" e "mola" são coisas diferentes);
- senão, procura o radical **mais parecido** do vocabulário com `difflib.get_close_matches(radical, VOCABULARIO, n=1, cutoff=corte)`; se achar, troca; se não achar, mantém.

Devolve a lista corrigida. O `difflib` **já vem com o Python**.

Três decisões neste código, e as três vão para o artigo:

- **o `corte`** é o quanto duas palavras precisam ser parecidas (de 0 a 1) para serem trocadas. Valor baixo demais troca palavras que não deviam ser trocadas; alto demais não corrige nada. Você vai **testar 0,7, 0,8 e 0,9** no passo 5;
- **palavras curtas não são corrigidas**, pelo motivo acima. Buscadores profissionais fazem o mesmo;
- **compara com o vocabulário do catálogo**, e não com um dicionário de português, porque o que interessa não é se a palavra existe, é se ela **existe nos seus cursos**. E compara **radicais**, porque é isso que está no índice.

> **Um cuidado de precisão para o artigo:** o `difflib` **não** calcula a distância de Levenshtein. Ele usa outra medida de semelhança (a razão do `SequenceMatcher`, baseada no algoritmo de Ratcliff e Obershelp). *Pesquise:* "difflib SequenceMatcher ratio" e compare, em duas linhas no diário, com a distância de Levenshtein. No artigo, você apresenta a distância de edição como conceito (Referencial) e diz **exatamente** qual medida usou (Materiais e Métodos). **E registre que o MySQL não oferece nada equivalente**: é a diferença mais visível entre as duas abordagens.

Teste no terminal: `corrigir(preparar("exel"))` deve virar o radical de "excel" (se houver Excel no seu catálogo).

**3. Escreva os sinônimos, em `dados/sinonimos.csv`:**

```
termo_popular,termo_catalogo
faxina,domésticos
```

O `termo_catalogo` é uma palavra **que existe no catálogo**, escrita normalmente (não o radical). No `busca3_python.py`, escreva `carregar_sinonimos()`, que lê o arquivo e monta um dicionário `{radical do termo popular: lista de radicais do termo do catálogo}`, passando os dois lados pelo `preparar`. Assim o radical certo sai sozinho, e você não precisa adivinhar como o radicalizador corta cada palavra.

Depois, `aplicar_sinonimos(radicais)`: para cada radical da consulta, se ele é uma chave do dicionário, **troca** pelos radicais do termo do catálogo; senão, mantém. (Trocar, e não acrescentar, porque o termo popular, por definição, não existe no catálogo: mantê-lo não ajuda em nada.)

> **Cuidado sério, e isto conta no artigo:** é tentador cadastrar exatamente as palavras das suas 5 consultas da categoria `sinonimo`. Isso é ajustar o buscador ao gabarito, e invalida a comparação. **Monte a lista pensando no domínio**: percorra os **eixos** do catálogo, um por um, e para cada eixo pense em 1 ou 2 termos populares que o público dos cursos FIC usaria para aquele tipo de curso. Limite-se a **10 a 15 entradas**. Só **depois** de pronta a lista, confira quantas das 5 consultas de sinônimo ela cobre, e **relate esse número** no artigo, com as notas com e sem sinônimos. Apresentar as duas é o que torna o resultado honesto.

**4. Reescreva `buscar` com os dois recursos opcionais:**

```python
def buscar(termo, limite=20, usar_correcao=True, usar_sinonimos=True):
    # 1. preparar o termo
    # 2. se usar_sinonimos: aplicar os sinônimos
    # 3. se usar_correcao: corrigir os radicais que não estão no vocabulário
    # 4. daqui em diante, igual à Sprint 5: candidatos pelo INDICE,
    #    notas com get_batch_scores, ordenação com desempate, os primeiros `limite`
```

Os sinônimos vêm **antes** da correção de propósito: senão, a correção tentaria "consertar" `faxina`, que não existe no catálogo, trocando-a por alguma palavra parecida e errada.

**5. Meça as versões separadamente: é a parte mais importante da sprint.**

Primeiro o corte. Crie um arquivo de três linhas por versão, que chama a busca com os parâmetros certos. Por exemplo, `buscadores/busca3_v2.py`:

```python
from buscadores.busca3_python import buscar as buscar_completo

def buscar(termo, limite=20):
    return buscar_completo(termo, limite, usar_correcao=True, usar_sinonimos=False)
```

Com o `busca3_v2.py`, teste o corte 0,7, 0,8 e 0,9 (mude o valor padrão de `corrigir` entre uma rodada e outra), com os rótulos `busca3_corte07`, `busca3_corte08` e `busca3_corte09`. Escolha pelo número, como nas Sprints 4 e 5.

Depois, com o corte escolhido, meça as quatro versões:

| Versão | Arquivo | Correção | Sinônimos | Rótulo |
|---|---|---|---|---|
| 3.1 | `busca3_v1.py` | não | não | `busca3_v1_radical` |
| 3.2 | `busca3_v2.py` | **sim** | não | `busca3_v2_correcao` |
| 3.3 | `busca3_v3.py` | não | **sim** | `busca3_v3_sinonimos` |
| 3.4 | `busca3_v4.py` | **sim** | **sim** | `busca3_v4_completa` |

A versão 3.1 já foi medida na Sprint 5. Meça de novo com o `busca3_v1.py`: **os números têm de ser idênticos** aos da Sprint 5. Se não forem, alguma coisa mudou no caminho (a ordem, as repetições, a lista de palavras vazias): descubra o quê antes de seguir. Essa conferência é o que garante que as diferenças entre as versões vêm dos recursos novos, e não de outra coisa.

**Por que medir separadamente?** Porque assim você consegue dizer **quanto cada recurso rendeu sozinho**. Essa é a diferença entre um trabalho que descreve e um trabalho que explica.

**6. Olhe o que mudou e procure onde a sua solução falha.**

- Monte no diário a tabela de **P@5 por categoria** com a Busca 1, a Busca 2 e as quatro versões da Busca 3. **Essa tabela é a figura principal do artigo.**
- Em quais categorias a correção fez diferença? E os sinônimos? A correção estragou alguma categoria que já funcionava?
- **Procure um caso em que a correção ESTRAGOU o resultado.** Compare, no `qualidade.csv`, a P@5 da versão 3.2 com a da 3.1, consulta por consulta. Se alguma piorou, descubra qual palavra foi trocada, e por qual. Se nenhuma das 30 piorou, invente 5 consultas extras (fora do gabarito, só para investigar) até achar uma troca errada, e documente. Mostrar onde a sua própria solução falha é o que impede o artigo de parecer propaganda, e é exatamente o que um avaliador procura.

**7. Acrescente ao `testes/testar_buscas.py`:**

1. o combinado (lista, no máximo 20, códigos `FICnnn`, sem repetição) para as quatro versões;
2. `corrigir` não altera um radical que está no vocabulário;
3. `corrigir` não altera uma palavra com menos de 4 letras;
4. a versão 3.4 encontra `"informatica basica"` nos **mesmos cursos** que a versão 3.1 (a correção não pode estragar o que já funcionava).

Atualize o `README.md` e o diário, faça os *commits* por assunto e abra o PR com `Closes #11`.

### Como saber que deu certo

- A versão 3.2, buscando `exel`, devolve cursos com Excel.
- A versão 3.3, buscando `faxina`, devolve cursos de serviços domésticos (se `faxina` estiver na sua lista).
- A versão 3.1 medida de novo deu **exatamente** as mesmas notas da Sprint 5.
- `python -m testes.testar_buscas` mostra `Tudo certo: buscas conferidas.`
- O diário tem a tabela de P@5 por categoria com as seis colunas e o caso de falha da correção.

### Entrega da sprint

- [ ] `corrigir` funcionando, com o corte testado em 0,7, 0,8 e 0,9 e escolhido pelo número.
- [ ] `dados/sinonimos.csv` com 10 a 15 entradas, montado pelos eixos, e a cobertura das 5 consultas de sinônimo anotada.
- [ ] `buscar` com `usar_correcao` e `usar_sinonimos`, sinônimos antes da correção.
- [ ] As quatro versões medidas, e a 3.1 conferida com a Sprint 5.
- [ ] Tabela de P@5 por categoria (Busca 1, Busca 2 e as quatro versões) no diário.
- [ ] Pelo menos um caso em que a correção errou, documentado.
- [ ] Diferença entre o `difflib` e a distância de Levenshtein anotada no diário.
- [ ] `testes/testar_buscas.py` com as novas conferências, terminando com `Tudo certo`.
- [ ] PR aberto com `Closes #11`.

<a id="sprint-6-escrita"></a>
## Sprint 6 · Escrita: colocar no documento as tabelas de qualidade

**Prazo:** 26/11/2026

**O que você vai entregar:** as tabelas de qualidade já dentro do documento, nos lugares certos dos Resultados, e Materiais e Métodos completo com os valores da Sprint 6. Nesta semana não há entrega de seção nova: é a tarefa que impede os Resultados de ficarem para a última hora.

### Passo a passo

**1. Crie no documento os títulos da seção 5** (5.1 a 5.7, como na [seção 8.3](#escrita-geral)), ainda sem texto.

**2. Monte a Tabela "Qualidade geral das buscas"** em 5.2: uma linha por busca (Busca 1, Busca 2 e as quatro versões da Busca 3), colunas P@5, revocação e MRR. Use **vírgula** como separador decimal e o **mesmo número de casas** (duas) em todas as colunas. Identificação em cima, centralizada; fonte embaixo ("Fonte: dados da pesquisa (2026)."), como em [`docs/orientacoes_escrita_tcc.md`](orientacoes_escrita_tcc.md).

**3. Monte a Tabela "P@5 por categoria de consulta"** em 5.3: seis linhas (as categorias) e as colunas das buscas. É a tabela do passo 6 da Sprint 6 dev.

**4. Monte, em 5.1, o quadro da distribuição** das 30 consultas por categoria e os números do catálogo (cursos, eixos, ementas do guia e próprias), e o resultado da conferência com o Entony (concordância média).

**5. Escreva só uma frase** antes de cada tabela, anunciando-a ("A Tabela X apresenta..."). A discussão vem na Sprint 7. Deixe uma nota no documento: "valores provisórios: conferir com a rodada oficial".

**6. Complete a seção 4.2** com o que foi decidido nesta sprint: a medida de semelhança do `difflib`, o corte escolhido (com a tabela), o limite de 4 letras, o número de sinônimos, o critério de montagem pelos eixos e a ordem "sinônimos antes da correção", com o porquê.

### Entrega

- [ ] Títulos 5.1 a 5.7 no documento.
- [ ] Tabelas de qualidade geral e por categoria, com identificação, fonte e vírgula decimal.
- [ ] Quadro das consultas, números do catálogo e concordância do gabarito em 5.1.
- [ ] Seção 4.2 completa com os valores da Sprint 6.
- [ ] Comentários da Entrega 4 respondidos e resolvidos.
- [ ] Versão nomeada no histórico: `Sprint 6 - tabelas de qualidade - 26/11`.

Para entregar, comente na *issue* com o nome da versão e mova o card para **Em revisão**.

---

# Sprint 7: 27/11 a 03/12/2026

<a id="sprint-7-dev"></a>
## Sprint 7 · Desenvolvimento: rodada oficial, tempo, espaço, gráficos e análise de erros

**Branch:** `feature/medicoes-finais` · **No PR:** `Closes #13`

**O que você vai entregar:** a rodada oficial de qualidade e de tempo, feita toda no mesmo dia e na mesma máquina; o tempo em três tamanhos de catálogo; o espaço dos índices; a demonstração do problema de sincronização; os três gráficos do artigo; e a análise dos erros.

É nesta semana que o trabalho deixa de ser "três buscas programadas" e passa a ser um artigo com achado.

**Atenção ao calendário:** os Resultados vencem na quinta, 03/12. **A rodada oficial e os gráficos precisam estar prontos até segunda, 30/11.**

**Divida a semana assim:**

| Dia | O que fazer |
|---|---|
| sexta, 27/11 | passos 1 a 4 (catálogos ampliados, rodada oficial de qualidade e de tempo) |
| segunda, 30/11 | passos 5 e 6 (espaço e gráficos) |
| terça, 01/12 | passos 7 e 8 (sincronização e análise de erros) |
| quarta e quinta, 02 e 03/12 | escrita dos Resultados; passo 9 (diário e PR) |

### Passo a passo

**1. Prepare os catálogos ampliados.** Para responder "e quando o catálogo crescer?", você vai medir o tempo em três tamanhos: o catálogo original, 10 vezes maior e 40 vezes maior (mais ou menos 10.000 cursos).

**a)** No `banco.py`, acrescente uma variável do módulo `NOME_BANCO`, que começa com o valor de `BANCO["database"]`, e uma função `usar_banco(nome)` que a troca. O `conectar()` passa a usar `NOME_BANCO` no lugar do `"database"` do `config.py`. Assim, um programa pode mudar de banco no meio da execução.

**b)** No `criar_banco.py`, acrescente dois parâmetros de linha de comando, com `argparse`: `--banco` (padrão `ific_busca`) e `--multiplicar` (padrão `1`). Com `--multiplicar 10`, cada curso é inserido 10 vezes, com o código seguido de um sufixo (`FIC001_01`, `FIC001_02`, ...). O resto (tabela, índices `FULLTEXT`) é igual. *Pesquise:* `argparse.ArgumentParser` e `add_argument` com `type=int`.

```
python criar_banco.py
python criar_banco.py --banco ific_busca_x10 --multiplicar 10
python criar_banco.py --banco ific_busca_x40 --multiplicar 40
```

> **Não calcule notas nos catálogos ampliados.** O gabarito não vale para eles (os códigos com sufixo não estão no gabarito, e os cursos repetidos não existem de verdade). Ali só se mede tempo. Diga isso no artigo, senão parece esquecimento.

**2. Rodada oficial de qualidade.** Acrescente ao `avaliar.py` um terceiro argumento opcional, o arquivo de destino (padrão: `resultados/qualidade.csv`). Feche o navegador e todos os outros programas e rode as seis avaliações, **em sequência, no mesmo dia**:

```
python avaliar.py buscadores.busca1_like busca1_like resultados/oficial_qualidade.csv
python avaliar.py buscadores.busca2_fulltext busca2_fulltext resultados/oficial_qualidade.csv
python avaliar.py buscadores.busca3_v1 busca3_v1_radical resultados/oficial_qualidade.csv
python avaliar.py buscadores.busca3_v2 busca3_v2_correcao resultados/oficial_qualidade.csv
python avaliar.py buscadores.busca3_v3 busca3_v3_sinonimos resultados/oficial_qualidade.csv
python avaliar.py buscadores.busca3_v4 busca3_v4_completa resultados/oficial_qualidade.csv
```

Confira: as notas têm de ser **iguais** às das Sprints 4 a 6 (as buscas são determinísticas). Se alguma for diferente, descubra por quê antes de seguir: é a prova de que nada mudou no caminho. **É essa rodada que vai para o artigo.**

**3. Escreva `medir_tempo.py`.** Tempo de computador varia a cada execução: um número só não significa nada. O programa:

1. para cada banco (`ific_busca`, `ific_busca_x10`, `ific_busca_x40`): chama `usar_banco`, conta os cursos e **monta de novo o índice da Busca 3** (chamando o `montar_indice` dela), medindo quanto tempo isso levou;
2. para cada uma das três buscas (Busca 1, Busca 2 e a versão 3.4 da Busca 3) e para cada uma das 30 consultas: roda a busca **6 vezes**, mede cada execução com `time.perf_counter()`, **descarta a primeira** e calcula a **mediana** e o **desvio padrão** das outras cinco;
3. grava uma linha por banco, busca e consulta em `resultados/oficial_tempos.csv`, com as colunas `data_hora`, `banco`, `n_cursos`, `busca`, `id_consulta`, `mediana_ms`, `desvio_ms`;
4. grava o tempo de montagem do índice da Busca 3 de cada banco em `resultados/oficial_montagem.csv` (`banco`, `n_cursos`, `tempo_montagem_s`);
5. no fim, mostra uma tabela resumida: para cada banco e busca, a **mediana das 30 medianas**.

*Pesquise:* `statistics.median`, `statistics.stdev`, e por que o `time.perf_counter()` é melhor que o `time.time()` para medir intervalos curtos.

Três coisas para explicar no artigo (escreva no diário agora):

- **por que descartar a primeira:** a primeira execução ainda está abrindo caminhos que as seguintes encontram prontos. O MySQL, por exemplo, mantém páginas de dados na memória (o *buffer pool*), e a primeira consulta é a mais lenta. Isso se chama **aquecimento**;
- **por que mediana, e não média:** a mediana não é distorcida por uma execução esquisita, que acontece quando o Windows resolve fazer outra coisa no meio da medição;
- **o mesmo procedimento nas três buscas.** As Buscas 1 e 2 abrem uma conexão com o MySQL a cada chamada, e isso entra no tempo medido. É uma limitação, mas é **igual para as duas**, e a comparação é relativa. A Busca 3 não abre conexão para buscar, porque o índice já está na memória: isso também é parte do resultado.

**4. Rode a medição de tempo** no mesmo dia da rodada oficial de qualidade, com o navegador e os outros programas fechados. Anote no diário a data, o horário de início e de fim, e a máquina (deve ser a do `docs/ambiente.md`).

**5. Meça o espaço, em `medir_espaco.py`.**

**a) Os índices no MySQL.** Para cada um dos três bancos, rode, nesta ordem:

```sql
SET SESSION information_schema_stats_expiry = 0;
ANALYZE TABLE cursos;
SELECT table_name, data_length, index_length
FROM information_schema.tables
WHERE table_schema = %s AND table_name = 'cursos';
```

O primeiro comando é necessário porque, no MySQL 8, os tamanhos do `information_schema` ficam guardados em *cache* por até 24 horas; sem ele, você poderia ler um número velho. *Pesquise:* `information_schema_stats_expiry`.

O índice `FULLTEXT` do InnoDB não fica todo dentro do `index_length`: ele é guardado em **tabelas auxiliares internas**. Tente também:

```sql
SELECT NAME, FILE_SIZE
FROM INFORMATION_SCHEMA.INNODB_TABLESPACES
WHERE NAME LIKE 'ific_busca/fts%';
```

(troque `ific_busca` pelo nome de cada banco). Se der erro de permissão, ou se os números não fizerem sentido, **não invente**: registre o que observou e diga no artigo que o espaço do índice de texto não pôde ser medido com precisão, e por quê. Relatar uma medição que não deu certo, explicando o motivo, é ciência; forçar um número é o contrário.

**b) A memória da Busca 3.** Meça quanta memória o Python usa para montar o índice da Busca 3, em cada um dos três bancos, com o módulo `tracemalloc`: inicie o rastreamento, chame `montar_indice`, leia o **pico** de memória e pare o rastreamento. *Pesquise:* `tracemalloc.start`, `tracemalloc.get_traced_memory` e `tracemalloc.stop`. **Meça a memória em uma execução separada da medição de tempo**, porque o `tracemalloc` deixa o programa mais lento.

Escreva tudo em `resultados/espaco.md`, em uma tabela: banco, número de cursos, `data_length`, `index_length`, tamanho das tabelas auxiliares do `FULLTEXT` (ou "não medido", com o motivo) e pico de memória da Busca 3.

**6. Faça os gráficos por script, em `graficos.py`.** Gráfico feito por script é reproduzível; print de planilha não é. O programa lê os arquivos `oficial_*` e gera três figuras em `graficos/`:

| Arquivo | Gráfico | O que mostra |
|---|---|---|
| `g1_p5_geral.png` | barras: a P@5 média de cada busca (as seis) | a figura que resume o trabalho |
| `g2_p5_categoria.png` | barras agrupadas: seis grupos (as categorias), com uma barra por busca (Busca 1, Busca 2 e versão 3.4) | **a figura mais importante do artigo**: mostra *onde* cada busca ganha |
| `g3_tempo_tamanho.png` | linhas: número de cursos no eixo horizontal, mediana do tempo no vertical, uma linha por busca | como o tempo cresce com o catálogo |

Cuidados:

- **não coloque título dentro da imagem.** Pela ABNT, o título vai no documento, em cima da figura;
- escreva o nome de cada eixo, com a unidade (`Tempo (ms)`, `Número de cursos`);
- a P@5 vai de 0 a 1: fixe o eixo vertical de 0 a 1 nos gráficos 1 e 2;
- use **vírgula decimal** nos números dos eixos (*pesquise:* `matplotlib.ticker.FuncFormatter`);
- no gráfico 3, se as linhas ficarem muito distantes (uma em 1 ms, outra em 200 ms), use **escala logarítmica** no eixo vertical (`plt.yscale("log")`) e **avise na legenda da figura**;
- salve com `dpi=200` e `bbox_inches="tight"`.

*Pesquise:* `plt.bar` e barras agrupadas com `numpy.arange` e um deslocamento para cada busca ("matplotlib grouped bar chart"); `plt.plot` com `marker="o"`; `plt.legend`; `plt.savefig`.

**7. Demonstre o problema de sincronização.** Na Sprint 5 você leu que o índice da Busca 3 fica desatualizado quando o banco muda. Agora, prove. Escreva `demonstrar_sincronizacao.py`, que:

1. importa a Busca 2 e a Busca 3 (o índice da Busca 3 é montado nesse momento);
2. escolhe um curso e, por `UPDATE`, acrescenta na ementa dele uma palavra que não existe no catálogo (por exemplo, `drone`), com `commit`;
3. busca `drone` na Busca 2 e na Busca 3, e mostra o que cada uma devolveu;
4. chama o `montar_indice` da Busca 3 e busca `drone` de novo;
5. desfaz a alteração (`UPDATE` de volta, com `commit`).

Guarde a saída em `docs/evidencias/`. O que você deve observar: a Busca 2 encontra o curso **na hora**, porque o índice vive dentro do banco e é atualizado junto com os dados; a Busca 3 só encontra **depois** de o índice ser montado de novo. **Este é o argumento mais forte a favor de ficar no banco**, e ele é invisível em qualquer comparação que meça só tempo e precisão.

**8. Faça a análise dos erros, em `docs/analise_erros.md`.** É aqui que está o valor do trabalho. Pegue, no `oficial_qualidade.csv`, as **10 consultas com pior P@5** da Busca 1, da Busca 2 e da versão 3.4 da Busca 3, e responda, para cada uma, **por quê**. Para cada consulta, rode a busca e olhe os nomes dos cursos que voltaram. Monte uma tabela assim:

| Consulta | Categoria | Busca | O que devolveu | Por quê |
|---|---|---|---|---|
| `exel` | erro_digitacao | 1 e 2 | nada | nenhuma das duas tolera erro de digitação |
| (a sua) | | | | |

Cada "por quê" usa um **conceito do seu Referencial** (ausência de ordenação por relevância, ausência de *stemming*, palavra abaixo do tamanho mínimo indexado, palavra fora do vocabulário do catálogo, palavra frequente com IDF baixo, troca errada pela correção, o radical que não junta "costura" e "costureiro"). É assim que Resultados e Referencial se amarram.

**Inclua obrigatoriamente:** pelo menos **um caso em que a Busca 3 perdeu** (você já encontrou um na Sprint 6) e pelo menos **um caso em que a Busca 1 já bastava**. Mostrar os dois é o que dá credibilidade ao resto.

**9. Feche a sprint.** Atualize o `README.md` (como gerar os catálogos ampliados, medir o tempo e o espaço e gerar os gráficos), escreva o diário, faça os *commits* por assunto e abra o PR com `Closes #13`. Em **Evidências de teste**, cole a saída das três verificações, a tabela resumida de tempos e os três gráficos.

### Como saber que deu certo

- O `oficial_qualidade.csv` tem 180 linhas, com as mesmas notas das Sprints 4 a 6.
- O `oficial_tempos.csv` tem 270 linhas (3 bancos × 3 buscas × 30 consultas).
- Os três gráficos estão em `graficos/`, gerados pelo `graficos.py`, sem título dentro da imagem.
- O `espaco.md` tem a tabela completa (ou a explicação do que não pôde ser medido).
- A saída da demonstração de sincronização mostra a Busca 3 sem achar `drone` antes de remontar o índice.
- A tabela de erros está pronta, com pelo menos uma falha da Busca 3 e um caso em que a Busca 1 bastou.

### Entrega da sprint

- [ ] Catálogos ampliados (10× e 40×) criados pelo `criar_banco.py`.
- [ ] Rodada oficial de qualidade feita, conferida com as sprints anteriores.
- [ ] `medir_tempo.py` com 6 repetições, descarte da primeira, mediana e desvio, nos três tamanhos.
- [ ] Tempo de montagem e pico de memória do índice da Busca 3 medidos.
- [ ] Espaço dos índices do MySQL medido (ou a impossibilidade registrada) em `resultados/espaco.md`.
- [ ] Demonstração da sincronização guardada em `docs/evidencias/`.
- [ ] `graficos.py` gerando os três gráficos.
- [ ] `docs/analise_erros.md` completo.
- [ ] PR aberto com `Closes #13`.

### Erros comuns

- **Tempos muito diferentes entre duas rodadas:** algum programa estava aberto, ou a máquina é outra. Refaça as duas no mesmo dia, nas mesmas condições, e anote.
- **`Access denied; you need (at least one of) the PROCESS privilege(s)`:** o seu usuário não pode ler o `INNODB_TABLESPACES`. Registre isso no `espaco.md` e siga com o `information_schema.tables`.
- **A Busca 3 encontra cursos `FIC001_03` no catálogo original:** o índice foi montado no banco ampliado e não foi remontado ao voltar. Remonte depois de cada `usar_banco`.

<a id="sprint-7-escrita"></a>
## Sprint 7 · Escrita: Resultados e Discussão (Entrega 5)

**Prazo:** 03/12/2026

**O que você vai entregar:** a seção 5 completa, de 4 a 6 páginas. É a seção mais importante do artigo.

Troque os valores provisórios da Sprint 6 pelos da rodada oficial (se forem iguais, como devem ser, apague a nota "valores provisórios").

> **Regra sem exceção:** toda figura ou tabela é **anunciada no texto antes** de aparecer e **explicada depois**. Nada de duas figuras seguidas sem texto entre elas. Organize a seção respondendo às **três perguntas de pesquisa**, na ordem.

### 5.1 Catálogo e coleção de teste

Curta: os números do catálogo, o quadro das consultas por categoria e a concordância com o segundo avaliador. Isso você já montou na Sprint 6.

### 5.2 Qualidade geral das três buscas (pergunta 1)

A tabela de qualidade geral e o Gráfico 1. **Discuta:** qual busca venceu em cada nota, e se alguma nota discorda das demais. Um caso que pode acontecer: uma busca com **revocação alta e P@5 baixa**, que encontra os cursos certos mas não os coloca no topo. Se aparecer, explore: é a diferença entre **encontrar** e **ordenar**, e é exatamente o que separa o `LIKE` do `MATCH ... AGAINST`.

### 5.3 Qualidade por categoria de consulta (pergunta 2)

**A subseção central do artigo.** A tabela por categoria e o Gráfico 2. É aqui que o trabalho deixa de responder "qual é melhor" e passa a responder "**melhor para quê**". Discuta categoria por categoria, sempre com o **mecanismo**, não só o número:

- **exato:** provavelmente as três vão bem. **Diga isso.** Reconhecer onde a solução simples basta é informação útil para quem vai decidir;
- **genérico:** a separação em palavras e a ordenação por relevância;
- **sem acento:** a collation do MySQL, que ignora acentos de graça, e o que a ordem A ou B fez na Busca 3;
- **erro de digitação:** quanto a correção rendeu, a medida de semelhança usada e a ausência de recurso equivalente no MySQL;
- **plural:** o efeito do radical, medido isoladamente na versão 3.1, e o limite do radical ("costura" não junta com "costureiro");
- **sinônimo:** os dois números, com e sem a lista, a cobertura das 5 consultas pela lista, e o **custo escondido**: alguém precisa montar e manter essa lista, e isso é trabalho humano recorrente.

**Feche com a conclusão prática:** a diferença entre as abordagens **não é uniforme**, ela se concentra em categorias específicas. Portanto, a decisão de construir uma camada de busca deveria depender de **quanto** dessas consultas problemáticas o sistema realmente recebe.

### 5.4 Tempo de resposta e espaço (pergunta 3)

A tabela de tempos (mediana nos três tamanhos), o Gráfico 3, o tempo de montagem e a memória da Busca 3, e o espaço dos índices (ou a ressalva). **Discuta o crescimento** usando os `EXPLAIN` da Sprint 4: qual busca lê a tabela inteira e qual usa índice, e o que isso faz com o tempo quando o catálogo cresce. Ligue ao índice invertido do Referencial: resultado ligado à teoria vale o dobro.

**Não omita o outro lado.** Em um catálogo de poucas centenas de cursos, é bem possível que **as três respondam rápido o suficiente** para a pessoa não perceber diferença. Se for o caso dos seus dados, **diga com todas as letras**: no porte atual do catálogo de cursos FIC, o tempo **não** é o critério de decisão; a qualidade é. É uma conclusão contraintuitiva, sustentada por número, e é o tipo de achado que dá valor a um artigo.

### 5.5 Análise das falhas

A tabela de `docs/analise_erros.md` (resumida, com os casos mais representativos), com a causa **nomeada em termos do Referencial**. Destaque o caso em que a Busca 3 perdeu e o caso em que a Busca 1 bastou. Depois, a **demonstração da sincronização**: o que aconteceu com `drone` na Busca 2 e na Busca 3, e a consequência (a busca devolve resultado errado sem dar erro nenhum).

### 5.6 Quadro-síntese e recomendação para o iFIC

Um quadro com uma linha por busca e as colunas: qualidade geral, categorias em que se destaca, tempo, esforço de implementação, custo de manutenção e **recomendação de uso**. **Este quadro é a contribuição prática do seu trabalho**: é o que a equipe do iFIC vai olhar para decidir. E não fuja da recomendação: diga, com base nos seus números, o que você faria no lugar da equipe, e **sob que condição** a resposta mudaria.

### 5.7 Limitações

Curta e honesta:

- o gabarito foi feito pela pessoa que também construiu as buscas (atenuado pelo critério escrito, pelo julgamento antes de rodar as buscas e pela conferência de uma amostra);
- o catálogo é de porte modesto, e parte das ementas foi escrita para o trabalho;
- as consultas foram elaboradas, e não coletadas do uso real do sistema (a limitação mais relevante);
- os parâmetros (peso do nome, ordem, repetições, corte) foram escolhidos com as mesmas consultas usadas na comparação;
- a camada dedicada foi implementada em Python, por restrição do ambiente, e o MySQL foi mantido na configuração padrão.

Note que várias dessas limitações são atenuadas por o estudo ser **comparativo**: a mesma limitação incide sobre as três buscas. Diga isso, sem usar o argumento para esconder o resto.

### Entrega

- [ ] Seções 5.1 a 5.7, com os números da rodada oficial.
- [ ] Os três gráficos inseridos, cada um anunciado antes e explicado depois.
- [ ] As três perguntas de pesquisa respondidas, na ordem.
- [ ] Quadro-síntese com a recomendação explícita para o iFIC.
- [ ] Comentários da Sprint 6 respondidos e resolvidos.
- [ ] Versão nomeada no histórico: `Entrega 5 - Resultados - 03/12`.

Para entregar, comente na *issue* com o nome da versão e mova o card para **Em revisão**.

---

# Sprint 8: 04/12 a 10/12/2026

<a id="sprint-8-dev"></a>
## Sprint 8 · Desenvolvimento: página web, README e fechamento

**Branch:** `feature/pagina-fechamento` · **No PR:** `Closes #15`

**O que você vai entregar:** uma página simples em Django que mostra as três buscas lado a lado para o mesmo termo, o `README.md` completo e testado do zero, o repositório limpo e a apresentação.

A página é a ligação do seu trabalho com o iFIC, que é feito em Django: ela mostra a quem for decidir, na tela, a diferença que os números descrevem.

**Divida a semana assim:**

| Dia | O que fazer |
|---|---|
| sexta, 04/12 | passos 1 a 4 (projeto Django, consulta dos nomes, *view*) |
| segunda, 07/12 | passos 5 a 7 (página, teste e prints); a Conclusão do artigo tem de estar pronta hoje |
| terça, 08/12 | passos 8 e 9 (`README.md` e reprodução do zero) |
| quarta e quinta, 09 e 10/12 | passos 10 a 12 (limpeza, apresentação e PR) e o fechamento do texto |

### Passo a passo

**1. Instale o Django e crie o projeto.** Na raiz do repositório, com o `.venv` ativo:

```
pip install django
pip freeze > requirements.txt
django-admin startproject web
cd web
python manage.py startapp busca
```

> **Por que `web` e não `site`?** O Django recusa nomes de projeto iguais a módulos do Python, e `site` é um módulo do Python. Se tentar, aparece um erro dizendo que o nome conflita com um módulo existente.

**2. Configure o projeto**, em `web/web/settings.py`: acrescente `"busca"` em `INSTALLED_APPS`, troque `LANGUAGE_CODE` para `"pt-br"` e `TIME_ZONE` para `"America/Fortaleza"` (o fuso do Rio Grande do Norte).

**3. Acrescente ao `banco.py` a função `nomes_dos_cursos(codigos)`**, que recebe uma lista de códigos e devolve um dicionário `{codigo: nome}`. Ela usa um `SELECT codigo, nome FROM cursos WHERE codigo IN (...)`, com **um `%s` para cada código**. Você vai montar o texto `%s, %s, %s` com `", ".join(...)`: isso **não** é injeção de SQL, porque você gera só os marcadores, e os valores continuam indo como parâmetros. Se a lista vier vazia, devolva um dicionário vazio sem consultar o banco.

**4. Escreva a *view*, em `web/busca/views.py`.** Uma função `pagina(request)` que:

1. acrescenta a **raiz do repositório** ao `sys.path`, para conseguir importar o `banco.py` e a pasta `buscadores/`. A raiz fica três níveis acima do arquivo `views.py`. *Pesquise:* `pathlib.Path(__file__).resolve().parents`;
2. lê o termo digitado com `request.GET.get("q", "")`;
3. se houver termo, roda as três buscas (Busca 1, Busca 2 e a versão 3.4 da Busca 3), medindo o tempo de cada uma com `time.perf_counter()`, e busca os nomes dos cursos com `nomes_dos_cursos`;
4. chama `render(...)` com o template `busca/pagina.html`, passando o termo e, para cada busca, o rótulo, o tempo em milissegundos e a lista de cursos (código e nome).

Faça o `sys.path` e os *imports* dos buscadores **fora** da função, no topo do arquivo: assim o índice da Busca 3 é montado **uma vez**, quando o servidor sobe, e não a cada busca. É o mesmo comportamento que a plataforma teria.

**5. Escreva a página**, em `web/busca/templates/busca/pagina.html`: um formulário com **método GET**, um campo de texto chamado `q` e um botão; embaixo, **três colunas lado a lado**, uma por busca, cada uma com o rótulo, o tempo e uma lista numerada (`<ol>`) dos cursos. Se uma busca não encontrar nada, a coluna mostra "Nenhum curso encontrado". **Simples mesmo**: dez linhas de CSS no próprio arquivo bastam (*pesquise:* `display: grid` com `grid-template-columns`). O objeto do trabalho é a busca, não o visual.

Em `web/web/urls.py`, ligue a raiz (`""`) à *view* `pagina`. *Pesquise:* `django.urls.path`, `{% for %}` e `{% empty %}` nos templates do Django.

Rode, de dentro da pasta `web`:

```
python manage.py runserver
```

e abra `http://127.0.0.1:8000/` no navegador.

> Vai aparecer um aviso sobre migrações pendentes. **Pode ignorar**: esta página não usa os modelos do Django, ela conversa com o MySQL pelo `banco.py`. Se o aviso incomodar, rode `python manage.py migrate` uma vez: o Django cria as tabelas internas dele em um arquivo SQLite próprio (`web/db.sqlite3`, que já está no `.gitignore`), separado do seu catálogo.

**6. Escreva o teste da página**, em `web/busca/tests.py`, com o cliente de teste do Django: (a) a página sem termo responde com código 200; (b) a página com `?q=excel` responde com código 200 e o conteúdo contém o texto `Busca 1`, `Busca 2` e `Busca 3`. Rode com `python manage.py test busca`, de dentro da pasta `web`. *Pesquise:* `django.test.TestCase` e `self.client.get`.

**7. Tire os prints** das três buscas respondendo, lado a lado, a três consultas: `exel`, `faxina` e `informatica basica`. Guarde em `docs/evidencias/s08_pagina_exel.png` e assim por diante. Um deles vai para o artigo.

**8. Complete o `README.md`.** Ele precisa permitir que outra pessoa repita tudo. Escreva na ordem em que a pessoa faria:

1. o que precisa ter: Python 3.10 ou mais novo e acesso a um servidor MySQL 8 com permissão para criar bancos;
2. como criar o ambiente virtual e instalar (`pip install -r requirements.txt`);
3. como criar o `config.py` a partir do `config_exemplo.py`;
4. como criar o banco e os índices (`python criar_banco.py`), e os catálogos ampliados;
5. como testar cada busca;
6. como rodar os testes (os três de `testes/` e o da página);
7. como rodar a avaliação de qualidade, a medição de tempo e a de espaço;
8. como gerar os gráficos;
9. como abrir a página web;
10. o que tem em cada pasta, e os responsáveis.

**9. Teste o seu README do zero.** Clone o repositório **em outra pasta** (`git clone ... teste_readme`), apague os bancos (`DROP DATABASE ific_busca;` e os dois ampliados) e siga o seu texto, passo por passo, sem usar nada que não esteja escrito nele. Cada vez que você precisar de algo que não está no README, acrescente. É a única forma de saber que ele está completo. Anote no diário quanto tempo levou.

**10. Limpe o repositório.** Rode `git status` e confira: nada de `.venv/`, `__pycache__/`, `web/db.sqlite3` e, principalmente, **nada de `config.py`**. Apague arquivos de teste soltos que não fazem parte do trabalho.

**11. Monte a apresentação.** Dez minutos, de 8 a 10 slides no Google Apresentações, salvos na mesma pasta do Drive do artigo: o problema (com um exemplo real do seu catálogo), as três buscas, a coleção de teste, o Gráfico 2 (por categoria), a demonstração da sincronização, a tabela de erros e a recomendação para o iFIC.

**12. Abra o PR** com `Closes #15`, com a saída dos testes e um print da página. Depois do *merge*, os orientadores levam a `develop` para a `main` e publicam a versão `v1.0`.

### Como saber que deu certo

- A página abre no navegador e mostra as três buscas lado a lado, com o tempo de cada uma.
- `python manage.py test busca` termina com `OK`.
- Você conseguiu seguir o seu próprio `README.md` do zero, em outra pasta.
- O `git status` está limpo, e o `config.py` não está no repositório.

### Entrega da sprint

- [ ] Projeto `web` com o app `busca`, mostrando as três buscas lado a lado.
- [ ] `nomes_dos_cursos` no `banco.py`, com um `%s` por código.
- [ ] Teste da página passando.
- [ ] Prints de `exel`, `faxina` e `informatica basica` em `docs/evidencias/`.
- [ ] `README.md` completo e testado do zero em outra pasta.
- [ ] Repositório limpo, **sem o `config.py`**.
- [ ] Apresentação de 10 minutos na pasta do Drive.
- [ ] PR aberto com `Closes #15`.

### Erros comuns

- **`ModuleNotFoundError: No module named 'buscadores'` no Django:** o `sys.path` não está apontando para a raiz do repositório. Imprima o caminho calculado e confira.
- **`TemplateDoesNotExist`:** o template não está em `web/busca/templates/busca/pagina.html`, ou o app `busca` não está em `INSTALLED_APPS`.
- **A página demora na primeira vez:** é o índice da Busca 3 sendo montado quando o servidor sobe. Nas buscas seguintes, não demora.

<a id="sprint-8-escrita"></a>
## Sprint 8 · Escrita: Conclusão, Objetivos específicos, Resumo e Título (Entrega 6)

**Prazo:** 10/12/2026 · **A Conclusão precisa estar pronta na segunda, 07/12.**

**O que você vai entregar:** a Conclusão, os Objetivos específicos, o Resumo, o *Abstract*, as palavras-chave, o Título definitivo e o texto inteiro revisado.

### 6 Conclusão (cerca de 1 página, até 07/12)

Curta e direta. Nada de resultado, conceito ou citação que não tenha aparecido antes. **Escreva, nesta ordem:**

1. **o problema e o objetivo geral**, afirmando que foi alcançado, **com número**: "[...] uma vez que a comparação das três buscas, sobre um catálogo de X cursos e 30 consultas, resultou em P@5 de A, B e C, respectivamente";
2. **a resposta direta às três perguntas de pesquisa**, uma ou duas frases cada. Na terceira, **recomende** uma abordagem para o iFIC;
3. **as contribuições:** a coleção de teste (consultas categorizadas e gabarito documentado, que outros trabalhos podem reaproveitar), a comparação sobre o mesmo SGBD da plataforma medindo qualidade e não só tempo, a medição do efeito de cada recurso separadamente, a análise das falhas e o protótipo com código aberto no repositório;
4. **as dificuldades reais**, do `docs/diario.md`: montar o catálogo e o gabarito, e as armadilhas técnicas (os dois índices `FULLTEXT` separados para poder ponderar, o `HAVING`, o tamanho mínimo de palavra, a lista de palavras vazias em inglês, a ordem entre acento e radical, o corte da correção);
5. **trabalhos futuros**, concretos: aplicar a abordagem recomendada ao iFIC (o principal); repetir a avaliação com consultas reais, coletadas do uso da plataforma; repetir com o MySQL configurado (palavras vazias em português, tamanho mínimo de palavra menor); comparar com uma ferramenta de busca de mercado; e implementar o "você quis dizer...?".

**Não escreva** que "a Busca 3 é melhor" sem dizer em qual nota, sobre qual catálogo e em que tipo de consulta. E não generalize para "sistemas de busca" o que você mediu em um catálogo, em um idioma, em um SGBD e com 30 consultas.

### 1.2 Objetivos específicos

De 4 a 5 itens, verbo no infinitivo, minúscula no início, ponto e vírgula no fim de cada um e ponto no último, **na mesma ordem** das etapas da Metodologia e das subseções dos Resultados. Cada um tem de ser **verificável**: na Conclusão, você mostrou com número que foi atingido. "Instalar uma biblioteca" é tarefa, não objetivo.

O que os itens devem cobrir (escreva com as suas palavras): a construção do catálogo no MySQL e das três buscas; a elaboração da coleção de teste; a medição e comparação da qualidade, por categoria; a medição do custo (tempo e espaço); e a análise das falhas com a recomendação de uso.

### Resumo, *Abstract* e palavras-chave

Escrito **por último**, depois do texto aprovado. Parágrafo único, de 150 a 250 palavras (é um artigo), impessoal, sem citações, sem siglas pouco conhecidas e sem menção a figuras ou tabelas (NBR 6028:2021). Uma ou duas frases para cada item:

1. **contexto e problema:** o catálogo de cursos FIC e a dificuldade de encontrar cursos com a busca simples;
2. **objetivo:** o que o trabalho comparou;
3. **método:** três buscas sobre MySQL, catálogo de N cursos, 30 consultas em seis categorias e gabarito de relevância;
4. **resultados:** os números principais (a P@5 de cada busca e a categoria em que a diferença foi maior);
5. **conclusão:** a recomendação que os números sustentam.

**Coloque números no resumo.** Resumo sem número é resumo fraco.

O ***Abstract*** é a versão em inglês. Os termos técnicos têm forma consagrada (*information retrieval*, *full-text search*, *typo tolerance*, *precision at k*, *test collection*): use-as, e não a tradução literal. Não entregue tradução automática sem revisar.

**Palavras-chave:** de 3 a 5, separadas por ponto e vírgula, no campo de: recuperação da informação; busca textual; MySQL; avaliação de sistemas de busca; cursos de formação inicial e continuada.

### Título

Deve indicar **o que foi feito** e **em que contexto**, coerente com o objetivo geral: a ação (comparação ou avaliação), o objeto (abordagens de busca textual), a tecnologia (MySQL, se couber) e o contexto (catálogo de cursos FIC). Subtítulo separado por dois-pontos, se precisar. Evite títulos genéricos ("Sistema de busca de cursos") e não prometa no título mais do que o artigo mede. Proponha **três opções** na *issue*; nós escolhemos uma com você na revisão.

### Revisão final

- [ ] A Introdução (bloco 4) e a Metodologia estão no **passado** (o que estava "planejado" foi atualizado com o que foi feito)?
- [ ] O print da página web foi inserido em Materiais e Métodos (4.2), anunciado e explicado?
- [ ] O objetivo geral, as perguntas de pesquisa, os objetivos específicos, as subseções dos Resultados e a Conclusão falam das mesmas coisas, na mesma ordem?
- [ ] Todos os números do Resumo, dos Resultados e da Conclusão são **exatamente** os da rodada oficial?
- [ ] Toda nota apresentada nos Resultados (P@5, revocação, MRR) foi definida no Referencial?
- [ ] Está escrito que o gabarito foi montado **antes** de rodar as buscas, e que houve conferência por um segundo avaliador?
- [ ] As justificativas do MySQL, do PyMySQL e da camada em Python estão em Materiais e Métodos?
- [ ] A configuração do banco está informada (collation, tamanho mínimo de palavra, palavras vazias, InnoDB)?
- [ ] Toda tabela e figura é citada no texto antes de aparecer, tem identificação em cima e fonte embaixo?
- [ ] Os gráficos informam a unidade, e a escala logarítmica (se usada) está avisada?
- [ ] Há pelo menos um resultado em que a busca mais simples bastou, e um em que a mais completa falhou?
- [ ] As limitações estão declaradas?
- [ ] As siglas (FIC, IFRN, SGBD, LGPD, MRR) estão por extenso na primeira vez?
- [ ] O texto está impessoal e no passado?
- [ ] O endereço do repositório (https://github.com/nicifrn/mp_ific_busca_curso) está citado em Materiais e Métodos?
- [ ] Todos os comentários foram respondidos e resolvidos?
- [ ] A versão final foi nomeada no histórico: `Entrega 6 - versão final - 10/12`?

Para entregar, comente na *issue* com o nome da versão e as três opções de título, e mova o card para **Em revisão**.

---

<a id="quadro-resumo"></a>
## 9. Quadro-resumo

| Sprint | Período | Desenvolvimento | Escrita | Conceitos novos |
|---|---|---|---|---|
| 1 | 16/10 a 22/10 | Ambiente e conexão com o MySQL | Preparar o documento e fichar | ambiente virtual, driver, collation, senha fora do código |
| 2 | 23/10 a 29/10 | Catálogo e Busca 1 | Introdução e Objetivo geral | CSV, SQL parametrizado, `LIKE`, limitações da busca simples |
| 3 | 30/10 a 05/11 | Coleção de teste e avaliação | Referencial 2.1 a 2.3 | Cranfield, P@5, revocação, MRR, concordância, TDD |
| 4 | 06/11 a 12/11 | Busca 2 (`FULLTEXT`) | Referencial 2.4 a 2.6 | índice invertido, relevância, IDF, `EXPLAIN`, limites do MySQL |
| 5 | 13/11 a 19/11 | Busca 3: índice, radical e BM25 | Metodologia e Materiais e Métodos | tokenização, palavras vazias, *stemming*, BM25 |
| 6 | 20/11 a 26/11 | Busca 3: correção e sinônimos | Tabelas de qualidade | semelhança entre palavras, sinônimos, medição isolada |
| 7 | 27/11 a 03/12 | Rodada oficial, tempo, espaço, gráficos e erros | Resultados e Discussão | mediana, aquecimento, crescimento do tempo, sincronização |
| 8 | 04/12 a 10/12 | Página web, README e fechamento | Conclusão, Resumo e Título | Django, reprodutibilidade |

---

<a id="riscos"></a>
## 10. Riscos e planos B

| Risco | Sinal de alerta | O que fazer |
|---|---|---|
| Sem conexão com o MySQL | Sprint 1, `Access denied` ou `Can't connect` | Confira o `config.py` com a mensagem que eu te enviei. Se continuar, comente na *issue* no mesmo dia, com o erro inteiro, e adiante o `README.md` e as leituras enquanto isso |
| Montar o catálogo consome a sprint inteira | Sprint 2 chegando à quarta sem CSV pronto | Reduza para 150 cursos, mantendo os 8 eixos, e siga. Catálogo menor é limitação declarada; catálogo inexistente é trabalho parado |
| Montar o gabarito consome a sprint inteira | Sprint 3 chegando à quarta sem gabarito | Reduza para 18 consultas, **mantendo as 6 categorias** (3 de cada). Categoria importa mais que quantidade |
| A Busca 2 devolve quase tudo vazio | Sprint 4 | Confira os índices (`SHOW INDEX`), o tamanho das palavras e a frequência delas (passo 6 da Sprint 4) |
| A Busca 3 sai pior que a Busca 2 | Sprint 5 | Confira ordenação, `preparar()` e palavras vazias. Se persistir, é resultado legítimo: **não mexa no gabarito** |
| A correção nunca erra nas 30 consultas | Sprint 6 | Invente consultas extras, fora do gabarito, até achar uma troca errada (passo 6 da Sprint 6) |
| Sem permissão para o `INNODB_TABLESPACES` | Sprint 7 | Registre no `espaco.md` e use só o `information_schema.tables`, com a ressalva no artigo |
| Tempos instáveis | Sprint 7, desvio maior que a mediana | Refaça a medição com tudo fechado, no mesmo dia da rodada de qualidade, e relate as duas |
| Django atrasa | Sprint 8 chegando à segunda sem página | Entregue o resto (README, limpeza, apresentação) e declare a página como trabalho futuro. A página não é resultado; as medições são |

**Se algo tiver de ser cortado, corte largura, não profundidade.** É melhor ter 18 consultas bem julgadas e três buscas bem medidas do que 40 consultas com gabarito no chute. O que **não** pode faltar é o gabarito, as notas por categoria e a análise das falhas: isso é o trabalho.

---

<a id="extras"></a>
## 11. Se sobrar tempo (opcional)

Só depois de a sprint da semana estar entregue. Cada extra que você fizer vira um parágrafo a mais nos Resultados.

- **E1.** Testar o **modo booleano** do MySQL (`IN BOOLEAN MODE`) com expansão de prefixo (`eletric*`) e medir se ele ajuda nos plurais. É o mais próximo de um *stemming* que o MySQL oferece sem mexer no servidor.
- **E2.** Criar uma **lista de palavras vazias em português** para o MySQL: uma tabela InnoDB com uma coluna `value VARCHAR(30)`, apontada pela variável de sessão `innodb_ft_user_stopword_table` **antes** de criar os índices `FULLTEXT`. Medir a Busca 2 com e sem a lista.
- **E3.** Implementar o "você quis dizer...?" na página, mostrando a consulta corrigida pela Busca 3.
- **E4.** Comparar o radicalizador do `snowballstemmer` com o **RSLP** da biblioteca NLTK (`pip install nltk`, depois `nltk.download("rslp")` e `nltk.stem.RSLPStemmer`) e medir a diferença.
- **E5.** Implementar a distância de Levenshtein por conta própria e comparar a correção feita com ela e com o `difflib`.
- **E6.** Medir se cursos com ementa curta são encontrados menos que cursos com ementa longa.

---

<a id="referencias-minimas"></a>
## 12. Referências mínimas do artigo

- **2 obras de metodologia científica:** Gil (2017) e Prodanov e Freitas (2013), em [`docs/orientacoes_escrita_tcc.md`](orientacoes_escrita_tcc.md);
- **2 livros-texto de recuperação da informação** (Manning, Raghavan e Schütze; Baeza-Yates e Ribeiro-Neto; ou Croft, Metzler e Strohman): cobrem as seções 2.1, 2.2 e 2.3;
- **1 fonte sobre *stemming* em português** (o algoritmo Snowball ou o RSLP);
- **o trabalho de Furnas *et al.* (1987)** sobre o problema do vocabulário;
- **a documentação oficial do MySQL** sobre *full-text search* (seção 2.4);
- **1 fonte sobre ferramentas de busca** (seção 2.5);
- **3 trabalhos relacionados** (seção 2.6);
- **a legislação e as fontes institucionais:** Lei nº 11.892/2008, Lei nº 13.709/2018 (LGPD), o Guia Pronatec de Cursos FIC, a Plataforma Nilo Peçanha e a TIC Domicílios;
- **as referências do projeto iFIC** que você usar na Introdução ([`docs/projeto_ific.md`](projeto_ific.md)).

Registre a referência completa de **tudo** o que ler, na seção de Referências do documento do Drive, desde o primeiro dia.
