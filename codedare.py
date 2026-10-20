from dataclasses import dataclass
from enum import Enum


# ===== ESTRUTURAS =====

@dataclass
class Cliente:
    id: int
    nome: str
    telefone: str


@dataclass
class Loja:
    id: int
    nome: str


@dataclass
class Pedido:
    id: int
    cliente: int
    loja: int
    valor: float
    status: str = "criado"


class Status(Enum):
    CRIADO = "criado"
    PREPARANDO = "em preparação"
    ENTREGA = "em entrega"
    ENTREGUE = "entregue"
    CANCELADO = "cancelado"


# ===== LISTAS =====

clientes = []
lojas = []
pedidos = []


def novo_id(lista):
    return len(lista) + 1


def buscar(lista, codigo):
    for item in lista:
        if item.id == codigo:
            return item
    return None


# ===== CLIENTES =====

def cadastrar_cliente():
    cliente = Cliente(
        novo_id(clientes),
        input("Nome: "),
        input("Telefone: ")
    )
    clientes.append(cliente)
    print("Cliente cadastrado!")


def listar_clientes():
    if not clientes:
        print("Nenhum cliente.")
        return

    for c in sorted(clientes, key=lambda x: x.nome):
        print(f"{c.id} - {c.nome} - {c.telefone}")


def remover_cliente():
    listar_clientes()
    codigo = int(input("ID: "))
    cliente = buscar(clientes, codigo)

    if cliente:
        clientes.remove(cliente)
        print("Cliente removido!")
    else:
        print("Cliente não encontrado.")


# ===== LOJAS =====

def cadastrar_loja():
    loja = Loja(
        novo_id(lojas),
        input("Nome da loja: ")
    )
    lojas.append(loja)
    print("Loja cadastrada!")


def listar_lojas():
    for loja in lojas:
        print(f"{loja.id} - {loja.nome}")


# ===== PEDIDOS =====

def criar_pedido():
    listar_clientes()
    cliente = int(input("ID do cliente: "))

    listar_lojas()
    loja = int(input("ID da loja: "))

    valor = float(input("Valor: R$ "))

    pedido = Pedido(
        novo_id(pedidos),
        cliente,
        loja,
        valor
    )

    pedidos.append(pedido)
    print("Pedido criado!")


def listar_pedidos():
    for p in pedidos:
        print(
            f"Pedido {p.id} | "
            f"Cliente {p.cliente} | "
            f"R$ {p.valor:.2f} | "
            f"{p.status}"
        )


def alterar_status():
    listar_pedidos()

    codigo = int(input("ID do pedido: "))
    pedido = buscar(pedidos, codigo)

    if not pedido:
        print("Pedido não encontrado.")
        return

    print("1 - Preparando")
    print("2 - Em entrega")
    print("3 - Entregue")
    print("4 - Cancelado")

    opcao = input("Escolha: ")

    status = {
        "1": Status.PREPARANDO.value,
        "2": Status.ENTREGA.value,
        "3": Status.ENTREGUE.value,
        "4": Status.CANCELADO.value
    }

    if opcao in status:
        pedido.status = status[opcao]
        print("Status alterado!")
    else:
        print("Opção inválida.")


# ===== RELATÓRIO =====

def resumo():
    # List comprehension
    entregues = [
        p for p in pedidos
        if p.status == Status.ENTREGUE.value
    ]

    # Map
    valores = list(map(lambda p: p.valor, pedidos))

    print(f"\nPedidos: {len(pedidos)}")
    print(f"Entregues: {len(entregues)}")

    if valores:
        print(f"Total: R$ {sum(valores):.2f}")

    # Slicing
    print("Últimos pedidos:", pedidos[-3:])


# ===== MENU =====

def main():
    while True:

        print("\n=== SISTEMA DE PEDIDOS ===")
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Remover cliente")
        print("4 - Cadastrar loja")
        print("5 - Listar lojas")
        print("6 - Criar pedido")
        print("7 - Listar pedidos")
        print("8 - Alterar status")
        print("9 - Resumo")
        print("0 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            remover_cliente()
        elif opcao == "4":
            cadastrar_loja()
        elif opcao == "5":
            listar_lojas()
        elif opcao == "6":
            criar_pedido()
        elif opcao == "7":
            listar_pedidos()
        elif opcao == "8":
            alterar_status()
        elif opcao == "9":
            resumo()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


main()