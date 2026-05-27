"""
ChatBot de Atendimento ao Cliente
Etapa 2 — Menu Geral, Submenus e Loop
Estrutura: 3 camadas de loop
  Camada 1: Loop principal (Menu Geral)
  Camada 2: Loop de submenu (Informações / Pedidos)
  Camada 3: Loop de ação (executa e volta ao submenu)
"""


def linha ():

    print('-' * 50)

def cabecalho (titulo: str) :
    linha()
    print(titulo)
    linha()

def pausar():
    input('Pressione Enter para continuar...')

def ler_opcao(opcoes_validas: list[str])-> str:
    """le a entrada do usuario e retorna a opcao escolhiada"""
    while True:
            escolha = int(input('Digite sua opção: '))
    if escolha in opcoes_validas:
            return escolha
print('Opção inválida. Tente novamente.')