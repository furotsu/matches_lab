from matches import Matches
from constants import *


class GameScreen:
    def __init__(self, root):
        self.root = root
        self.game_started = False

    def _set_game_frame(self):
        self.game_frame = Frame(self.root)
        self.game_frame.configure(width=SCREEN_WIDTH / 2 + 300, height=SCREEN_HEIGHT / 2 + 200)
        self.game_frame.configure(bg='lightgrey')
        self.game_frame.place(relx=0.1, rely=0.1)

    def _set_canvas(self):
        self.canvas = Canvas(self.game_frame, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='cyan')
        self.canvas.focus_set()
        self.canvas.place(relx=0.1, rely=0.1)

    def _set_matches(self):
        self.matches = Matches(3)

    def _set_back_button(self):
        self.back_button = Button(self.game_frame, text="Back", relief=RAISED)
        self.back_button.configure(bg="blue", width=5, height=2)
        self.back_button.place(relx=0.48, rely=0.9)

    def set_game_screen(self):
        self._set_game_frame()
        self._set_canvas()
        self._set_matches()
        self._set_back_button()

    def hide_game_screen(self):
        self.game_frame.place_forget()
