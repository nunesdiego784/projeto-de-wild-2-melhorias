import unicodedata
from validacoes import cabecalho, linha, pausar


def _normalizar(texto):
    """Remove acentos e converte para minúsculas para facilitar a busca."""
    return unicodedata.normalize('NFKD', texto).encode('ascii', 'ignore').decode('ascii').lower()


def _proximo_codigo(pedidos):
    if not pedidos:
        return 1
    return max(p["codigo"] for p in pedidos) + 1


def pedido_novo(pedidos, clientes, produtos):
    cabecalho("Realizar Novo Pedido")

    # 1. Valida cliente pelo CPF
    cpf_comprador = input("  CPF do cliente comprador: ").strip()
    cliente_encontrado = None
    for c in clientes:
        if c["cpf"] == cpf_comprador:
            cliente_encontrado = c
            break

    if not cliente_encontrado:
        print("\n   BLOQUEADO: cliente não cadastrado. Cadastre o cliente primeiro.")
        pausar()
        return

    # 2. Busca produto por palavra-chave
    print(f"\n  Cliente: {cliente_encontrado['nome']}")

    produto_encontrado = None
    print("  Produtos disponíveis para compra:")
    linha()
    for prod in produtos:
        print(f"  {prod['nome']} - R$ {prod['preco']:.2f} (Estoque: {prod['estoque']})")
        linha()

    while not produto_encontrado:
        busca = input("\n  Digite o nome ou palavra-chave do produto (ou 'sair'): ").strip().lower()

        if busca == "sair":
            print("  Pedido cancelado.")
            pausar()
            return

        if not busca:
            print("   Digite ao menos uma palavra-chave.")
            continue

        # Filtra produtos cujo nome contenha qualquer palavra da busca (ignora acentos)
        palavras = _normalizar(busca).split()
        resultados = [
            p for p in produtos
            if any(palavra in _normalizar(p["nome"]) for palavra in palavras)
        ]

        if not resultados:
            print(f"   Nenhum produto encontrado para '{busca}'. Tente outra palavra.")
            continue

        # Exibe os resultados encontrados
        print(f"\n  {len(resultados)} produto(s) encontrado(s):")
        linha()
        for i, prod in enumerate(resultados, 1):
            print(f"  [{i}] {prod['nome']} - R$ {prod['preco']:.2f} (Estoque: {prod['estoque']})")
        linha()

        # Usuário sempre escolhe pelo número da lista
        while True:
            try:
                escolha = input(f"  Escolha o número do produto (1-{len(resultados)}) ou 0 para buscar novamente: ").strip()
                num = int(escolha)
                if num == 0:
                    break
                if 1 <= num <= len(resultados):
                    produto_encontrado = resultados[num - 1]
                    break
                print(f"   Número inválido. Digite entre 1 e {len(resultados)}.")
            except ValueError:
                print("   Digite apenas o número da opção.")

    # 3. Quantidade e estoque
    try:
        qtd = int(input(f"  Quantidade de '{produto_encontrado['nome']}': ").strip())
    except ValueError:
        print("   Quantidade inválida! Use apenas números.")
        pausar()
        return

    if qtd <= 0:
        print("   A quantidade deve ser maior que zero.")
        pausar()
        return

    if qtd > produto_encontrado["estoque"]:
        print(f"   BLOQUEADO: estoque insuficiente! Disponível: {produto_encontrado['estoque']} unidade(s).")
        pausar()
        return

    # 4. Registra pedido
    produto_encontrado["estoque"] -= qtd
    total_compra = qtd * produto_encontrado["preco"]
    novo_codigo = _proximo_codigo(pedidos)

    novo_pedido = {
        "codigo": novo_codigo,
        "id_cliente": cliente_encontrado["id_cliente"],
        "cpf_cliente": cliente_encontrado["cpf"],
        "nome_cliente": cliente_encontrado["nome"],
        "id_produto": produto_encontrado["codigo"],
        "nome_produto": produto_encontrado["nome"],
        "quantidade": qtd,
        "total": total_compra,
        "status": "Aguardando confirmação",
    }
    pedidos.append(novo_pedido)

    print(f"\n   Pedido #{novo_codigo} registrado com sucesso!")
    print(f"      Produto: {novo_pedido['nome_produto']} (Qtd: {novo_pedido['quantidade']})")
    print(f"      Total  : R$ {novo_pedido['total']:.2f}")
    pausar()


