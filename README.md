# Resumo do Projeto — ChatBot Assistente de ERP

Pagina 1

## O que é o projeto?

Vocês vão construir um **sistema de gerenciamento empresarial (ERP) via terminal**, usando Python puro. O sistema simula um chatbot onde um funcionário consegue gerenciar dois setores da empresa numa mesma sessão. Tudo roda na memória RAM — sem banco de dados, sem arquivos externos.

---

## As 3 Etapas (o que o PDF descreve)

O documento mostra apenas a **Etapa 1** completa. As etapas 2 e 3 provavelmente estão na página 2 (que não foi carregada), mas pela lógica do projeto incremental, seguem o padrão abaixo:

### 📅 Etapa 1 — Mapeamento de Dados e Carga Inicial
**Objetivo:** Montar a estrutura de dados e popular com dados de teste.

O que precisa ser feito:
- Escolher os **dois cadastros integrados** (ex: Clientes + Ordens de Serviço)
- Definir os **campos de cada cadastro** com seus tipos (`str`, `int`, `float`, `bool`)
- Criar **regras de validação** (ex: CPF não pode ser vazio, valor não pode ser negativo)
- Popular **duas matrizes** com no mínimo 10 registros de teste cada uma, diretamente no código

### 📅 Etapa 2 — (provável) CRUD e Integração entre Cadastros
Com base no padrão de projetos assim, essa etapa provavelmente pede:
- Operações de **Criar, Listar, Buscar, Atualizar e Deletar** registros
- **Integração real** entre os dois cadastros (ex: uma Ordem de Serviço só pode ser criada se o Cliente existir)
- Validações cruzadas entre os dois setores

### 📅 Etapa 3 — (provável) Interface do ChatBot e Travas de Segurança
- Menu interativo no terminal com navegação por comandos
- **Travas de segurança** (ex: não deletar cliente que tem pedido ativo)
- Relatórios e consultas integradas

---

## Como desenvolver em grupo no GitHub

### Estrutura de organização recomendada

Já que vocês têm uma organização criada no GitHub, sigam esse fluxo:

**1. Criem um repositório dentro da organização**
- Nome sugerido: `erp-chatbot-python`
- Inicializem com um `README.md` descrevendo o projeto

**2. Montem a estrutura de pastas assim:**
```
erp-chatbot-python/
├── README.md
├── main.py              ← arquivo principal (integra tudo)
├── clientes.py          ← módulo do cadastro de clientes
├── ordens_servico.py    ← módulo do segundo cadastro
├── dados_iniciais.py    ← as matrizes com os 10+ registros de teste
└── validacoes.py        ← funções de validação compartilhadas
```

**3. Dividam as tarefas por arquivo/módulo**

| Integrante | Responsabilidade |
|---|---|
| Pessoa A | `clientes.py` — CRUD de clientes |
| Pessoa B | `ordens_servico.py` — CRUD do segundo cadastro |
| Pessoa C | `validacoes.py` + `dados_iniciais.py` |
| Pessoa D | `main.py` — menu do chatbot e integração |

**4. Usem branches para não conflitar**
- Cada pessoa trabalha na sua branch: `feature/cadastro-clientes`, `feature/ordens-servico`, etc.
- Abram **Pull Requests** para mesclar na branch `main` — isso também serve como revisão do grupo

**5. Usem Issues do GitHub para organizar tarefas**
- Criem uma Issue para cada tarefa ("Criar matriz de clientes", "Validar CPF", etc.)
- Atribuam cada Issue a um integrante

---

## Por onde começar agora (Etapa 1)

1. **Decidam os dois cadastros** em reunião de grupo — escolham algo relacionado ao BPMN que já fizeram
2. **Num documento compartilhado** (pode ser no próprio README), listem os campos de cada cadastro com tipo e regra de validação antes de escrever qualquer código
3. **Uma pessoa cria o repositório** na organização e convida os demais como colaboradores
4. **Cada um clona** o repositório na sua máquina
5. Criem o arquivo `dados_iniciais.py` juntos (pode ser numa chamada) para garantir que os 10 registros de cada cadastro façam sentido e sejam coerentes entre si

---




# Projeto Completo — ChatBot Assistente de ERP

    Pagina 2 

---

## Etapa 1 — Mapeamento de Dados e Carga Inicial
**Entrega: Documento PDF**

### O que fazer
Escolher os dois cadastros e montar uma **tabela de mapeamento** para cada um. Exemplo com Clientes + Ordens de Serviço:

**Cadastro 1 — Clientes**
| Campo | Tipo | Obrigatório? |
|---|---|---|
| id_cliente | int | Sim |
| nome | str | Sim |
| cpf | str | Sim |
| telefone | str | Não |
| ativo | bool | Sim |

