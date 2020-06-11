"""
Exemplo de uso de funções para cadastro
Uso de Dicionários como banco de dados
Estrutura:

products_db {
    id : {
        name: ,
        city: ,
        age:
    }
}
"""

import Utilities as util

CONST_FIELD_NAME = "name"
CONST_FIELD_CITY = "city"
CONST_FIELD_AGE = "age"



def register_client(id, clients):
    """
    Faz o registro do cliente

    :param id: id do cliente
    :param clients: dicionario contendo os clientes
    :return: mensagem
    """
    name = input("Por favor, digite o nome do cliente: ")
    city = input("Por favor, digite a cidade do cliente: ")
    age = util.get_int("Digite a idade do cliente", 18, 120)
    clients[id] = {
        CONST_FIELD_NAME: name,
        CONST_FIELD_CITY: city,
        CONST_FIELD_AGE: age
    }



def database_clear(clients):
    """
    apaga todo o Database

    :param clients: dicionario contendo os clientes
    :return: Retorna a opção escolhida s/n e apaga db
    """
    op = util.get_yes_no("Tem certeza que deseja zerar o banco de dados")
    if op == 's':
        clients.clear()
        return True, "Dados zerados com sucesso"
    else:
        return False, "Operação cancelada pelo usuário"



def client_query(clients):
    """
    Busca o cliente no DB

    :param clients: dicionario contendo os clientes
    :return: Retorna os clientes encontrados
    """
    id = input("Por favor, digite o CPF do cliente: ")
    if id in clients:
        print("Nome do cliente:", clients[id][CONST_FIELD_NAME])
        print("Cidade do cliente:", clients[id][CONST_FIELD_CITY])
        print("Idade do cliente:", clients[id][CONST_FIELD_AGE])
        input("")
    else:
        print("Cliente não localizado")
        input("")



def client_del(clients):
    """
    deleta o cliente do DB

    :param clients: dicionario contendo os clientes
    :return: Retorna uma mensagem de sucesso ou erro
    """
    id = input("Por favor, digite o CPF do cliente: ")
    if id in clients:
        op = util.get_yes_no("Deseja excluir este cliente? ")
        if op == 's':
            del clients[id]
            return True, "Cliente excluído com sucesso"
        else:
            return False, "Operação cancelada pelo usuário"



def client_edit(clients):
    """
    Busca o cliente no DB

    :param clients: dicionario contendo os clientes
    :return: Edita cliente
    """
    id = input("Por favor, digite o CPF do cliente: ")
    if id in clients:
        register_client(id, clients)
        return True, "Cliente alterado com sucesso"
    else:
        op = util.get_yes_no("Sem registros. Deseja fazer seu cadastro")
        if op == 's':
            register_client(id, clients)
            return True, "Cliente cadastrado com sucesso"
        else:
            return False, "Cliente não localizado."



def client_add(clients):
    """
    Adciona cliente ao DB

    :param clients: dicionario contendo os clientes
    :return: Cadastra os clientes ou confirma sua existencia
    """
    id = input("Por favor, digite o CPF do cliente: ")
    if id in clients:
        op = util.get_yes_no("Cliente existente. Deseja alterar seus dados")
        if op == 's':
            register_client(id, clients)
            return True, "Cliente alterado com sucesso"
        else:
            return False, "Cadastro não realizado. Cliente já existente"
    else:
        register_client(id, clients)
        return True, "Cliente cadastrado com sucesso"


def load_file(filename):
    """
    carrega arquivo bin

    :param filename: nome do arquivo
    :return: none
    """
    clients = util.file_read_bin(filename)
    return clients


def save_file(filename, clients):
    """
    salva arquivo bin

    :param filename: nome do arquivo
    :return: none
    """
    util.file_write_bin(filename, clients)



def menu():
    """
    Exibe menu de opções

    :return: Opção escolhida pelo usuário
    """
    print("*** Sistema de Cadastro de Clientes ***")
    print("1. Cadastrar cliente")
    print("2. Alterar dados de cliente")
    print("3. Excluir cliente")
    print("4. Pesquisar cliente")
    print("5. Zerar banco de dados")
    print("6. Sair")
    print(39 * "*")
    return util.get_int("Digite uma das opções", 1, 6)



def main(clients):
    """
    Ponto principal do programa

    :param clientes: dicionario possuindo os clientes
    :return: None
    """
    filename = "clients"
    clients = load_file(filename)
    while True:
        op = menu()
        if op == 1:
            resp, msg = client_add(clients)
            print(msg)
            input("")

        elif op == 2:
            resp, msg = client_edit(clients)
            print(msg)
            input("")

        elif op == 3:
            resp, msg = client_del(clients)
            print(msg)
            input("")

        elif op == 4:
            client_query(clients)

        elif op == 5:
            resp, msg = database_clear(clients)
            print(msg)
            if resp:
                r = util.get_yes_no("Deseja criar um primeiro cliente")
                if r == 's':
                    client_add(clients)

        elif op == 6:
            save_file(filename, clients)
            break


if __name__ == '__main__':
    database = {}  
    main(database)
