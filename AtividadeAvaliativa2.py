import random

pedidos = {}
entregadores = {}
id_entregador_int = 999


def barra():
    print("-" * 70)


def gerar_id_pedido():
    while True:
        numero = random.randint(1000, 9999)
        id_pedido = "A" + str(numero)

        if id_pedido not in pedidos:
            return id_pedido


def menu():

    barra()
    print(" Sistema de logística urbana FluxoNorte ")
    barra()

    print(f"\n1-Cadastro de Entregadores/Pedidos\n2-Atualizar Pedidos\n3-Consulta\n4-Relatórios\n5-Desenvolvedores\n6-Encerrar Sistema")

    try:
        opc = int(input("--> "))
    except ValueError:
        print("Digite apenas números!")
        return menu()

    match opc:

        case 1:
            menu_cadastro()
            return menu()

        case 2:
            menu_atualizacao()
            return menu()

        case 3:
            menu_consultas()
            return menu()

        case 4:
            relatorios()
            return menu()

        case 5:
            print(f"\nJúlia Andrade Guarnieri\nLarissa Souza Quito Sampaio\nPedro Henrique Sanches Agatti Godoy")
            input("Pressione ENTER...")
            return menu()

        case 6:
            print("Sistema encerrado.")
            return False

        case _:
            print("Opção inválida!")
            return menu()

def menu_cadastro():

    print("\n1-Cadastrar Entregador\n2-Cadastrar Pedido\n3-Voltar")

    try:
        opc = int(input("--> "))
    except ValueError:
        print("Digite apenas números!")
        return menu_cadastro()

    match opc:

        case 1:
            cadastro_entregador()
            return menu_cadastro()

        case 2:
            cadastro_pedido()
            return menu_cadastro()

        case 3:
            return

        case _:
            print("Opção inválida!")
            return menu_cadastro()


def menu_atualizacao():

    print(f"\n1-Alterar Status\n2-Cancelar Pedido\n3-Associar Entregador\n4-Remover Entregador\n5-Voltar")

    opc = input("--> ")

    match opc:

        case "1":
            alterar_status()

        case "2":
            cancelar_pedido()

        case "3":
            associar_entregador()

        case "4":
            remover_entregador()

        case "5":
            return

        case _:
            print("Opção inválida!")


def menu_consultas():

    print(f"\n1-Pedidos Pendentes\n2 Pedidos Entregues\n3-Buscar Pedido por ID\n4-Entregadores Disponíveis\n5-Entregas por Entregador\n6-Voltar")

    opc = input("--> ")

    match opc:

        case "1":
            listar_pendentes()

        case "2":
            listar_entregues()

        case "3":
            buscar_pedido()

        case "4":
            entregadores_disponiveis()

        case "5":
            entregas_entregador()

        case "6":
            return

        case _:
            print("Opção inválida!")


def cadastro_entregador():

    global id_entregador_int

    id_entregador_int += 1
    id_entregador = str(id_entregador_int)

    print(f"\nID gerado: {id_entregador}")

    nome = input("Nome do entregador: ")

    for dados in entregadores.values():

        if dados["nome"].lower() == nome.lower():
            print("Entregador já cadastrado!")
            return

    veiculo = ""
    while veiculo not in ["carro", "van", "moto"]:
        veiculo = input("Veículo (carro/van/moto): ").lower()

        if veiculo not in ["carro", "van", "moto"]:
            print("Veículo inválido!")

    disponibilidade = ""
    while disponibilidade not in ["sim", "não", "nao", "s", "n"]:
        disponibilidade = input("Disponível? (sim/não): ").lower()

        if disponibilidade not in ["sim", "não", "nao", "s", "n"]:
            print("Resposta inválida!")

    entregadores[id_entregador] = {"nome": nome, "veiculo": veiculo,"pedidos": [],"disponibilidade": disponibilidade}

    print("Entregador cadastrado com sucesso!")


def cadastro_pedido():

    if len(entregadores) == 0:
        print("Cadastre um entregador primeiro!")
        return

    id_pedido = gerar_id_pedido()

    print(f"\nID do pedido: {id_pedido}")

    cliente = input("Nome do cliente: ")

    endereco = input("Endereço: ")

    prioridade = ""

    while prioridade not in ["Alta", "Normal"]:

        prioridade = input("Prioridade (Alta/Normal): ").capitalize()

        if prioridade not in ["Alta", "Normal"]:
            print("Prioridade inválida!")

    descricao = input("Descrição do pedido: ")

    status = ""

    while status not in ["Pendente", "Em Rota", "Entregue", "Cancelado"]:
        status = input("Status (Pendente/Em Rota/Entregue/Cancelado): ").title()

        if status not in ["Pendente", "Em Rota", "Entregue", "Cancelado"]:
            print("Status inválido!")

    id_entregador = input("ID do entregador: ")

    if id_entregador not in entregadores:
        print("Entregador inexistente!")
        return

    if len(entregadores[id_entregador]["pedidos"]) >= 5:
        print("Esse entregador já atingiu o limite de pedidos!")
        return

    pedidos[id_pedido] = { "cliente": cliente, "endereco": endereco, "prioridade": prioridade,"descricao": descricao,"status": status,"entregador": id_entregador}

    entregadores[id_entregador]["pedidos"].append(id_pedido)

    print("Pedido cadastrado com sucesso!")