**Cadastro 2 — Ordens de Serviço**
| Campo | Tipo | Obrigatório? |
|---|---|---|
| id_os | int | Sim |
| id_cliente | int | Sim (vínculo) |
| descricao | str | Sim |
| valor | float | Sim |
| concluida | bool | Sim |

No código, cada cadastro vira uma **lista de listas** (matriz), com 10 registros fixos escritos manualmente. Nada de input ainda — só dados estáticos pra testar.

### Dica para o grupo
Um integrante monta a tabela de Clientes, outro monta a de OS. Depois reúnem no mesmo documento PDF e revisam juntos se os campos fazem sentido integrados.

---

## Etapa 2 — Menu Geral, Submenus e Loop
**Entrega: Código parcial navegável**

### O que construir
A **espinha dorsal** do chatbot — a navegação. O sistema precisa ficar rodando em loop até o usuário digitar "Sair".

### Como pensar a estrutura (sem código na cara)

Pense em **3 camadas de loop**:

```
Loop externo (while) → Menu Principal
    └── Loop interno A → Submenu de Clientes
            └── opções: Listar / Cadastrar / Excluir / Voltar
    └── Loop interno B → Submenu de Ordens de Serviço
            └── opções: Listar / Cadastrar / Excluir / Voltar
    └── Opção 0 → encerra o loop externo
```

O segredo do "Voltar" é uma **variável booleana de controle** do loop interno. Quando o usuário digita "Voltar", essa variável vira `False` e o loop interno para — voltando ao menu principal automaticamente.

### Divisão no grupo
- Pessoa A: escreve o loop principal e o Menu Principal
- Pessoa B: escreve o submenu de Clientes
- Pessoa C: escreve o submenu de OS
- Pessoa D: integra tudo no `main.py` e testa a navegação

---

## Etapa 3 — CRUD Integrado e Validações Cruzadas
**Entrega: Código completo + apresentação ao professor**

### As 4 operações que precisam funcionar

**Listar (Read)**
- Para Clientes: exibe todos os campos da matriz
- Para OS: ao exibir, **traduz o `id_cliente` para o nome real** buscando na matriz de clientes — o professor vai olhar isso com atenção

**Cadastrar (Create)**
Duas validações obrigatórias:
1. Verificar se o ID já existe na matriz antes de inserir (impedir duplicata)
2. Impedir campos de texto em branco
3. Na OS especificamente: checar se o `id_cliente` informado **existe na matriz de clientes** antes de criar a OS

**Excluir (Delete)**
A **trava mais importante** do projeto: antes de deletar um Cliente, o sistema varre a matriz de OS procurando se algum registro usa aquele `id_cliente`. Se encontrar, bloqueia a exclusão com uma mensagem clara de erro.

### Como pensar as funções
Cada operação vira uma função separada que recebe a matriz como parâmetro. Isso facilita muito dividir entre o grupo:

```
cadastrar_cliente(matriz_clientes)
listar_clientes(matriz_clientes)
excluir_cliente(matriz_clientes, matriz_os)  ← precisa das duas!
cadastrar_os(matriz_os, matriz_clientes)     ← precisa das duas!
listar_os(matriz_os, matriz_clientes)        ← precisa das duas!
excluir_os(matriz_os)
```

---

## Fluxo de trabalho no GitHub (organização já criada)

### Setup inicial (fazer uma vez só)
1. Um integrante cria o repositório na organização e configura a estrutura de pastas
2. Todos fazem `git clone` do repositório
3. Ninguém trabalha direto na branch `main`

### Fluxo por etapa
```
main (protegida)
├── etapa-1/documentacao
├── etapa-2/menus
└── etapa-3/crud-validacoes
```

Cada pessoa trabalha na sua branch, abre Pull Request, outro integrante revisa e aprova antes de mesclar. Isso garante que o professor veja o histórico de contribuição de cada um.

### Estrutura de arquivos sugerida
```
erp-chatbot/
├── README.md
├── main.py               ← loop principal + menus
├── dados_iniciais.py     ← as duas matrizes com 10 registros
├── clientes.py           ← funções CRUD de clientes
├── ordens_servico.py     ← funções CRUD de OS
└── validacoes.py         ← funções de validação compartilhadas
```

---

## O que o professor vai avaliar na apresentação

Com base nas exigências da Etapa 3, preparem para demonstrar ao vivo:
- Tentar cadastrar uma OS com um `id_cliente` que **não existe** → deve bloquear
- Tentar deletar um cliente que **tem OS vinculada** → deve bloquear
- Cadastrar dois registros com o **mesmo ID** → deve bloquear
- Listar OS mostrando o **nome do cliente** (não o ID numérico)

Se quiser ajuda para pensar a lógica de alguma função específica sem receber o código pronto, é só perguntar!