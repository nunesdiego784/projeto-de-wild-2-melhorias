from validacoes import cabecalho, linha, pausar, ler_opcao


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

def alterar_cliente(clientes):
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

    # Só chega aqui se nenhum cliente foi encontrado
    print("Cliente não encontrado. Verifique o CPF e tente novamente.")


def excluir_cliente(clientes):
    cabecalho("Excluir Cliente")
    cpf = input("Digite o CPF do cliente que deseja excluir: ").strip()

    for cliente in clientes:
        if cliente["cpf"] == cpf:
            print(f"Cliente encontrado: {cliente['nome']} (CPF: {cliente['cpf']})")
            confirma = input("Confirmar exclusão deste cliente? (s/n): ").strip().lower()
            if confirma == "s":
                clientes.remove(cliente)
                print("Cliente excluído com sucesso!")
            else:
                print("Exclusão cancelada.")
            return

    # Só chega aqui se nenhum cliente foi encontrado
    print("Cliente não encontrado. Verifique o CPF e tente novamente.")


def suporte_cliente():
    cabecalho("Suporte ao Cliente")
    print("  Para suporte, por favor entre em contato conosco através dos seguintes canais:")
    print("  - Telefone: (11) 1234-5678")
    print("  - E-mail: suporte@empresa.com")
    pausar()

def submenu_cadastro_suporte(clientes):
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
            cadastro_novo_cliente(clientes)
        elif opcao == "2":
            alterar_cliente(clientes)
        elif opcao == "3":
            excluir_cliente(clientes)
        elif opcao == "4":
            suporte_cliente()   


clientes = []

def cadastramento_de_cliente():
    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")

    novo_cliente = {
        "nome": nome,
        "cpf": cpf
    }

    clientes.append(novo_cliente)

    print("Cliente cadastrado com sucesso!")

# Chamando a função
cadastramento_de_cliente()

# Mostrando os clientes cadastrados
print(clientes)