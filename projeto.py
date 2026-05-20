

# Cadastro de entregadores
"""
nome = input("Digite o nome do entregador ")
veiculo = input("Digite o veiculo ")

"""
# entregadores = {1:["Pedro", "Moto", "Disponibilidade","Pedidos a serem entregues"], 2:["Claudia", "Carro", "Ocupada","3"]}
entregadores = {
    1000: {"nome": "Pedro", "veiculo": "Moto", "disponibilidade": "livre", "pedidos": "Nenhum"},
    1001: {"nome": "Claudia", "veiculo": "Carro", "disponibilidade": "Ocupada", "pedidos": "3"}
}


x = int(input("Digite o ID: "))
if x not in entregadores:
    print("ID não encontrado.")
else:
    y = input("Digite o que você quer ver (nome, veiculo, disponibilidade, pedidos): ").strip().lower()

    match y:
        case _ if y.startswith("nom") or y.endswith("me"):
            print(f"Nome: {entregadores[x]['nome']}")
        case _ if y.startswith("vei") or y.endswith("ulo"):
            print(f"Veículo: {entregadores[x]['veiculo']}")
        case _ if y.startswith("dis") or y.endswith("dade"):
            print(f"Disponibilidade: {entregadores[x]['disponibilidade']}")
        case _ if y.startswith("ped") or y.endswith("dos"):
            print(f"Pedidos: {entregadores[x]['pedidos']}")
        case _:
            print("Opção não reconhecida.")

