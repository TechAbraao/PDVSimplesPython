
from src.views.menu_decision_view import MenuDecision

def menu_decision_constructor() -> str:
    command_selected = MenuDecision().menu_decision()

    return command_selected