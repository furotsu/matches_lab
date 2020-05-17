from menu import MainMenu
from game_screen import GameScreen
from level_manager import LevelManager
from level_builder import LevelBuilder
from level_chooser import LevelChooser
from constants import *


class Gui(MainMenu, GameScreen, LevelBuilder, LevelChooser):
    def __init__(self, root):
        self.level_manager = LevelManager(LEVEL_STORAGE)

        MainMenu.__init__(self, root)
        LevelChooser.__init__(self, root, self.level_manager.LevelsAmount)
        LevelBuilder.__init__(self, root)
        GameScreen.__init__(self, root, self.level_manager.load_levels())

    def _create_start_button(self):
        super()._create_start_button()
        self.start_button.configure(command=self.choose_level)

    def _create_level_builder_button(self):
        super()._create_level_builder_button()
        self.level_builder_button.configure(command=self.start_level_maker)

    def _create_save_button(self):
        super()._create_save_button()
        self._save_button.configure(command=self.save_level)

    def _create_levels_buttons(self):
        """ create buttons that lead calls start_game function
            with parameter of level which contains in its name (but["text"][-1])"""
        super()._create_levels_buttons()
        self._prepare_levels_buttons()

    def _create_delete_level_button(self):
        super()._create_delete_level_button()
        self._delete_level_button.configure(command=self.prepare_levels_to_anihilation)

    def _prepare_levels_buttons(self):
        for i in range(self.levels_amount):
            lbut = self.levels_buttons[i]
            lbut.configure(command=lambda but=lbut: self.start_game(int(but["text"][-1])))

    def prepare_levels_to_anihilation(self):
        for i in range(self.levels_amount):
            lbut = self.levels_buttons[i]
            lbut.configure(command=lambda but=lbut:
                            self.level_manager.delete_level(int(but["text"][-1])-1, self.root))
        self.levels_ready_to_delete = True

    def _create_back_button(self):
        super()._create_back_button()
        self._back_button.configure(command=self.back_to_menu)

    def _create_back_button2(self):
        super()._create_back_button2()
        self._back_button2.configure(command=self.back_to_menu)

    def _create_back_button3(self):
        super()._create_back_button3()
        self._back_button3.configure(command=self.back_to_menu)

    def _create_back_button4(self):
        super()._create_back_button4()
        self._back_button4.configure(command=self.back_to_menu)

    def _to_next_level(self):
        try:
            super()._to_next_level()
        except IndexError as e:
            self.back_to_menu()

    def save_level(self):
        level = {"start": self.start_field, "expected": self.result_field, "task": self.level_description}
        self.level_manager.write_level(level)
        self._levels = self.level_manager.load_levels()
        self.root.quit()

    def choose_level(self):
        super().hide_main_menu()
        super().set_level_chooser()
        if self.levels_ready_to_delete:
            self._prepare_levels_buttons()
            self.levels_ready_to_delete = False

    def start_game(self, level):
        print(level)
        super().hide_level_chooser()
        super().set_game_screen(level - 1)

    def start_level_maker(self):
        super().hide_main_menu()
        super().set_level_builder()

    def back_to_menu(self):
        super().hide_game_screen()
        super().hide_level_builder()
        super().hide_level_chooser()
        super().set_main_menu()
