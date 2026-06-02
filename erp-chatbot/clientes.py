from validacoes import cabecalho, linha, pausar, ler_opcao


def _cpf_duplicado(clientes, cpf, ignorar_id=None):
    """Retorna True se o CPF já existe em outro cliente."""
    for c in clientes:
        if c["cpf"] == cpf and c["id_cliente"] != ignorar_id:
            return True
    return False


def _proximo_id(clientes):
    if not clientes:
        return 1
    return max(c["id_cliente"] for c in clientes) + 1


def cadastro_novo_cliente(clientes):
    cabecalho("Cadastrar Novo Cliente")
    print("  Informe os dados abaixo:")

    # Nome obrigatório
    while True:
        nome = input("  Nome completo : ").strip()
        if len(nome) >= 3:
            break
        print("   Erro: nome deve ter pelo menos 3 caracteres.")

    # CPF obrigatório e sem duplicata
    while True:
        cpf = input("  CPF (11 dígitos): ").strip()
        if not (len(cpf) == 11 and cpf.isdigit()):
            print("   Erro: CPF deve ter exatamente 11 dígitos numéricos.")
            continue
        if _cpf_duplicado(clientes, cpf):
            print("   Erro: este CPF já está cadastrado.")
            continue
        break

    telefone = input("  Telefone (opcional): ").strip()
    novo_id = _proximo_id(clientes)

    novo_cliente = {
        "id_cliente": novo_id,
        "nome": nome,
        "cpf": cpf,
        "telefone": telefone,
        "ativo": True,
    }
    clientes.append(novo_cliente)
    print(f"\n   Cliente '{nome}' cadastrado com sucesso! (ID: {novo_id})")
    pausar()


def listar_clientes(clientes):
    cabecalho("Lista de Clientes")
    if not clientes:
        print("  Nenhum cliente cadastrado.")
        pausar()
        return
    print(f"  {'ID':<5} {'Nome':<25} {'CPF':<13} {'Telefone':<16} {'Ativo'}")
    linha()
    for c in clientes:
        ativo = "Sim" if c["ativo"] else "Não"
        print(f"  {c['id_cliente']:<5} {c['nome']:<25} {c['cpf']:<13} {c.get('telefone',''):<16} {ativo}")
    print()
    pausar()


def alterar_cliente(clientes):
    cabecalho("Alterar Dados do Cliente")
    cpf_busca = input("  CPF do cliente que deseja alterar: ").strip()
    cliente_encontrado = None
    for c in clientes:
        if c["cpf"] == cpf_busca:
            cliente_encontrado = c
            break

    if not cliente_encontrado:
        print("  Cliente não encontrado. Verifique o CPF.")
        pausar()
        return

    print(f"\n  Cliente: {cliente_encontrado['nome']} (ID: {cliente_encontrado['id_cliente']})")

    # Novo nome
    while True:
        novo_nome = input("\n  Novo nome (Enter para manter): ").strip()
        if not novo_nome:
            print("  → Nome mantido.")
            break
        if len(novo_nome) >= 3:
            cliente_encontrado["nome"] = novo_nome
            print("  → Nome atualizado.")
            break
        print("   Erro: nome deve ter pelo menos 3 caracteres.")

    # Novo CPF
    while True:
        novo_cpf = input("  Novo CPF (Enter para manter): ").strip()
        if not novo_cpf:
            print("  → CPF mantido.")
            break
        if not (len(novo_cpf) == 11 and novo_cpf.isdigit()):
            print("   Erro: CPF deve ter 11 dígitos numéricos.")
            continue
        if _cpf_duplicado(clientes, novo_cpf, ignorar_id=cliente_encontrado["id_cliente"]):
            print("   Erro: este CPF já pertence a outro cliente.")
            continue
        cliente_encontrado["cpf"] = novo_cpf
        print("  → CPF atualizado.")
        break

    print("\n  Alteração finalizada!")
    pausar()


def excluir_cliente(clientes, pedidos):
    """Bloqueia exclusão se o cliente tiver pedidos vinculados."""
    cabecalho("Excluir Cliente")
    cpf = input("  CPF do cliente que deseja excluir: ").strip()

    cliente_encontrado = None
    for c in clientes:
        if c["cpf"] == cpf:
            cliente_encontrado = c
            break

    if not cliente_encontrado:
        print("  Cliente não encontrado. Verifique o CPF.")
        pausar()
        return

    # ── TRAVA DE INTEGRIDADE ──────────────────────────────────────────
    id_cli = cliente_encontrado["id_cliente"]
    pedidos_vinculados = [p for p in pedidos if p["id_cliente"] == id_cli]
    if pedidos_vinculados:
        print(f"\n   BLOQUEADO: o cliente '{cliente_encontrado['nome']}' possui "
              f"{len(pedidos_vinculados)} pedido(s) vinculado(s).")
        print("   Cancele ou remova os pedidos antes de excluir o cliente.")
        pausar()
        return
    # ──────────────────────────────────────────────────────────────────

    print(f"  Cliente encontrado: {cliente_encontrado['nome']} (CPF: {cliente_encontrado['cpf']})")
    confirma = input("  Confirmar exclusão? (s/n): ").strip().lower()
    if confirma == "s":
        clientes.remove(cliente_encontrado)
        print("  Cliente excluído com sucesso!")
    else:
        print("  Exclusão cancelada.")
    pausar()


def suporte_cliente():
    cabecalho("Suporte ao Cliente")
    print("  Para suporte, entre em contato pelos canais abaixo:")
    print("  - Telefone: 4022-8922")
    print("  - E-mail  : suporte@casadecampocentral.com")
    pausar()


def submenu_cadastro_suporte(clientes, pedidos):
    while True:
        cabecalho("  Cadastro e Suporte")
        print("  1. Cadastrar Novo Cliente")
        print("  2. Listar Clientes")
        print("  3. Alterar Dados do Cliente")
        print("  4. Excluir Cliente")
        print("  5. Suporte ao Cliente")
        print("  0. Voltar ao Menu Principal")

        opcao = ler_opcao(["1", "2", "3", "4", "5", "0"])

        if opcao == "0":
            break
        elif opcao == "1":
            cadastro_novo_cliente(clientes)
        elif opcao == "2":
            listar_clientes(clientes)
        elif opcao == "3":
            alterar_cliente(clientes)
        elif opcao == "4":
            excluir_cliente(clientes, pedidos)   # passa pedidos para a trava
        elif opcao == "5":
            suporte_cliente()
