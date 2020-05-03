from matches import Matches
from levels import level1
from constants import *


class GameScreen:
    def __init__(self, root, levels=NotImplemented):
        self.root = root
        self.game_started = False

        self._levels = levels

        self._create_game_screen()
        self.chosen_match = -1

    def _create_game_frame(self):
        self.game_frame = Frame(self.root)
        self.game_frame.configure(width=SCREEN_WIDTH / 2 + 500, height=SCREEN_HEIGHT / 2 + 300)
        self.game_frame.configure(bg='lightgrey')

    def _create_canvas(self):
        self.canvas = Canvas(self.game_frame, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=GAME_FRAME_BG)
        self.canvas.focus_set()
        self.canvas.place(relx=CANVAS_REL_X, rely=CANVAS_REL_Y)

    def _create_back_button(self):
        self._back_button = Button(self.game_frame, text="Back to main menu", relief=RAISED)
        self._back_button.configure(bg="blue", width=15, height=2)
        self._back_button.place(relx=0.38, rely=0.9)

    def _create_back_button2(self):
        self._back_button2 = Button(self.win_frame, text="Back to main menu", relief=RAISED)
        self._back_button2.configure(bg="blue", width=15, height=2)
        self._back_button2.place(relx=0.35, rely=0.7)

    def _create_next_level_button(self):
        self._next_level_button = Button(self.win_frame, text="Next level", relief=RAISED)
        self._next_level_button.configure(bg="grey", width=15, height=2)
        self._next_level_button.place(relx=0.35, rely=0.3)

    def _create_reset_button(self):
        self._reset_button = Button(self.win_frame, text="Restart level", relief=RAISED)
        self._reset_button.configure(bg="green", width=15, height=2)
        self._reset_button.place(relx=0.4, rely=0.5)

    def click(self, event):
        """check for click on match after that:
            1) if click on existed match highlights it and all possible places to set it
            2) if click on non-existed match while existed already chosen place it on that spot
                and check if current matches layout is winning"""
        self.draw_matches()
        for i in range(self.matches.Length):
            if level1["start"][i] and self.matches[i].inside_of_rectangle([event.x, event.y]):
                print(i)
                self.draw_spaces()
                self.matches[i].draw(self.canvas, 'red')
                self.chosen_match = i
                return
            elif not level1["start"][i] and self.matches[i].inside_of_rectangle([event.x, event.y]) and self.chosen_match + 1:
                level1["start"][i] = 1
                level1["start"][self.chosen_match] = 0
                self.chosen_match = -1
                self._check_for_win()
                self.hide_spaces()
                self.draw_matches()
                return
        #self.chosen_match = -1
        self.hide_spaces()
        self.draw_matches()

    def _check_for_win(self):
        for i in range(len(level1["start"])):
            if level1["start"][i] != level1["expected"][i]:
                return False
        self.show_win_message()
        return True

    def show_win_message(self):
        self._set_win_frame()

    def _create_matches(self):
        self.matches = Matches(FIELD_POWER)

    def draw_matches(self):
        self.matches.draw_visible_matches(self.canvas, level1["start"])

    def draw_spaces(self):
        self.matches.draw_invisible_matches(self.canvas, level1["start"], "yellow")

    def hide_spaces(self):
        self.matches.draw_invisible_matches(self.canvas, level1["start"], GAME_FRAME_BG)

    def _create_game_screen(self):
        self._create_game_frame()
        self._create_canvas()
        self._create_matches()
        self._create_back_button()
        self.draw_matches()
        self._create_win_frame()
        self._create_next_level_button()
        self._create_back_button2()
        self._create_reset_button()

    def hide_win_frame(self):
        self.win_frame.place_forget()

    def _set_win_frame(self):
        self.win_frame.place(relx=0, rely=0)

    def _create_win_frame(self):
        self.win_frame = Frame(self.game_frame)
        self.win_frame.configure(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, bg='yellow')

    def set_game_screen(self):
        self.game_frame.place(relx=0.01, rely=0.01)
        self.root.bind("<Button-1>", self.click)

    def hide_game_screen(self):
        self.game_frame.place_forget()
        self.root.bind("<Button-1>", lambda event: NotImplemented)
