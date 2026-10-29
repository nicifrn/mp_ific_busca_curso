# mp_ific_busca_curso

## O que é este projeto
Este projeto compara abordagens de busca de cursos de Formação Inicial e Continuada (FIC) sobre um catálogo sintético, no contexto da plataforma iFIC, do Instituto Federal do Rio Grande do Norte (IFRN).
As abordagens são avaliadas com métricas de recuperação da informação (precisão, revocação, P@5 e MRR) e com medições de tempo de resposta e consumo de recursos.
O resultado servirá de base para o campo de busca do catálogo público de cursos do iFIC.

## Responsáveis
- Kelly Claire (@Kcallvs): autora
- Prof. Bruno Gomes (@brunogomesifrn): orientador, NIC/IFRN
- Entony (@franciscoentony): orientador, NIC/IFRN

## Instalação
1. Clone o repositório e entre na pasta:

        git clone https://github.com/nicifrn/mp_ific_busca_curso.git
        cd mp_ific_busca_curso

2. Crie e ative o ambiente virtual (no Windows, a ativação é `.venv\Scripts\activate`):

        python3 -m venv .venv
        source .venv/bin/activate

3. Instale as dependências:

        pip install -r requirements.txt

4. Crie o `config.py` a partir do modelo e preencha com os dados do seu MySQL. Ele não vai para o Git, porque guarda a senha do banco:

        cp config_exemplo.py config.py

## Como rodar
Por enquanto, só o verificador do ambiente:

    python verificar_ambiente.py


### Sprint 2: catálogo e Busca 1
Carregar o catálogo no MySQL (pode rodar mais de uma vez):

    python criar_banco.py

Verificar o catálogo:

    python -m testes.verificar_catalogo

Testar a Busca 1 (LIKE):

    python -m buscadores.busca1_like
