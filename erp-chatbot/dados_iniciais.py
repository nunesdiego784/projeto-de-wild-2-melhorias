from validacoes import cabecalho, pausar

# ─────────────────────────────────────────────
#  MASSA DE DADOS INICIAIS
# ─────────────────────────────────────────────

clientes_iniciais = [
    {"id_cliente": 1,  "nome": "Ana Paula Souza",      "cpf": "11122233344", "telefone": "(11) 91111-0001", "ativo": True},
    {"id_cliente": 2,  "nome": "Bruno Ferreira Lima",  "cpf": "22233344455", "telefone": "(11) 92222-0002", "ativo": True},
    {"id_cliente": 3,  "nome": "Carla Mendes Rocha",   "cpf": "33344455566", "telefone": "(21) 93333-0003", "ativo": True},
    {"id_cliente": 4,  "nome": "Diego Oliveira Cruz",  "cpf": "44455566677", "telefone": "(31) 94444-0004", "ativo": True},
    {"id_cliente": 5,  "nome": "Elaine Costa Pires",   "cpf": "55566677788", "telefone": "(41) 95555-0005", "ativo": True},
    {"id_cliente": 6,  "nome": "Fábio Alves Martins",  "cpf": "66677788899", "telefone": "(51) 96666-0006", "ativo": True},
    {"id_cliente": 7,  "nome": "Gabriela Nunes Dias",  "cpf": "77788899900", "telefone": "(61) 97777-0007", "ativo": True},
    {"id_cliente": 8,  "nome": "Henrique Borges Tal",  "cpf": "88899900011", "telefone": "(71) 98888-0008", "ativo": True},
    {"id_cliente": 9,  "nome": "Isabela Moura Leal",   "cpf": "99900011122", "telefone": "(81) 99999-0009", "ativo": True},
    {"id_cliente": 10, "nome": "João Pedro Ramos",     "cpf": "00011122233", "telefone": "(91) 90000-0010", "ativo": True},
]

pedidos_iniciais = [
    {"codigo": 1,  "id_cliente": 1,  "cpf_cliente": "11122233344", "nome_cliente": "Ana Paula Souza",     "id_produto": 1,  "nome_produto": "Ração para Cavalos",    "quantidade": 2,  "total": 241.00, "status": "Aguardando confirmação"},
    {"codigo": 2,  "id_cliente": 2,  "cpf_cliente": "22233344455", "nome_cliente": "Bruno Ferreira Lima", "id_produto": 3,  "nome_produto": "Adubo Orgânico",         "quantidade": 3,  "total": 135.00, "status": "Confirmado"},
    {"codigo": 3,  "id_cliente": 3,  "cpf_cliente": "33344455566", "nome_cliente": "Carla Mendes Rocha",  "id_produto": 5,  "nome_produto": "Enxada",                 "quantidade": 1,  "total": 59.90,  "status": "Entregue"},
    {"codigo": 4,  "id_cliente": 4,  "cpf_cliente": "44455566677", "nome_cliente": "Diego Oliveira Cruz", "id_produto": 7,  "nome_produto": "Sementes de Capim",      "quantidade": 5,  "total": 177.50, "status": "Aguardando confirmação"},
    {"codigo": 5,  "id_cliente": 5,  "cpf_cliente": "55566677788", "nome_cliente": "Elaine Costa Pires",  "id_produto": 2,  "nome_produto": "Saco de Milho 50kg",     "quantidade": 2,  "total": 179.80, "status": "Confirmado"},
    {"codigo": 6,  "id_cliente": 6,  "cpf_cliente": "66677788899", "nome_cliente": "Fábio Alves Martins", "id_produto": 9,  "nome_produto": "Pulverizador Manual",    "quantidade": 1,  "total": 98.75,  "status": "Cancelado"},
    {"codigo": 7,  "id_cliente": 7,  "cpf_cliente": "77788899900", "nome_cliente": "Gabriela Nunes Dias", "id_produto": 4,  "nome_produto": "Mangueira p/ Irrigação", "quantidade": 2,  "total": 151.98, "status": "Entregue"},
    {"codigo": 8,  "id_cliente": 8,  "cpf_cliente": "88899900011", "nome_cliente": "Henrique Borges Tal", "id_produto": 6,  "nome_produto": "Vacina Veterinária",     "quantidade": 1,  "total": 150.00, "status": "Aguardando confirmação"},
    {"codigo": 9,  "id_cliente": 9,  "cpf_cliente": "99900011122", "nome_cliente": "Isabela Moura Leal",  "id_produto": 8,  "nome_produto": "Botina de Couro",        "quantidade": 1,  "total": 110.00, "status": "Confirmado"},
    {"codigo": 10, "id_cliente": 10, "cpf_cliente": "00011122233", "nome_cliente": "João Pedro Ramos",    "id_produto": 10, "nome_produto": "Arame Farpado 100m",     "quantidade": 1,  "total": 210.00, "status": "Entregue"},
]

# ─────────────────────────────────────────────
#  FUNÇÕES DE INFORMAÇÃO
# ─────────────────────────────────────────────

def info_horarios():
    cabecalho("Horários de Atendimento")
    print("  Segunda a Sexta: 08h às 18h")
    print("  Sábado:          09h às 13h")
    print("  Domingo:         Fechado")
    pausar()

def info_contato():
    cabecalho("Canais de Contato")
    print("   Telefone : (11) 1234-5678")
    print("   E-mail   : suporte@casadecampocentral011.com")
    pausar()

def info_politicas():
    cabecalho("Políticas e Termos")
    print("  • Prazo de devolução: 7 dias corridos")
    print("  • Garantia padrão   : 12 meses")
    print("  • Privacidade       : www.casadecampocentral011.com/privacidade")
    pausar()

def info_faq():
    cabecalho("Perguntas Frequentes (FAQ)")
    faqs = [
        ("Como rastrear meu pedido?", "Acesse 'Pedidos > Rastrear Pedido' ou use o código no e-mail."),
        ("Posso trocar um produto?",  "Sim, dentro de 7 dias com nota fiscal."),
        ("Aceitam cartão de débito?", "Sim, todas as bandeiras principais."),
    ]
    for i, (p, r) in enumerate(faqs, 1):
        print(f"\n  {i}. {p}")
        print(f"     → {r}")
    pausar()
