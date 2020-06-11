import Utilities as util

CONST_FIELD_PNAME = "product"
CONST_FIELD_MODEL = "model"
CONST_FIELD_DESCRIPTION = "description"
CONST_FIELD_QUANTITY = "quantity"
CONST_FIELD_PRICE = "price"


def reg_product(id, products_db):
    """
    Responsavel pelo registro

    :param id: pega o id da peça
    :param products_db: dicionario contendo as peças
    :return: mensagem
    """
    product = input('Nome do Produto:  ')
    model = input('Nome o Modelo do Carro:  ')
    description = input('Descrição do produto: ')
    quantity = int(input('Quantidade: '))
    price = int(input('Preco: '))
    products_db[id] = {
        CONST_FIELD_PNAME: product,
        CONST_FIELD_MODEL: model,
        CONST_FIELD_DESCRIPTION: description,
        CONST_FIELD_QUANTITY: quantity,
        CONST_FIELD_PRICE: price
    }


def show_all_pieces(products_db):
    """
    Mostra todas as peças no banco

    :param products_db: dicionario contendo as peças
    :return: mensagem
    """
    print(products_db)


def show_specifc_piece(products_db):
    """
    mostra peça especifica procurada pelo id

    :param products_db: dicionario contendo as peças
    :return: mensagem com peça buscada pelo id
    """
    id = input("ID da peça: ")
    if id in products_db:
        print("Peça: ", products_db[id][CONST_FIELD_PNAME])
        print("Modelo: ", products_db[id][CONST_FIELD_MODEL])
        print("Descrição: ", products_db[id][CONST_FIELD_DESCRIPTION])
        print("Quantidade: ", products_db[id][CONST_FIELD_QUANTITY])
        print("Preço: ", products_db[id][CONST_FIELD_PRICE])
    else:
        print('Peça não localizada')


def product_add(products_db):
    """
    adiciona uma peça

    :param products_db: dicionario contendo as peças
    :return: mensagem
    """
    id = input("ID da peca: ")
    if id in products_db:
        op = util.get_yes_no("Peça já cadastrada, deseja alterar?")
        if op == 's':
            reg_product(id, products_db)
            return True, "peça alterado com sucesso"
        else:
            return False, "Cadastro não realizado. peça já existente"
    else:
        reg_product(id, products_db)
        return True, "peça cadastrada com sucesso"


def stock_rem(products_db, rem):
    """
    remove peças do estoque

    :param products_db: dicionario contendo as peças
    :return: mensagem
    """
    id = input("ID da peca que deseja remover do estoque: ")
    rem = int(input('Quantos voce deseja remover: '))
    if id in products_db:
        product = products_db[id][CONST_FIELD_PNAME]
        model = products_db[id][CONST_FIELD_MODEL]
        description = products_db[id][CONST_FIELD_DESCRIPTION]
        quantity = products_db[id][CONST_FIELD_QUANTITY] - rem
        price = products_db[id][CONST_FIELD_PRICE]
        products_db[id] = {
            CONST_FIELD_PNAME: product,
            CONST_FIELD_MODEL: model,
            CONST_FIELD_DESCRIPTION: description,
            CONST_FIELD_QUANTITY: quantity,
            CONST_FIELD_PRICE: price
        }
        print('Peças removidas com sucesso! ')
    else:
        op = util.get_yes_no('Nenhum produto com esse ID deseja inserir? ')
        if op == 's':
            product_add(products_db)


def load_file(filename):
    """
    carrega arquivo bin

    :param filename: nome do arquivo
    :return: none
    """
    products_db = util.file_read_bin(filename)
    return products_db


def save_file(filename, products_db):
    """
    salva arquivo bin

    :param filename: nome do arquivo
    :return: none
    """
    util.file_write_bin(filename, products_db)


def menu():
    """
    Exibe menu de opções

    :return: Opção escolhida pelo usuário
    """
    print("*** Sistema de Cadastro de Produtos ***")
    print("1. Cadastrar Peça")
    print("2. Listar Toda as Peças")
    print("3. Listar Peças por Modelo")
    print("4. Remover Peça do Estoque")
    print("5. Sair")
    print("***************************************\n")
    return util.get_int("Digite uma das opções", 1, 6)


def main(product):
    """
    Ponto principal do programa

    :param peças: dicionario possuindo os peças
    :return: None
    """
    filename = "productDB"
    products_db = load_file(filename)
    while True:
        op = menu()
        if op == 1:
            product_add(products_db)
        elif op == 2:
            show_all_pieces(products_db)
        elif op == 3:
            show_specifc_piece(products_db)
        elif op == 4:
            stock_rem(products_db)
        elif op == 5:
            save_file(filename, products_db)
            break


if __name__ == '__main__':
    products = {}
    main(products)
