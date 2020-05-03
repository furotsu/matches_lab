from matches import Matches
from level_manager import LevelManager
from constants import *


class LevelBuilder:
    def __init__(self, root):
        self.root = root
        self.start_field = [1 for i in range(42)]
        self.result_field = [0 for i in range(42)]

        self._create_builder_screen()
        self.chosen_match = (0, -1)

    def _create_frame(self):
        self.builder_frame = Frame(self.root)
        self.builder_frame.configure(width=SCREEN_WIDTH / 2 + 500, height=SCREEN_HEIGHT / 2 + 300)
        self.builder_frame.configure(bg='lightgrey')

    def _create_builder_canvas(self):
        self.builder_canvas = Canvas(self.builder_frame, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="cyan")
        self.builder_canvas.focus_set()
        self.builder_canvas.place(relx=CANVAS_REL_X, rely=CANVAS_REL_Y)

    def _create_add_button(self):
        self._add_button = Button(self.builder_frame, text="Add a match", relief=RAISED)
        self._add_button.configure(bg="green", width=15, height=2)
        self._add_button.configure(command=self._add_match)
        self._add_button.place(relx=0.2, rely=0.8)

    def _create_remove_button(self):
        self._remove_button = Button(self.builder_frame, text="Remove a match", relief=RAISED)
        self._remove_button.configure(bg="red", width=15, height=2)
        self._remove_button.configure(command=self._remove_match)
        self._remove_button.place(relx=0.6, rely=0.8)

    def _create_back_button3(self):
        self._back_button3 = Button(self.builder_frame, text="Back to main menu", relief=RAISED)
        self._back_button3.configure(bg="blue", width=15, height=2)
        self._back_button3.place(relx=0.38, rely=0.9)

    def builder_click(self, event):
        """check for click on match after that:
            1) if click on existed match highlights it and all possible places to set it
            2) if click on non-existed match while existed already chosen place it on that spot
                and check if current matches layout is winning"""
        self.draw_builder_matches()
        flag1 = self.paint_matches(self.start_matches, self.start_field, event, 0)
        flag2 = self.paint_matches(self.result_matches, self.result_field, event, 1)
        if flag1 and flag2:
            self.hide_builder_spaces()
            self.draw_builder_matches()

    def paint_matches(self, matches, board, event, square):
        for i in range(matches.Length):
            if board[i] and matches[i].inside_of_rectangle([event.x, event.y]):
                print(i)
                matches[i].draw(self.builder_canvas, 'red')
                self.chosen_match = (square, i)
                return True
            elif not board[i] and matches[i].inside_of_rectangle([event.x, event.y]):
                print(i)
                matches[i].draw(self.builder_canvas, 'red')
                self.chosen_match = (square, i)
                return True
        return False

    def _add_match(self):
        if not self.chosen_match[0]:
            if self.chosen_match[1] + 1:
                self.start_field[self.chosen_match[1]] = 1
        else:
            if self.chosen_match[1] + 1:
                self.result_field[self.chosen_match[1]] = 1

        self.draw_builder_matches()

    def _remove_match(self):
        if not self.chosen_match[0]:
            if self.chosen_match[1] + 1:
                self.start_field[self.chosen_match[1]] = 0
        else:
            if self.chosen_match[1] + 1:
                self.result_field[self.chosen_match[1]] = 0

        self.hide_builder_spaces()
        self.draw_builder_matches()

    def _create_builder_matches(self):
        self.start_matches = Matches(FIELD_POWER, 100, 20, -50)
        self.result_matches = Matches(FIELD_POWER, 100, 400, -50)

    def draw_builder_matches(self):
        self.start_matches.draw_visible_matches(self.builder_canvas, self.start_field, "green")
        self.result_matches.draw_visible_matches(self.builder_canvas, self.result_field, "green")

    def hide_builder_spaces(self):
        self.start_matches.draw_invisible_matches(self.builder_canvas, self.start_field, "grey")
        self.result_matches.draw_invisible_matches(self.builder_canvas, self.result_field, "grey")

    def _create_builder_screen(self):
        self._create_frame()
        self._create_builder_canvas()
        self._create_builder_matches()
        self.draw_builder_matches()
        self.hide_builder_spaces()
        self._create_add_button()
        self._create_remove_button()
        self._create_back_button3()

    def set_level_builder(self):
        self.builder_frame.place(relx=0.01, rely=0.01)
        self.root.bind("<Button-1>", self.builder_click)

    def hide_level_builder(self):
        self.builder_frame.place_forget()
        self.root.bind("<Button-1>", lambda event: NotImplemented)