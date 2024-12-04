import os


def menu_decision() -> int:
    os.system("cls||clear")

    message = '''
============== MENU ==============
 [1] - Cadastrar Produto
 [2] - Consultar Produto
 [0] - Encerrar Programa
==================================
    '''
    print(message)
    command_select = int(input("Digite a opção: "))

    return command_select