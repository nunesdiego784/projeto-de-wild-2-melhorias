from validacoes import cabecalho, linha, pausar, ler_opcao


def cadastro_novo_cliente(clientes):
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
    
    cpf_busca = input("Digite o CPF do cliente que deseja alterar: ").strip()
    cliente_encontrado = None

    for cliente in clientes:
        if cliente["cpf"] == cpf_busca:
            cliente_encontrado = cliente
            break 

    if cliente_encontrado:
        print(f"\n Cliente encontrado: {cliente_encontrado['nome']} (CPF: {cliente_encontrado['cpf']})")
        
        while True:
            novo_nome = input("\nDigite o novo nome (deixe em branco para manter): ").strip()
            if not novo_nome:
                print("-> Mantendo o nome atual.")
                break 
            
            if len(novo_nome) >= 3:
                cliente_encontrado["nome"] = novo_nome
                print("-> Nome atualizado com sucesso!")
                break
            else:
                print(" Nome muito curto! O nome deve ter pelo menos 3 caracteres.")

        # VALIDAÇÃO DO NOVO CPF
        while True:
            novo_cpf = input("\nDigite o novo CPF (deixe em branco para manter): ").strip()
            if not novo_cpf:
                print("-> Mantendo o CPF atual.")
                break 

            if len(novo_cpf) == 11 and novo_cpf.isdigit():
                # Verifica se o novo CPF já não pertence a OUTRA pessoa
                cpf_ja_existe = False
                for c in clientes:
                    if c["cpf"] == novo_cpf:
                        cpf_ja_existe = True
                        break
                
                if cpf_ja_existe:
                    print(" Erro: Este CPF já está cadastrado para outro cliente!")
                else:
                    cliente_encontrado["cpf"] = novo_cpf
                    print("-> CPF atualizado com sucesso!")
                    break
            else:
                print(" CPF inválido! Digite exatamente 11 números (apenas dígitos).")

        print("\n=== Processo de alteração finalizado! ===")

    else:
        print("\n❌ Cliente não encontrado. Verifique o CPF e tente novamente.")

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

def cadastro_novo_cliente(clientes):  
    cabecalho("Cadastrar Novo Cliente")
    print("  Informe os dados abaixo:")
    nome = input("  Nome completo : ").strip()
    cpf = input("  CPF           : ").strip()

    novo_cliente = {"nome": nome, "cpf": cpf}
    
    clientes.append(novo_cliente)  
    
    print(f"\n   Cliente '{nome}' cadastrado com sucesso!")
    print(f"      CPF: {cpf}")
    pausar()
