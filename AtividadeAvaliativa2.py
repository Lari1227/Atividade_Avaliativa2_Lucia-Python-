import random

pedidos = {}
entregadores = {}
id_entregador_int = 999


def barra():
    print("-" * 70)


def gerar_id_pedido():

    valido = False

    while valido == False:

        numero = random.randint(1000, 9999)

        id_pedido = "A" + str(numero)

        if id_pedido not in pedidos:

            valido = True

    return id_pedido


def menu():
    opc = ""

    while opc != "6":
        barra()
        print(" Sistema de logística urbana FluxoNorte ")
        barra()

        print("\n1-Cadastro de Entregadores/Pedidos")
        print("2-Atualizar Pedidos")
        print("3-Consulta")
        print("4-Relatórios")
        print("5-Desenvolvedores")
        print("6-Encerrar Sistema")

        opc = input("--> ")

        if opc == "1" or opc == " 1" or opc == "1 ":
            menu_cadastro()

        elif opc == "2" or opc == " 2" or opc == "2 ":
            menu_atualizacao()

        elif opc == "3" or opc == " 3" or opc == "3 ":
            menu_consultas()

        elif opc == "4" or opc == " 4" or opc == "4 ":
            relatorios()

        elif opc == "5" or opc == " 5" or opc == "5 ":

            print("\nJúlia Andrade Guarnieri")
            print("Larissa Souza Quito Sampaio")
            print("Pedro Henrique Sanches Agatti Godoy")
            input("Pressione ENTER...")

        elif opc == "6" or opc == " 6" or opc == "6 ":
            print("Sistema encerrado.")

        else:
            print("Opção inválida!")

def menu_cadastro():
    opc = ""

    while opc != "3":
        print("\n1-Cadastrar Entregador")
        print("2-Cadastrar Pedido")
        print("3-Voltar")

        opc = input("--> ")

        if opc == "1" or opc == " 1" or opc == "1 ":
            cadastro_entregador()

        elif opc == "2" or opc == " 2" or opc == "2 ":
            cadastro_pedido()

        elif opc == "3" or opc == " 3" or opc == "3 ":
            print("Voltando...")

        else:
            print("Opção inválida!")


def menu_atualizacao():
    opc = ""

    while opc != "5":
        print("\n1-Alterar Status")
        print("2-Cancelar Pedido")
        print("3-Associar Entregador")
        print("4-Remover Entregador")
        print("5-Voltar")

        opc = input("--> ")

        if opc == "1" or opc == " 1" or opc == "1 ":
            alterar_status()

        elif opc == "2" or opc == " 2" or opc == "2 ":
            cancelar_pedido()

        elif opc == "3" or opc == " 3" or opc == "3 ":
            associar_entregador()

        elif opc == "4" or opc == " 4" or opc == "4 ":
            remover_entregador()

        elif opc == "5" or opc == " 5" or opc == "5 ":
            print("Voltando...")

        else:
            print("Opção inválida!")


def menu_consultas():
    opc = ""

    while opc != "7":
        print("\n1-Pedidos Pendentes")
        print("2-Pedidos Entregues")
        print("3-Buscar Pedido por ID")
        print("4-Entregadores Disponíveis")
        print("5-Entregas por Entregador")
        print("6-Listar Todos os Pedidos")
        print("7-Voltar")

        opc = input("--> ")

        if opc == "1" or opc == " 1" or opc == "1 ":
            listar_pendentes()

        elif opc == "2" or opc == " 2" or opc == "2 ":
            listar_entregues()

        elif opc == "3" or opc == " 3" or opc == "3 ":
            buscar_pedido()

        elif opc == "4" or opc == " 4" or opc == "4 ":
            entregadores_disponiveis()

        elif opc == "5" or opc == " 5" or opc == "5 ":
            entregas_entregador()

        elif opc == "6" or opc == " 6" or opc == "6 ":
            listar_todos_pedidos()

        elif opc == "7" or opc == " 7" or opc == "7 ":
            print("Voltando...")

        else:
            print("Opção inválida!")


