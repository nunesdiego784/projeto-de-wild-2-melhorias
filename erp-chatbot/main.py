def menu_geral():
    """Loop principal do ChatBot."""
    print("\n" + "═" * 40)
    print("   🤖  ChatBot de Atendimento ao Cliente")
    print("═" * 40)
    print("   Olá! Bem-vindo(a) ao nosso atendimento.")

    while True:
        cabecalho("MENU PRINCIPAL")
        print("  1. 📋  Informações")
        print("  2. 🛒  Pedidos")
        print("  0. ❌  Encerrar Atendimento")

        opcao = ler_opcao(["1", "2", "0"])

        if opcao == "1":
            submenu_informacoes()      # entra na camada 2
        elif opcao == "2":
            submenu_pedidos()          # entra na camada 2
        elif opcao == "0":
            linha()
            print("  Obrigado pelo contato. Até logo! 👋")
            linha()
            break   # encerra o programa

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