# 🤖 ChatBot Assistente de ERP — Terminal Python

> Projeto acadêmico | Componente Curricular: Desenvolvimento de Sistemas Computacionais para Processamento e Registro de Dados

---

## 📌 Sobre o Projeto

Sistema de gerenciamento empresarial (ERP) operado via terminal, desenvolvido em Python puro. O ChatBot simula a interface que um funcionário usaria para gerenciar dois setores integrados da empresa em uma única sessão interativa.

> ⚠️ **Regra de Escopo:** Todas as operações rodam puramente na memória RAM (listas e matrizes Python). Não há persistência de dados — sem arquivos `.txt`, `.json` ou banco de dados. Se o programa for encerrado, os dados resetam. O foco é a lógica de integração e as travas de segurança do sistema.

---

## 🏗️ Estrutura de Arquivos

```
erp-chatbot/
├── README.md
├── main.py               # Loop principal + menus de navegação
├── dados_iniciais.py     # Duas matrizes com 10+ registros de teste
├── clientes.py           # Funções CRUD do Cadastro de Clientes
├── ordens_servico.py     # Funções CRUD do Cadastro de Ordens de Serviço
└── validacoes.py         # Funções de validação compartilhadas
```

---

## 🗂️ Cadastros Integrados

### Cadastro 1 — Clientes

| Campo | Tipo | Obrigatório |
|---|---|---|
| id_cliente | int | ✅ Sim |
| nome | str | ✅ Sim |
| cpf | str | ✅ Sim |
| telefone | str | ❌ Não |
| ativo | bool | ✅ Sim |

### Cadastro 2 — Ordens de Serviço

| Campo | Tipo | Obrigatório |
|---|---|---|
| id_os | int | ✅ Sim |
| id_cliente | int | ✅ Sim (vínculo) |
| descricao | str | ✅ Sim |
| valor | float | ✅ Sim |
| concluida | bool | ✅ Sim |

---

## 📅 Etapas do Projeto

### Etapa 1 — Mapeamento de Dados e Carga Inicial *(Semana 1)*

**Objetivo:** Modelar os dados dos dois setores e preparar a base na memória.

- Definir os dois cadastros integrados com base no fluxo BPMN da equipe
- Identificar campos obrigatórios, regras de validação e tipos primitivos
- Criar duas matrizes com no mínimo 10 registros reais de teste cada

**Entrega:** Documento PDF com os dois setores escolhidos e as tabelas de mapeamento de dados (Nome do campo, Tipo Primitivo, Estrutura Utilizada e Obrigatoriedade).

---

### Etapa 2 — Menu Geral, Submenus e Loop *(Semana 2)*

**Objetivo:** Construir a navegação do ChatBot com transição contínua entre as duas áreas.

A estrutura de navegação funciona em 3 camadas de loop:

```
Loop externo (while) → Menu Principal
    ├── Loop interno A → Submenu de Clientes
    │       └── Listar / Cadastrar / Excluir / Voltar
    ├── Loop interno B → Submenu de Ordens de Serviço
    │       └── Listar / Cadastrar / Excluir / Voltar
    └── Opção 0 → Encerra o sistema
```

> O "Voltar" é controlado por uma variável booleana do loop interno. Quando o usuário escolhe voltar, a variável vira `False` e o loop interno para, retornando ao menu principal.

**Entrega:** Código-fonte parcial com estrutura de menus e submenus totalmente navegável.

---

### Etapa 3 — CRUD Integrado e Validações Cruzadas *(Semana 3)*

**Objetivo:** Finalizar as operações de dados com travas lógicas de segurança (Regras de Negócio).

#### Operações implementadas

**📋 Listar (Read)**
- Clientes: exibe todos os campos da matriz
- OS: traduz o `id_cliente` para o **nome real** do cliente buscando na matriz de clientes

**➕ Cadastrar (Create)**
- Impede IDs duplicados
- Impede campos de texto em branco
- Na OS: valida se o `id_cliente` informado **existe na matriz de clientes** antes de criar

**🗑️ Excluir (Delete) — Trava de Integridade**
- Antes de deletar um Cliente, o sistema varre a matriz de OS
- Se encontrar alguma OS vinculada ao cliente, **bloqueia a exclusão** com mensagem de erro

#### Funções principais

```
cadastrar_cliente(matriz_clientes)
listar_clientes(matriz_clientes)
excluir_cliente(matriz_clientes, matriz_os)   # recebe as duas matrizes
cadastrar_os(matriz_os, matriz_clientes)      # recebe as duas matrizes
listar_os(matriz_os, matriz_clientes)         # recebe as duas matrizes
excluir_os(matriz_os)
```

**Entrega Final:** Código-fonte completo `.py` + apresentação prática demonstrando o ChatBot operando ambos os setores e provando que as validações e bloqueios funcionam.

---

## ✅ Checklist da Apresentação Final

O professor vai avaliar ao vivo — preparem para demonstrar:

- [ ] Cadastrar OS com `id_cliente` inexistente → deve **bloquear**
- [ ] Deletar cliente que possui OS vinculada → deve **bloquear**
- [ ] Cadastrar dois registros com o mesmo ID → deve **bloquear**
- [ ] Listar OS exibindo o **nome do cliente** (não o ID numérico)

---

## 👥 Divisão de Tarefas da Equipe

| Integrante | Responsabilidade |
|---|---|
| A definir | `clientes.py` — CRUD de Clientes |
| A definir | `ordens_servico.py` — CRUD de Ordens de Serviço |
| A definir | `validacoes.py` + `dados_iniciais.py` |
| A definir | `main.py` — Menu do ChatBot e integração geral |

---

## 🔀 Fluxo de Trabalho no GitHub

1. **Nunca trabalhar direto na branch `main`**
2. Cada integrante cria sua branch: `feature/cadastro-clientes`, `feature/ordens-servico`, etc.
3. Ao finalizar, abrir um **Pull Request** para revisão do grupo
4. Outro integrante revisa e aprova antes de mesclar na `main`
5. Usar **Issues** para registrar e distribuir tarefas

```
main (protegida)
├── feature/dados-iniciais
├── feature/menus
├── feature/crud-clientes
└── feature/crud-ordens-servico
```

---

## 🛠️ Tecnologias

- Python 3.x
- Execução via Terminal
- Sem dependências externas

---

*Projeto desenvolvido para a disciplina de Desenvolvimento de Sistemas Computacionais — UNIFAN*
