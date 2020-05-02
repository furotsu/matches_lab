from matches import Matches
from levels import level1
from functools import partial
from constants import *


class GameScreen:
    def __init__(self, root):
        self.root = root
        self.game_started = False
        self.all_created = False

        self._set_matches()

    def _set_game_frame(self):
        self.game_frame = Frame(self.root)
        self.game_frame.configure(width=SCREEN_WIDTH / 2 + 500, height=SCREEN_HEIGHT / 2 + 300)
        self.game_frame.configure(bg='lightgrey')
        self.game_frame.place(relx=0.01, rely=0.01)

    def _set_canvas(self):
        self.canvas = Canvas(self.game_frame, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='cyan')
        self.canvas.focus_set()
        self.canvas.place(relx=CANVAS_REL_X, rely=CANVAS_REL_Y)

    def _set_back_button(self):
        self.back_button = Button(self.game_frame, text="Back", relief=RAISED)
        self.back_button.configure(bg="blue", width=5, height=2)
        self.back_button.place(relx=0.42, rely=0.9)

    def click(self, event):
        self.draw_matches()
        for i in range(self.matches.Length):
            if level1["start"][i] and self.matches[i].inside_of_rectangle([event.x, event.y]):
                print(i)
                self.draw_spaces()
                self.matches[i].draw(self.canvas, 'red')
                return
        self.hide_spaces()
        self.draw_matches()

    def _set_matches(self):
        self.matches = Matches(FIELD_POWER)

    def draw_matches(self):
        self.matches.draw_visible_matches(self.canvas, level1["start"])


    def draw_spaces(self):
        self.matches.draw_invisible_matches(self.canvas, level1["start"], "yellow")

    def hide_spaces(self):
        self.matches.draw_invisible_matches(self.canvas, level1["start"], "cyan")

    def _set_game_screen(self):
        self._set_game_frame()
        self._set_canvas()
        self._set_matches()
        self._set_back_button()
        self.draw_matches()

    def set_game_screen(self):
        if not self.all_created:
            self._set_game_screen()
            self.all_created = True
        self.game_frame.place(relx=0.01, rely=0.01)
        self.root.bind("<Button-1>", self.click)

    def hide_game_screen(self):
        self.game_frame.place_forget()
        self.root.bind("<Button-1>", lambda event: NotImplemented)