def alterar_status():

    id_pedido = input("Digite o ID do pedido: ")

    if id_pedido not in pedidos:
        print("Pedido não encontrado!")
        return

    print("\n1-Pendente\n2-Em Rota\n3-Entregue\n4-Cancelado")

    opc = input("--> ")

    match opc:

        case "1":
            pedidos[id_pedido]["status"] = "Pendente"

        case "2":
            pedidos[id_pedido]["status"] = "Em Rota"

        case "3":
            pedidos[id_pedido]["status"] = "Entregue"

        case "4":
            pedidos[id_pedido]["status"] = "Cancelado"

        case _:
            print("Status inválido!")
            return

    print("Status atualizado!")


def cancelar_pedido():

    id_pedido = input("Digite o ID do pedido: ")

    if id_pedido not in pedidos:
        print("Pedido não encontrado!")
        return

    pedidos[id_pedido]["status"] = "Cancelado"

    print("Pedido cancelado!")


def associar_entregador():

    id_pedido = input("ID do pedido: ")
    id_entregador = input("ID do entregador: ")

    if id_pedido not in pedidos:
        print("Pedido inexistente!")
        return

    if id_entregador not in entregadores:
        print("Entregador inexistente!")
        return

    pedidos[id_pedido]["entregador"] = id_entregador

    entregadores[id_entregador]["pedidos"].append(id_pedido)

    print("Entregador associado!")


def remover_entregador():

    id_pedido = input("ID do pedido: ")

    if id_pedido not in pedidos:
        print("Pedido inexistente!")
        return

    id_entregador = pedidos[id_pedido]["entregador"]

    if id_entregador != "Nenhum":
        entregadores[id_entregador]["pedidos"].remove(id_pedido)

    pedidos[id_pedido]["entregador"] = "Nenhum"

    print("Associação removida!")




def listar_pendentes():

    print("\nPEDIDOS PENDENTES\n")

    encontrou = False

    for id_pedido, dados in pedidos.items():

        if dados["status"] == "Pendente":
            print(id_pedido, "-", dados["cliente"])
            encontrou = True

    if encontrou == False:
        print("Nenhum pedido pendente.")


def listar_entregues():

    print("\nPEDIDOS ENTREGUES\n")

    encontrou = False

    for id_pedido, dados in pedidos.items():

        if dados["status"] == "Entregue":
            print(id_pedido, "-", dados["cliente"])
            encontrou = True

    if encontrou == False:
        print("Nenhum pedido entregue.")

def buscar_pedido():

    id_pedido = input("Digite o ID: ")

    if id_pedido not in pedidos:
        print("Pedido não encontrado!")
        return

    print("\nDADOS DO PEDIDO\n")

    for chave, valor in pedidos[id_pedido].items():
        print(f"{chave}: {valor}")


def entregadores_disponiveis():

    print("\nENTREGADORES DISPONÍVEIS\n")

    if len(entregadores) == 0:
        print("Nenhum entregador cadastrado.")
        return

    encontrou = False

    for id_entregador, dados in entregadores.items():

        if dados["disponibilidade"] == "sim":
            print(id_entregador, "-", dados["nome"])
            encontrou = True

    if encontrou == False:
        print("Nenhum entregador disponível.")

def entregas_entregador():

    id_entregador = input("Digite o ID do entregador: ")

    if id_entregador not in entregadores:
        print("Entregador não encontrado!")
        return

    print(f"\nPedidos do entregador {entregadores[id_entregador]['nome']}\n")

    if len(entregadores[id_entregador]["pedidos"]) == 0:
        print("Nenhum pedido associado.")
        return

    for pedido in entregadores[id_entregador]["pedidos"]:
        print(pedido)


def relatorios():

    total = len(pedidos)

    pendentes = 0
    entregues = 0
    cancelados = 0
    alta = 0

    for dados in pedidos.values():

        if dados["status"] == "Pendente":
            pendentes += 1

        elif dados["status"] == "Entregue":
            entregues += 1

        elif dados["status"] == "Cancelado":
            cancelados += 1

        if dados["prioridade"] == "Alta":
            alta += 1

    print("\nRELATÓRIO OPERACIONAL\n")

    print(f"Total de pedidos: {total}")
    print(f"Pedidos pendentes: {pendentes}")
    print(f"Pedidos entregues: {entregues}")
    print(f"Pedidos cancelados: {cancelados}")
    print(f"Pedidos alta prioridade: {alta}")

    maior = 0
    nome = ""

    for dados in entregadores.values():

        qtd = len(dados["pedidos"])

        if qtd > maior:
            maior = qtd
            nome = dados["nome"]

    if nome != "":
        print(f"Entregador com mais entregas: {nome} ({maior})")


menu()
