from constants import *


class MainMenu:
    def __init__(self, root):
        self.root = root
        self.s_width, self.s_height = SCREEN_WIDTH, SCREEN_HEIGHT

        self.config_root()
        self._create_menu_frame()
        self.set_main_menu()
        self._set_buttons()

    def _set_buttons(self):
        self._set_start_button()
        self._set_quit_button()

    def _create_menu_frame(self):
        self.main_frame = Frame(self.root)
        self.main_frame.configure(width=self.s_width / 2, height=self.s_height / 2 + 100)
        self.main_frame.configure(bg="lightblue")

    def _set_start_button(self):
        self.start_button = Button(self.main_frame, text="Start", relief=RAISED)
        self.start_button.configure(bg="green", width=int(self.s_width / 32), height=2)
        self.start_button.place(relx=0.25, rely=0.4)

    def _set_quit_button(self):
        self.quit_button = Button(self.main_frame, text="Quit", relief=RAISED)
        self.quit_button.configure(bg="red", width=int(self.s_width / 32), height=2)
        self.quit_button.configure(command=self.root.quit)
        self.quit_button.place(relx=0.25, rely=0.6)

    def config_root(self):
        self.root.title(GAME_TITLE)
        self.root.geometry("{}x{}+{}+{}".format(self.s_width, self.s_height, 300, 200))
        self.root.resizable(width=False, height=False)

    def hide_main_menu(self):
        self.main_frame.place_forget()

    def set_main_menu(self):
        self.main_frame.place(relx=0.2, rely=0.1)
