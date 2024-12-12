import os

class MenuInfoView:
    def menu_info(self) -> str:
        os.system("cls||clear")

        message = '''
    *========= Informações ===========*
    *                                 *
    * Autor: Abraão V. S. Santos      *   
    *                                 *
    * Data: 11/12/2024                *          
    *                                 *
    * Objetivo: Implementação incial  *
    *           do padrão MVC para    *
    *           fins de aprendizado.  *
    *                                 *
    *=================================*
    '''
        print(message)
        
        command_selected = input(" * Aperte qualquer tecla para sair: ")

        return command_selected



