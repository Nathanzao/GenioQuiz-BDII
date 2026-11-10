# Gerenciador de Prompts

Projeto desenvolvido para a disciplina de Banco de Dados II.  
Alunos: Nicolas e Nathan.

## Descricao
Aplicacao web desenvolvida em Python (Flask) integrada a um banco de dados relacional SQLite para registro, edicao e acompanhamento de evolucao de prompts. O sistema suporta anexo de imagens e mantem o historico de derivacao das versoes cadastradas.

## Banco de Dados
O banco de dados SQLite local (`prompts.db`) armazena os dados na tabela `prompts`:

- `id`: Identificador unico (INTEGER, Chave Primaria, Autoincremento).
- `text`: Texto do prompt (TEXT, obrigatorio).
- `image_path`: Caminho relativo da imagem enviada no upload (TEXT, opcional).
- `parent_id`: Referencia ao prompt de origem (INTEGER, auto-relacionamento com `prompts.id`). Permite identificar qual prompt gerou uma nova versao quando utilizada a acao de evolucao.

## Estrutura do Projeto
```
prompt_ai/
|-- app.py                  # Rotas da aplicacao e manipulacao do SQLite
|-- requirements.txt        # Dependencias Python
|-- prompts.db              # Banco de dados SQLite
|-- orientacoes_apresentacao.md # Roteiro de apresentacao
|-- README.md               # Documentacao do projeto
|-- static/
|   |-- ia.jpg              # Imagem de apresentacao da interface
|   `-- uploads/            # Diretorio onde sao salvas as imagens enviadas
`-- templates/
    |-- index.html          # Pagina principal (cadastro, listagem e acoes)
    `-- edit.html           # Tela de edicao de prompts
```

## Instrucoes de Execucao

1. Instale as dependencias do projeto:
```bash
pip install -r requirements.txt
```

2. Inicie o servidor:
```bash
python app.py
```

3. Acesse a aplicacao pelo navegador:
```
http://127.0.0.1:5000
```
