from src.views.menu_decision_view import MenuDecision
from src.views.register_product_view import RegisterProductView


def start_program() -> None:
    register_product_instance = RegisterProductView()
    menu_decision_instance = MenuDecision()

    while True:
        command_selected = menu_decision_instance.menu_decision()
        #
        match command_selected:
            case 0:
                exit()
            case 1:
                register_product_instance.register_product()
            case 2:
                print("2")
                   
        
        