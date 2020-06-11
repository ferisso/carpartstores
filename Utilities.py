"""
Módulo de funções úteis
"""

import pickle
import random

def get_int(message: str, min_value: int, max_value: int) -> int:
    """
    Valida dados inteiros em um determinado range

    :param message: A mensagem a ser exibida
    :param min_value: Valor inteiro mínimo
    :param max_value: Valor inteiro máximo
    :return: Retorna a opção escolhida dentro do range
    """
    while True:
        try:
            op = int(input(message + ": "))
        except ValueError:
            print("Formato inválido: esperado um número")
            continue
        if not min_value <= op <= max_value:
            print("Escolha um número de", min_value, "a", max_value)
        else:
            return op


def get_yes_no(message: str) -> str:
    """
    Valida opções de sim e não

    :param message: A mensagem a ser exibida
    :return: Retorna a opção escolhida s/n
    """
    while True:
        op = input(message + " (s/n): ")
        if op == 's' or op == 'n':
            return op
        else:
            print("Opção inválida: escolha s (sim) ou n (não)")


def file_read_bin(filename: str) -> dict:
    """
    Executa a leitura do arquivo binário

    :param filename: Nome do arquivo de gravação
    :return: Lista com os dados lidos
    """
    content = {}
    try:
        file = open(filename, "rb")
        content = pickle.load(file)
        file.close()
    except IOError:
        pass
    return content


def file_write_bin(filename: str, content: dict):
    """
    Executa a escrita do arquivo binário

    :param filename: Nome do arquivo de gravação
    :param content: Lista com os dados a serem gravados
    :return: None
    """
    file = open(filename, "wb")
    pickle.dump(content, file)
    file.close()

