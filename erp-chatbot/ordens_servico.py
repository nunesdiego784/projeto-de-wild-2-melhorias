from validacoes import cabecalho, linha, pausar
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