def cadastro_entregador():

    global id_entregador_int

    id_entregador_int += 1
    id_entregador = str(id_entregador_int)

    print(f"\nID gerado: {id_entregador}")

    nome = input("Nome do entregador: ")

    if nome == "":
        print("Nome inválido!")
        return

    for id_e in entregadores:
        if entregadores[id_e]["nome"].lower() == nome.lower():
            print("Já existe esse entregador!")
            return
    
    print("\n Escolha um veículo: ")
    print("1-Carro")
    print("2-Van")
    print("3-Moto")
    
    opc_veiculo = input("--> ")
    if opc_veiculo == "1":
        veiculo = "carro"
    elif opc_veiculo == "2":
        veiculo = "van"
    elif opc_veiculo == "3":
        veiculo = "moto"
    else:
        print("Opção inválida!")
        return
    
    print("\nDisponibilidade:")
    print("1-Sim")
    print("2-Não")
    opc_disp = input("--> ")
    if opc_disp == "1" or opc_disp == " 1" or opc_disp == "1 ":
        disponibilidade = "sim"
    elif opc_disp == "2" or opc_disp == " 2" or opc_disp == "2 ":
        disponibilidade = "não"
    else:
        print("Opção inválida!")
        return

    entregadores[id_entregador] = {"nome": nome, "veiculo": veiculo,"pedidos": [],"disponibilidade": disponibilidade}

    print("Entregador cadastrado com sucesso!")


def cadastro_pedido():

    if len(entregadores) == 0:
        print("Cadastre um entregador primeiro!")
        return

    id_pedido = gerar_id_pedido()

    print(f"\nID do pedido: {id_pedido}")

    cliente = ""

    while cliente == "":
        cliente = input("Nome do cliente: ")

    endereco = input("Endereço: ")

    print("\nEscolha a prioridade:")
    print("1-Alta")
    print("2-Normal")

    opc_prioridade = input("--> ")

    if opc_prioridade == "1" or opc_prioridade == " 1" or opc_prioridade == "1 ":
        prioridade = "Alta"

    elif opc_prioridade == "2" or opc_prioridade == " 2" or opc_prioridade == "2 ":
        prioridade = "Normal"

    else:
        print("Opção inválida!")
        return

    descricao = input("Descrição do pedido: ")

    print("\nEscolha o status:")
    print("1-Pendente")
    print("2-Em Rota")
    print("3-Entregue")
    print("4-Cancelado")

    opc_status = input("--> ")

    if opc_status == "1" or opc_status == " 1" or opc_status == "1 ":
        status = "Pendente"

    elif opc_status == "2" or opc_status == " 2" or opc_status == "2 ":
        status = "Em Rota"

    elif opc_status == "3" or opc_status == " 3" or opc_status == "3 ":
        status = "Entregue"

    elif opc_status == "4" or opc_status == " 4" or opc_status == "4 ":
        status = "Cancelado"

    else:
        print("Opção inválida!")
        return

    id_entregador = input("ID do entregador: ")

    if id_entregador not in entregadores:
        print("Entregador inexistente!")
        return

    if len(entregadores[id_entregador]["pedidos"]) >= 5:
        print("Esse entregador já atingiu o limite de pedidos!")
        return

    pedidos[id_pedido] = {
        "cliente": cliente,
        "endereco": endereco,
        "prioridade": prioridade,
        "descricao": descricao,
        "status": status,
        "entregador": id_entregador
    }

    if id_pedido not in entregadores[id_entregador]["pedidos"]:
        entregadores[id_entregador]["pedidos"].append(id_pedido)

    print("Pedido cadastrado com sucesso!")

def listar_todos_pedidos():

    print("\nTODOS OS PEDIDOS\n")

    if len(pedidos) == 0:
        print("Nenhum pedido cadastrado.")
        return

    for id_pedido, dados in pedidos.items():

        print(
            id_pedido, "-", dados["cliente"], "-", dados["status"]
        )

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
    
    for id_e in entregadores:
        if id_pedido in entregadores[id_e]["pedidos"]:
            entregadores[id_e]["pedidos"].remove(id_pedido)

    pedidos[id_pedido]["entregador"] = id_entregador

    if id_pedido not in entregadores[id_entregador]["pedidos"]:
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
    em_rota = 0

    for id_pedido in pedidos:

        dados = pedidos[id_pedido]

        if dados["status"] == "Pendente":
            pendentes += 1

        elif dados["status"] == "Entregue":
            entregues += 1

        elif dados["status"] == "Cancelado":
            cancelados += 1
        
        elif dados["status"] == "Em Rota":
             em_rota += 1

        if dados["prioridade"] == "Alta":
            alta += 1
        


    print("\nRELATÓRIO OPERACIONAL\n")

    print(f"Total de pedidos: {total}")
    print(f"Pedidos pendentes: {pendentes}")
    print(f"Pedidos entregues: {entregues}")
    print(f"Pedidos cancelados: {cancelados}")
    print(f"Pedidos alta prioridade: {alta}")
    print(f"Pedidos em rota: {em_rota}")
    maior = 0
    nome = ""

    for id_entregador in entregadores:

        dados = entregadores[id_entregador]

        qtd = len(dados["pedidos"])

        if qtd > maior:
            maior = qtd
            nome = dados["nome"]

    if nome != "":
        print(f"Entregador com mais entregas: {nome} ({maior})")


menu()