def pedido_rastrear(pedidos):
    cabecalho("Rastrear Pedidos por CPF")

    if not pedidos:
        print("   Nenhum pedido registrado no sistema ainda.")
        pausar()
        return

    cpf_busca = input("  CPF do cliente: ").strip()

    pedidos_cliente = [p for p in pedidos if p["cpf_cliente"] == cpf_busca]

    if not pedidos_cliente:
        print("   Nenhum pedido encontrado para este CPF.")
        pausar()
        return

    nome_cliente = pedidos_cliente[-1]["nome_cliente"]
    print(f"\n  Cliente: {nome_cliente}")
    print(f"  Total de pedido(s) encontrado(s): {len(pedidos_cliente)}")

    # Separa o mais recente dos anteriores
    mais_recente = pedidos_cliente[-1]
    anteriores   = pedidos_cliente[:-1]

    # ── Pedido atual ──────────────────────────────────────
    linha()
    print("  PEDIDO ATUAL")
    linha()
    print(f"  Nº        : #{mais_recente['codigo']}")
    print(f"  Produto   : {mais_recente['nome_produto']} (Qtd: {mais_recente['quantidade']})")
    print(f"  Total     : R$ {mais_recente['total']:.2f}")
    print(f"  Status    : {mais_recente['status']}")

    # ── Pedidos anteriores ────────────────────────────────
    if anteriores:
        linha()
        print("  PEDIDOS ANTERIORES")
        linha()
        print(f"  {'Nº':<6} {'Produto':<26} {'Qtd':<5} {'Total':<11} Status")
        linha()
        for p in reversed(anteriores):
            print(f"  #{p['codigo']:<5} {p['nome_produto']:<26} {p['quantidade']:<5} "
                  f"R$ {p['total']:<8.2f} {p['status']}")

    linha()
    pausar()


def pedido_cancelar(pedidos):
    cabecalho("Cancelar Pedido")
    if not pedidos:
        print("   Nenhum pedido registrado no sistema ainda.")
        pausar()
        return

    try:
        codigo_busca = int(input("  Número do pedido a cancelar: ").strip())
    except ValueError:
        print("   Código inválido! Use apenas números.")
        pausar()
        return

    pedido_encontrado = None
    for p in pedidos:
        if p["codigo"] == codigo_busca:
            pedido_encontrado = p
            break

    if not pedido_encontrado:
        print("   Pedido não encontrado.")
        pausar()
        return

    if pedido_encontrado["status"] == "Cancelado":
        print("   Este pedido já se encontra cancelado.")
        pausar()
        return

    print(f"\n   Pedido #{pedido_encontrado['codigo']} - {pedido_encontrado['nome_produto']}")
    confirma = input("  Confirmar cancelamento? (s/n): ").strip().lower()
    if confirma == "s":
        pedido_encontrado["status"] = "Cancelado"
        print("   Pedido cancelado com sucesso.")
    else:
        print("   Cancelamento abortado.")
    pausar()


def pedido_historico(pedidos, clientes):
    """Lista todos os pedidos traduzindo id_cliente para o nome atual na matriz."""
    cabecalho("Histórico de Pedidos")
    if not pedidos:
        print("   Nenhum pedido registrado no sistema ainda.")
        pausar()
        return

    # Monta índice id_cliente → nome para exibição dinâmica
    indice_clientes = {c["id_cliente"]: c["nome"] for c in clientes}

    print(f"  {'Nº':<5} {'Cliente':<22} {'Produto':<24} {'Qtd':<5} {'Total':<10} {'Status'}")
    linha()
    for p in pedidos:
        nome_cli = indice_clientes.get(p["id_cliente"], f"(ID {p['id_cliente']} removido)")
        print(f"  {p['codigo']:<5} {nome_cli:<22} {p['nome_produto']:<24} "
              f"{p['quantidade']:<5} R$ {p['total']:<7.2f} {p['status']}")
    print()
    pausar()
