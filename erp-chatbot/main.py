from validacoes import cabecalho, linha, ler_opcao, pausar
from dados_iniciais import (clientes_iniciais, pedidos_iniciais,
                             info_horarios, info_contato, info_politicas, info_faq)
from clientes import submenu_cadastro_suporte
from ordens_servico import pedido_novo, pedido_rastrear, pedido_cancelar, pedido_historico

# ─────────────────────────────────────────────
#  MATRIZES GLOBAIS (carregadas com dados iniciais)
# ─────────────────────────────────────────────
clientes = list(clientes_iniciais)   # cópia para não modificar os originais
pedidos  = list(pedidos_iniciais)

produtos = [
    {"codigo": 1,  "nome": "Ração para Cavalos",      "categoria": "Animais",       "preco": 120.50, "estoque": 15},
    {"codigo": 2,  "nome": "Saco de Milho 50kg",       "categoria": "Grãos",         "preco": 89.90,  "estoque": 30},
    {"codigo": 3,  "nome": "Adubo Orgânico",           "categoria": "Jardinagem",    "preco": 45.00,  "estoque": 20},
    {"codigo": 4,  "nome": "Mangueira para Irrigação", "categoria": "Irrigação",     "preco": 75.99,  "estoque": 12},
    {"codigo": 5,  "nome": "Enxada",                   "categoria": "Ferramentas",   "preco": 59.90,  "estoque": 18},
    {"codigo": 6,  "nome": "Vacina Veterinária",       "categoria": "Veterinária",   "preco": 150.00, "estoque": 8},
    {"codigo": 7,  "nome": "Sementes de Capim",        "categoria": "Sementes",      "preco": 35.50,  "estoque": 40},
    {"codigo": 8,  "nome": "Botina de Couro",          "categoria": "Vestuário Rural","preco": 110.00,"estoque": 10},
    {"codigo": 9,  "nome": "Pulverizador Manual",      "categoria": "Agricultura",   "preco": 98.75,  "estoque": 14},
    {"codigo": 10, "nome": "Arame Farpado 100m",       "categoria": "Cercamento",    "preco": 210.00, "estoque": 6},
]


# ─────────────────────────────────────────────
#  SUBMENUS
# ─────────────────────────────────────────────

def submenu_informacoes():
    while True:
        cabecalho("  Informações")
        print("  1. Horários de Atendimento")
        print("  2. Canais de Contato")
        print("  3. Políticas e Termos")
        print("  4. Perguntas Frequentes (FAQ)")
        print("  0. Voltar ao Menu Principal")

        opcao = ler_opcao(["1", "2", "3", "4", "0"])
        if opcao == "1":
            info_horarios()
        elif opcao == "2":
            info_contato()
        elif opcao == "3":
            info_politicas()
        elif opcao == "4":
            info_faq()
        elif opcao == "0":
            break


def submenu_pedidos():
    while True:
        cabecalho("  Pedidos")
        print("  1. Realizar Pedido")
        print("  2. Rastrear Pedido")
        print("  3. Cancelar Pedido")
        print("  4. Histórico de Pedidos")
        print("  0. Voltar ao Menu Principal")

        opcao = ler_opcao(["1", "2", "3", "4", "0"])
        if opcao == "1":
            pedido_novo(pedidos, clientes, produtos)
        elif opcao == "2":
            pedido_rastrear(pedidos)
        elif opcao == "3":
            pedido_cancelar(pedidos)
        elif opcao == "4":
            pedido_historico(pedidos, clientes)   # passa clientes para busca dinâmica
        elif opcao == "0":
            break


# ─────────────────────────────────────────────
#  MENU PRINCIPAL
# ─────────────────────────────────────────────

def menu_geral():
    print("\n" + "═" * 40)
    print("     ChatBot de Atendimento ao Cliente")
    print("═" * 40)
    print("   Olá! Bem-vindo(a) ao nosso atendimento.")

    while True:
        cabecalho("MENU PRINCIPAL")
        print("  1. Cadastro e Suporte")
        print("  2. Informações")
        print("  3. Pedidos")
        print("  0. Encerrar Atendimento")

        opcao = ler_opcao(["1", "2", "3", "0"])

        if opcao == "1":
            submenu_cadastro_suporte(clientes, pedidos)   # passa pedidos para a trava
        elif opcao == "2":
            submenu_informacoes()
        elif opcao == "3":
            submenu_pedidos()
        elif opcao == "0":
            linha()
            print("  Obrigado pelo contato. Até logo!")
            linha()
            break


if __name__ == "__main__":
    menu_geral()
