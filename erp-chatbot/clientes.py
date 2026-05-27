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