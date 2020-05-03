from menu import MainMenu
from game_screen import GameScreen
from level_manager import LevelManager
from level_builder import LevelBuilder
from constants import *


class Gui(MainMenu, GameScreen, LevelBuilder):
    def __init__(self, root):
        MainMenu.__init__(self, root)
        GameScreen.__init__(self, root)
        LevelBuilder.__init__(self, root)
        self.level_manager = LevelManager(LEVEL_STORAGE)

    def _create_start_button(self):
        super()._create_start_button()
        self.start_button.configure(command=self.start_game)

    def _create_level_builder_button(self):
        super()._create_level_builder_button()
        self.level_builder_button.configure(command=self.start_level_maker)

    def _create_back_button(self):
        super()._create_back_button()
        self._back_button.configure(command=self.back_to_menu)

    def _create_back_button2(self):
        super()._create_back_button2()
        self._back_button2.configure(command=self.back_to_menu)

    def _create_back_button3(self):
        super()._create_back_button3()
        self._back_button3.configure(command=self.back_to_menu)

    def start_game(self):
        super().hide_main_menu()
        super().set_game_screen()

    def start_level_maker(self):
        super().hide_main_menu()
        super().set_level_builder()

    def back_to_menu(self):
        super().hide_game_screen()
        super().hide_level_builder()
        super().set_main_menu()
