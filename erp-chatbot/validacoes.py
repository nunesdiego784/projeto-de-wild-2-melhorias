
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