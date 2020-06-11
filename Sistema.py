"""
Ponto de entrada do sistema
"""

import cadastro as c
import produtos as p
import Utilities as util
import random

CONST_FIELD_BUYER = "comprador"
CONST_FIELD_PRODCUT = "produto"
CONST_FIELD_QUANTITY = "quantidade"
CONST_FIELD_PRICE = "preço"


def order(vendas, clients, products_db):
    """
    Cria e faz o pedido.

    :param vendas: dict contendo historico de vendas
    :param clients: dict contendo os dados do client
    :param products_db: dict contendo os produtos
    :return: Retorna mensagem de compra com sucesso ou erros
    """
    id = input('Insira o ID do cliente: ')
    if id in clients:  # pesquisa os cpf
        name = clients[id][c.CONST_FIELD_NAME]
        # pesquisa o numero da peca
        idp = input(f'Ok {name}, Insira o ID da peca que deseja compara: ')
        if idp in products_db:
            piece = products_db[idp][p.CONST_FIELD_PNAME]
            description = products_db[idp][p.CONST_FIELD_DESCRIPTION]
            while True:  # inicia o processo de compra
                print("'S' para confirmar compra 'N' para cancelar compra")
                op = util.get_yes_no(f'Comprar {piece} desc: {description}?')
                if op == 's':
                    rem = int(input('Quantos voce deseja comprar: '))
                    stock_sell(products_db, rem, idp)
                    sell_value = rem * products_db[idp][p.CONST_FIELD_PRICE]
                    sell_id = random.randint(1000000, 9999999)
                    print(f'O ID da venda é {sell_id} por favor anote!')
                    vendas[sell_id] = {  # faz o registro da venda
                        CONST_FIELD_BUYER: name,
                        CONST_FIELD_PRODCUT: piece,
                        CONST_FIELD_QUANTITY: rem,
                        CONST_FIELD_PRICE: sell_value
                    }
                    print(f'Total da compra {sell_value}')
                    break
                else:
                    print('Compra cancelada')
                    break
        else:
            print('ID da peça incorreto')
    else:
        print('CPF Incorreto.')


def stock_sell(products_db, rem, idp):
    """
    Retira o estoque

    :param products_db: dict contendo os produtos
    :param rem: variavel q armazena o quanto a ser retirado do estoque
    :param idp: codigo do produto
    :return: none
    """
    product = products_db[idp][p.CONST_FIELD_PNAME]
    model = products_db[idp][p.CONST_FIELD_MODEL]
    description = products_db[idp][p.CONST_FIELD_DESCRIPTION]
    quantity = products_db[idp][p.CONST_FIELD_QUANTITY] - rem
    price = products_db[idp][p.CONST_FIELD_PRICE]
    products_db[idp] = {
        p.CONST_FIELD_PNAME: product,
        p.CONST_FIELD_MODEL: model,
        p.CONST_FIELD_DESCRIPTION: description,
        p.CONST_FIELD_QUANTITY: quantity,
        p.CONST_FIELD_PRICE: price
    }


def sell_history(vendas):
    """
    mostra o historico de vendas

    :param vendas: dict contendo historico de vendas
    :return: Retorna dicionario com todas as vendas
    """
    print(vendas)


def sell_query(vendas):
    """
    mostra uma venda especifica

    :param vendas: dict contendo historico de vendas
    :return: venda buscada pelo id_sell
    """
    sell_id = int(input('Coloque o ID da venda: '))
    if sell_id in vendas:
        print('Nome do cliente:', vendas[sell_id][CONST_FIELD_BUYER])
        print('Produto Vendido:', vendas[sell_id][CONST_FIELD_PRODCUT])
        print('Quantidade vendida:', vendas[sell_id][CONST_FIELD_QUANTITY])
        print('Preço Total: R$', vendas[sell_id][CONST_FIELD_PRICE])
    else:
        print('Venda não registrada')


def load_file(filename):
    """
    carrega arquivo bin

    :param filename: nome do arquivo
    :return: none
    """
    clients = util.file_read_bin(filename)
    return clients


def save_file(filename, vendas):
    """
    salva arquivo bin

    :param filename: nome do arquivo
    :return: none
    """
    util.file_write_bin(filename, vendas)


def menu():
    print("*** Sistema de Cadastro de Produtos ***")
    print("1. Registrar venda")
    print("2. Relatório de vendas")
    print("3. Buscar Venda por ID")
    print("4. Sair")
    print("***************************************\n")
    return util.get_int("Digite uma das opções", 1, 6)


def main():
    filename = 'vendas'
    clients = load_file('clients')
    products_db = load_file('productDB')
    vendas = load_file(filename)
    while True:
        op = menu()
        if op == 1:
            order(vendas, clients, products_db)
        elif op == 2:
            sell_history(vendas)
        elif op == 3:
            sell_query(vendas)
        elif op == 4:
            save_file(filename, vendas)
            save_file("clients", clients)
            save_file("productDB", products_db)
            break


if __name__ == '__main__':
    main()
