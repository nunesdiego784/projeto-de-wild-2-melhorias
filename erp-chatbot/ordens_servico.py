from validacoes import cabecalho, linha, pausar

def pedido_novo(pedidos, clientes, produtos):
    cabecalho("Realizar Novo Pedido")
    
    # 1. PERGUNTA O CPF DO COMPRADOR E VALIDA SE ELE EXISTE
    cpf_comprador = input("  Digite o CPF do cliente comprador: ").strip()
    cliente_encontrado = None
    
    for cliente in clientes:
        if cliente["cpf"] == cpf_comprador:
            cliente_encontrado = cliente
            break
            
    if not cliente_encontrado:
        print("\n   AVISO: Cliente não cadastrado! Cadastre o cliente primeiro.")
        pausar()
        return

    # 2. MOSTRA A LISTA DE PRODUTOS CADASTRADOS NO MAIN.PY
    print(f"\n   Cliente: {cliente_encontrado['nome']}")
    print("   === PRODUTOS DISPONÍVEIS ===")
    for prod in produtos:
        print(f"   [{prod['codigo']}] {prod['nome']} - R$ {prod['preco']:.2f} (Estoque: {prod['estoque']})")
    linha()

    # 3. SELECIONA O PRODUTO PELO CÓDIGO
    try:
        codigo_escolhido = int(input("   Digite o CÓDIGO do produto desejado: ").strip())
    except ValueError:
        print("   AVISO: Código inválido! Use apenas números.")
        pausar()
        return

    produto_encontrado = None
    for prod in produtos:
        if prod["codigo"] == codigo_escolhido:
            produto_encontrado = prod
            break

    if not produto_encontrado:
        print("   AVISO: Produto não encontrado!")
        pausar()
        return

    # 4. PEDE A QUANTIDADE E VALIDA O ESTOQUE
    try:
        qtd = int(input(f"   Quantidade de '{produto_encontrado['nome']}': ").strip())
    except ValueError:
        print("   AVISO: Quantidade inválida! Use apenas números.")
        pausar()
        return

    if qtd <= 0:
        print("   AVISO: A quantidade deve ser maior que zero.")
        pausar()
        return

    if qtd > produto_encontrado["estoque"]:
        print(f"   AVISO: Estoque insuficiente! Temos apenas {produto_encontrado['estoque']} unidades.")
        pausar()
        return

    # 5. ATUALIZA O ESTOQUE E CRIA O DICIONÁRIO COMPLETO
    produto_encontrado["estoque"] -= qtd
    total_compra = qtd * produto_encontrado["preco"]
    id_gerado = len(pedidos) + 1

    novo_pedido = {
        "codigo": id_gerado,
        "cpf_cliente": cliente_encontrado["cpf"],
        "nome_cliente": cliente_encontrado["nome"],
        "id_produto": produto_encontrado["codigo"],
        "nome_produto": produto_encontrado["nome"],
        "quantidade": qtd,
        "total": total_compra,
        "status": "Aguardando confirmação"
    }

    # ADICIONA TUDO NA LISTA DO MAIN.PY
    pedidos.append(novo_pedido)

    print(f"\n   Pedido #{id_gerado} registrado com sucesso!")
    print(f"      Produto: {novo_pedido['nome_produto']} (Qtd: {novo_pedido['quantidade']})")
    print(f"      Total  : R$ {novo_pedido['total']:.2f}")
    pausar()

def pedido_rastrear(pedidos):
    cabecalho("Rastrear Pedido")
    
    if not pedidos:
        print("   AVISO: Nenhum pedido foi registrado no sistema ainda.")
        pausar()
        return

    try:
        codigo_busca = int(input("  Digite o número/código do pedido: ").strip())
    except ValueError:
        print("   AVISO: Código inválido! Use apenas números.")
        pausar()
        return

    # Procura o pedido na lista global
    pedido_encontrado = None
    for p in pedidos:
        if p["codigo"] == codigo_busca:
            pedido_encontrado = p
            break

    if pedido_encontrado:
        print(f"\n   Pedido #{pedido_encontrado['codigo']} encontrado!")
        print(f"     Cliente      : {pedido_encontrado['nome_cliente']}")
        print(f"     Produto      : {pedido_encontrado['nome_produto']} (Qtd: {pedido_encontrado['quantidade']})")
        print(f"     Valor Total  : R$ {pedido_encontrado['total']:.2f}")
        print(f"     Status atual : {pedido_encontrado['status']}")
    else:
        print("   AVISO: Pedido não encontrado. Verifique o número.")
    
    pausar()


def pedido_cancelar(pedidos):
    cabecalho("Cancelar Pedido")
    
    if not pedidos:
        print("   AVISO: Nenhum pedido foi registrado no sistema ainda.")
        pausar()
        return

    try:
        codigo_busca = int(input("  Digite o número do pedido a cancelar: ").strip())
    except ValueError:
        print("   AVISO: Código inválido! Use apenas números.")
        pausar()
        return

    # Procura o pedido na lista global
    pedido_encontrado = None
    for p in pedidos:
        if p["codigo"] == codigo_busca:
            pedido_encontrado = p
            break

    if pedido_encontrado:
        # Se o pedido já estiver cancelado, avisa o usuário
        if pedido_encontrado["status"] == "Cancelado":
            print("   AVISO: Este pedido já se encontra cancelado.")
            pausar()
            return

        print(f"\n   Pedido #{pedido_encontrado['codigo']} - {pedido_encontrado['nome_produto']}")
        confirma = input(f"  Confirmar cancelamento deste pedido? (s/n): ").strip().lower()
        
        if confirma == "s":
            # Altera o status do dicionário real dentro da lista!
            pedido_encontrado["status"] = "Cancelado"
            print("   Pedido cancelado com sucesso.")
        else:
            print("   Cancelamento abortado.")
    else:
        print("   AVISO: Pedido não encontrado.")
        
    pausar()

def pedido_historico(pedidos):
    cabecalho("Histórico de Pedidos")
    
    if not pedidos:
        print("   Nenhum pedido registrado no sistema ainda.")
        pausar()
        return

    print(f"  {'Nº':<5} {'Cliente':<15} {'Produto':<25} {'Qtd':<5} {'Total':<10} {'Status'}")
    linha()
    
    for p in pedidos:
        print(f"  {p['codigo']:<5} {p['nome_cliente']:<15} {p['nome_produto']:<25} {p['quantidade']:<5} R$ {p['total']:<8.2f} {p['status']}")
    
    print()
    pausar()