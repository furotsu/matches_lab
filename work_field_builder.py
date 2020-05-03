from matches import Matches
from constants import *

# TODO maybe
class WorkField:
    def __init__(self, root):
        self.root = root

    def _create_frame(self):
        self.game_frame = Frame(self.root)
        self.game_frame.configure(width=SCREEN_WIDTH / 2 + 500, height=SCREEN_HEIGHT / 2 + 300)
        self.game_frame.configure(bg='lightgrey')

    def _create_canvas(self):
        self.canvas = Canvas(self.game_frame, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=GAME_FRAME_BG)
        self.canvas.focus_set()
        self.canvas.place(relx=CANVAS_REL_X, rely=CANVAS_REL_Y)

    def _create_back_button(self):
        self._back_button1 = Button(self.game_frame, text="Back to main menu", relief=RAISED)
        self._back_button1.configure(bg="blue", width=15, height=2)
        self._back_button1.place(relx=0.38, rely=0.9)

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
            elif not level1["start"][i] and self.matches[i].inside_of_rectangle(
                    [event.x, event.y]) and self.chosen_match + 1:
                print("this one ")
                level1["start"][i] = True
                level1["start"][self.chosen_match] = False
                self.chosen_match = -1
                self.hide_spaces()
                self.draw_matches()
                return
        self.chosen_match = -1
        self.hide_spaces()
        self.draw_matches()

    def _create_matches(self):
        self.matches = Matches(FIELD_POWER)

    def draw_matches(self):
        self.matches.draw_visible_matches(self.canvas, level1["start"])

    def draw_spaces(self):
        self.matches.draw_invisible_matches(self.canvas, level1["start"], "yellow")

    def hide_spaces(self):
        self.matches.draw_invisible_matches(self.canvas, level1["start"], GAME_FRAME_BG)

