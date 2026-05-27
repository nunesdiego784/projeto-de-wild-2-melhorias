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
     break