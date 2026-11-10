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

Explicacao tecnica para o professor:
O uso do `parent_id` implementa uma estrutura de lista encadeada / arvore (auto-relacionamento). Quando o usuario gera ou refina uma nova versao de um prompt existente, o novo registro guarda a referencia direta de qual prompt serviu de base.

---

## 3. Roteiro Pratico da Apresentacao (Passo a Passo)

### Parte 1: Introducao e Contexto (1 a 2 minutos)
- "Nosso projeto consiste em uma plataforma para gerenciamento e evolucao de prompts orientados a modelos de IA generativa."
- "O foco principal desta entrega foi estruturar a camada de persistencia relacional e uma interface limpa para operacao dos dados."

### Parte 2: Demonstracao Pratica na Tela (2 a 3 minutos)
1. **Mostrar a tela inicial** (`http://127.0.0.1:5000`):
   - Apontar o topo com a identidade visual da IA.
   - Mostrar o formulario com entrada de texto e upload de imagem.
2. **Cadastrar o primeiro prompt**:
   - Digitar um exemplo (ex: "Gere uma descricao detalhada para uma campanha de marketing").
   - Clicar em Salvar.
   - Mostrar que o prompt foi renderizado na lista logo abaixo.
3. **Demonstrar a Evolucao (`parent_id`)**:
   - Clicar no botao **Evolve** do prompt criado.
   - Mostrar que foi gerada uma nova entrada com o indicador `Evolucao do prompt #1`.
4. **Demonstrar no Banco de Dados**:
   - Abrir o terminal ou a extensao SQLite Viewer no VS Code.
   - Mostrar a tabela `prompts` com as colunas `id`, `text`, `image_path` e `parent_id` preenchidas.

### Parte 3: Conclusao e Proximos Passos (1 minuto)
- "Com a base estruturada e os relacionamentos de versao consolidados, as proximas etapas serao conectar a API do modelo de linguagem para processar as entradas e alimentar automaticamente o historico de geracoes."

---

## 4. Possiveis Perguntas do Professor e Respostas Sugeridas

**P: Por que usar SQLite nessa fase?**  
*R:* O SQLite e um banco relacional completo, sem overhead de configuracao de rede, ideal para prototipagem de modelos de dados relacionais e testes locais antes da migracao para PostgreSQL ou MySQL em producao.

**P: Como funciona o relacionamento de evolucao dos prompts?**  
*R:* Foi implementado um auto-relacionamento 1:N atraves da coluna `parent_id`. Um prompt pai pode ter multiplos prompts filhos (variacoes ou refinamentos), permitindo reconstruir toda a linhagem das iteracoes feitas pelo usuario.

**P: Onde as imagens ficam armazenadas?**  
*R:* Os arquivos fisicos sao salvos no diretorio `static/uploads/`, e o banco armazena apenas o caminho relativo em `image_path`. Isso evita sobrecarregar o banco de dados com tipos BLOB e segue as boas praticas de arquitetura de aplicacoes web.
