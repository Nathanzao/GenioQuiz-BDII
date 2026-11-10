# Guia de Apresentacao do Projeto - Banco de Dados II
**Alunos:** Nicolas e Nathan  
**Tema:** Interface e Persistencia de Prompts com Evolucao de Versoes

---

## 1. Visao Geral da Apresentacao

O objetivo do projeto nesta etapa foi desenvolver a interface inicial e a modelagem do banco de dados para um sistema gerador e gerenciador de prompts para IA.

Pontos centrais da proposta:
- Interface simples e direta para submissao e consulta de prompts.
- Suporte a anexo de imagem de contexto/referencia.
- Persistencia relacional em SQLite.
- Controle de historico e linhagem de prompts atraves do campo de auto-relacionamento `parent_id`.

---

## 2. Modelagem do Banco de Dados

A base foi implementada em SQLite local (`prompts.db`).

Tabela: `prompts`
- `id`: Chave primaria autoincrementada (INTEGER PRIMARY KEY AUTOINCREMENT).
- `text`: Texto do prompt (TEXT NOT NULL).
- `image_path`: Caminho da imagem anexada no servidor (TEXT, opcional).
- `parent_id`: Identificador do prompt de origem (INTEGER, chave estrangeira logica para `prompts.id`). Permite criar a arvore de derivacoes e evolucoes de um prompt.
