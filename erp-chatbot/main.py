"""
ChatBot de Atendimento ao Cliente
Etapa 2 — Menu Geral, Submenus e Loop
Estrutura: 3 camadas de loop
  Camada 1: Loop principal (Menu Geral)
  Camada 2: Loop de submenu (Informações / Pedidos)
  Camada 3: Loop de ação (executa e volta ao submenu)
"""
def linha():
    print("─" * 40)

def cabecalho(titulo: str):
    linha()
    print(f"  {titulo}")
    linha()

def pausar():
    input("\nPressione Enter para continuar...")

def ler_opcao(opcoes_validas: list[str]) -> str:
    """Lê a entrada do usuário e valida contra a lista de opções."""
    while True:
        escolha = input("\nEscolha uma opção: ").strip()
        if escolha in opcoes_validas:
            return escolha
        print(f"  ⚠  Opção inválida. Escolha entre: {', '.join(opcoes_validas)}")  
       
def cadastro_novo_cliente():
    cabecalho("Cadastrar Novo Cliente")
    print("  Informe os dados abaixo:")
    nome = input("  Nome completo : ").strip()
    cpf  = input("  CPF          : ").strip()
    if nome and cpf:
        print(f"\n   Cliente '{nome}' cadastrado com sucesso!")
        print(f"     CPF: {cpf}")
    else:
        print("   Dados incompletos. Cadastro não realizado.")
    pausar()

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

def pedido_novo():
    cabecalho("Realizar Novo Pedido")
    print("  Informe os dados abaixo:")
    produto = input("  Nome do produto : ").strip()
    qtd     = input("  Quantidade      : ").strip()
    if produto and qtd:
        print(f"\n   Pedido registrado!")
        print(f"     Produto  : {produto}")
        print(f"     Qtd      : {qtd}")
        print(f"     Status   : Aguardando confirmação")
    else:
        print("    Dados incompletos. Pedido não registrado.")
    pausar()

def pedido_rastrear():
    cabecalho("Rastrear Pedido")
    codigo = input("  Digite o código do pedido: ").strip()
    if codigo:
        # Simulação de rastreamento
        print(f"\n   Rastreando pedido {codigo.upper()}...")

        print("     Status atual : Em separação no estoque")

        print("     Previsão     : 2 dias úteis")
    else:
        print("    Código não informado.")
    pausar()

def pedido_cancelar():
    cabecalho("Cancelar Pedido")
    codigo = input("  Código do pedido a cancelar: ").strip()
    if codigo:
        confirma = input(f"  Confirmar cancelamento de '{codigo.upper()}'? (s/n): ").strip().lower()
        if confirma == "s":
            print("   Pedido cancelado com sucesso.")
        else:
            print("    Cancelamento abortado.")
    else:
        print("   Código não informado.")
    pausar()

def pedido_historico():
    cabecalho("Histórico de Pedidos")
    # Dados simulados
    historico = []
    print(f"  {'Código':<10} {'Produto':<15} {'Status':<15} {'Data'}")
    linha()
    for cod, prod, status, data in historico:
        print(f"  {cod:<10} {prod:<15} {status:<15} {data}")
    pausar()



def submenu_cadastro_suporte():
    """Loop do submenu de Cadastro e Suporte."""

    while True:
        cabecalho("👤  Cadastro e Suporte")

        print("  1. Cadastrar Novo Cliente")
        print("  2. Alterar Dados do Cliente")
        print("  3. Excluir Cliente")
        print("  4. Suporte ao Cliente")
        print("  0. Voltar ao Menu Principal")

        opcao = ler_opcao(["1", "2", "3", "4", "0"])

        if opcao == "0":
            break
        elif opcao == "1":
            cadastro_novo_cliente() 

        elif opcao == "2":
            def submenu_alterar_cliente():
                cabecalho("Alterar Dados do Cliente")
                cpf = input("Digite o CPF do cliente que deseja alterar: ").strip()
                for cliente in clientes:
                    if cliente["cpf"] == cpf:
                        print(f"Cliente encontrado: {cliente['nome']} (CPF: {cliente['cpf']})")
                        novo_nome = input("Digite o novo nome (deixe em branco para manter): ").strip()
                        novo_cpf  = input("Digite o novo CPF (deixe em branco para manter): ").strip()
                        if novo_nome:
                            cliente["nome"] = novo_nome
                        if novo_cpf:
                            cliente["cpf"] = novo_cpf
                        print("Cliente atualizado com sucesso!")
                        return
                    else:
                        print("Alteração cancelada.")
                        return  
                print("Cliente não encontrado. Verifique o CPF e tente novamente.")
                submenu_alterar_cliente()


        elif opcao == "3":
            def submenu_excluir_cliente():
                cabecalho("Excluir Cliente")
                cpf = input(" Digite o CPF do cliente que deseja excluir: ").strip()
                for cliente in clientes:
                    if cliente["cpf"] == cpf:
                        print(f" Cliente encontrado: {cliente['nome']} (CPF: {cliente['cpf']})")
                        confirma = input(" Confirmar exclusão deste cliente? (s/n): ").strip().lower()
                        if confirma == "s":
                            clientes.remove(cliente)
                            print(" Cliente excluído com sucesso!")
                            return
                        else:
                            print(" Exclusão cancelada.")
                            return
                print(" Cliente não encontrado. Verifique o CPF e tente novamente.")
                submenu_excluir_cliente()

def submenu_informacoes():
    """Loop do submenu Informações."""
    while True:
        cabecalho("📋  Informações")

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
            break   # sobe para camada 1


def submenu_pedidos():
    """Loop do submenu Pedidos."""
    while True:
        cabecalho("🛒  Pedidos")

        print("  1. Realizar Novo Pedido")

        print("  2. Rastrear Pedido")

        print("  3. Cancelar Pedido")

        print("  4. Histórico de Pedidos")

        print("  0. Voltar ao Menu Principal")


        opcao = ler_opcao(["1", "2", "3", "4", "0"])

        if opcao == "1":
            pedido_novo()

        elif opcao == "2":
            pedido_rastrear()
        elif opcao == "3":
            pedido_cancelar()
            
        elif opcao == "4":
            pedido_historico()
        elif opcao == "0":
            break   # sobe para camada 1

def menu_geral():
    """Loop principal do ChatBot."""
    print("\n" + "═" * 40)

    print("   🤖  ChatBot de Atendimento ao Cliente")

    print("═" * 40)

    print("   Olá! Bem-vindo(a) ao nosso atendimento.")


    while True:
        cabecalho("MENU PRINCIPAL")
        print("  1.   Cadastro e Suporte")

        print("  2. 📋  Informações")
        
        print("  3. 🛒  Pedidos")

        print("  0. ❌  Encerrar Atendimento")


        opcao = ler_opcao(["1", "2", "3", "0"])

        if opcao == "1":
            submenu_cadastro_suporte() # entra na camada 2
        elif opcao == "2":
            submenu_informacoes()      # entra na camada 2
        elif opcao == "3":
            submenu_pedidos()          # entra na camada 2
        elif opcao == "0":
            linha()
            print("  Obrigado pelo contato. Até logo! 👋")
            linha()
            break   # encerra o programa

if __name__ == "__main__":
    menu_geral()