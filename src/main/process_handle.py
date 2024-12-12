from .constructor.menu_decision_constructor import menu_decision_constructor
from .constructor.menu_info_constructor import menu_info_constructor
from .constructor.register_product_constructor import register_product_constructor
## from src.views.register_product_view import RegisterProductView
## from src.views.menu_info_view import MenuInfoView

def start_program() -> None:
    # register_product_instance = RegisterProductView()
    # menu_decision_instance = MenuDecision()
    # menu_info_instance = MenuInfoView()
    while True:
        command_selected = menu_decision_constructor()
        #
        if command_selected == '1': register_product_constructor()
        elif command_selected == '2': print("NULL")
        elif command_selected == '0': exit()
        elif command_selected == '10': menu_info_constructor()
        else: print("Escolha uma opção válida.")
        
        