from src.views.menu_info_view import MenuInfoView


class MenuInfoController:

    def process_command(self, command_selected):
        response = self.verify_option(command_selected)
        return response


    def verify_option(self, command_selected):
        return command_selected == 's' 