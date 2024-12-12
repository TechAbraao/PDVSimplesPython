import os

class MenuDecision:
    def menu_decision(self) -> int:
        os.system("cls||clear")

        message = '''
    *========= Sistema Nexus ==========*
    *                                  *
    * [1] - Cadastrar Produto          *
    * [2] - Consultar Produto          *
    * [0] - Encerrar Programa          *
    *                                  *
    * [10] - Informações gerais        *
    *==================================*
    '''
        print(message)
        command_select = input(" * Digite a opção: ")

        return command_select