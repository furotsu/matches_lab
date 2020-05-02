from menu import MainMenu
from game_screen import GameScreen


class Gui(MainMenu, GameScreen):
    def __init__(self, root):
        MainMenu.__init__(self, root)
        GameScreen.__init__(self, root)

        self.game_started = False

    def _set_start_button(self):
        super()._set_start_button()
        self.start_button.configure(command=self.start_game)

    def _set_back_button(self):
        super()._set_back_button()
        self.back_button.configure(command=self.back_to_menu)

    def start_game(self):
        super().hide_main_menu()
        super().set_game_screen()

    def back_to_menu(self):
        super().hide_game_screen()
        super().set_main_menu()
