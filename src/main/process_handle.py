from src.main.constructor.menu_decision_constructor import menu_decision_constructor

def start_program() -> None:
    while True:
        command_selected = menu_decision_constructor()
        #
        if command_selected == 0: exit()
        elif command_selected == 1: print("Opção 1.")
        elif command_selected == 2: print("Opção 2.")
        