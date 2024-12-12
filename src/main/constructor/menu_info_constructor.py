from src.views.menu_info_view import MenuInfoView
from src.controllers.menu_info_controller import MenuInfoController

def menu_info_constructor():
    menu_info_view = MenuInfoView().menu_info()
    menu_info_controller = MenuInfoController()
