from matches import Matches
from level_manager import LevelManager
from constants import *


class LevelBuilder:
    def __init__(self, root):
        self.root = root
        self.start_field = [0 for i in range(42)]
        self.result_field = [0 for i in range(42)]
        self.level_description = ""
        self._level_description = StringVar()

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

    def _create_save_button(self):
        self._save_button = Button(self.builder_frame, text="Save current puzzle", relief=RAISED)
        self._save_button.configure(bg="yellow", width=20, height=2)
        self._save_button.place(relx=0.4, rely=0.01)

    def _create_builder_entry(self):
        self._entry = Entry(self._entry_description_frame, textvariable=self._level_description)
        self._entry.configure(width=25)
        self._entry.pack(side=BOTTOM, anchor=W)

    def _create_builder_entry_button(self):
        self._builder_entry_button = Button(self._entry_description_frame, text="ok")
        self._builder_entry_button.configure(command=self._save_description)
        self._builder_entry_button.pack(side=RIGHT)

    def _create_builder_entry_label(self):
        self._builder_entry_label = Label(self._entry_description_frame, text="Enter a level description:")
        self._builder_entry_label.configure(font=("Lora", 8, "bold"), bd=3, bg="lightyellow")
        self._builder_entry_label.pack(side=TOP)

    def _create_builder_entry_frame(self):
        self._entry_description_frame = Frame(self.builder_frame)
        self._entry_description_frame.configure(width=150, height=150, bg="lightgreen")
        self._entry_description_frame.place(relx=0.01, rely=0.01)

    def _create_back_button3(self):
        self._back_button3 = Button(self.builder_frame, text="Back to main menu", relief=RAISED)
        self._back_button3.configure(bg="blue", width=15, height=2)
        self._back_button3.place(relx=0.38, rely=0.9)

    def builder_click(self, event):
        """check for click on match and highlights it after what """
        self.draw_builder_matches()
        flag1 = self.paint_matches(self.start_matches, self.start_field, event, 0)
        flag2 = self.paint_matches(self.result_matches, self.result_field, event, 1)
        if flag1 and flag2:
            print('dfdfdfdfdf')
            self.hide_builder_spaces()
            self.draw_builder_matches()

    def paint_matches(self, matches, board, event, square):
        for i in range(matches.Length):
            if board[i] and matches[i].inside_of_rectangle([event.x, event.y]):
                print(i)
                self.hide_builder_spaces()
                self.draw_builder_matches()
                matches[i].draw(self.builder_canvas, 'red')
                self.chosen_match = (square, i)
                return True
            elif not board[i] and matches[i].inside_of_rectangle([event.x, event.y]):
                print(i)
                self.hide_builder_spaces()
                self.draw_builder_matches()
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

    def _save_description(self):
        self.level_description = self._level_description.get()
        print(self.level_description)

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
        self._create_save_button()
        self._create_back_button3()
        self._create_builder_entry_frame()
        self._create_builder_entry()
        self._create_builder_entry_button()
        self._create_builder_entry_label()

    def set_level_builder(self):
        self.builder_frame.place(relx=0.01, rely=0.01)
        self.root.bind("<Button-1>", self.builder_click)

    def hide_level_builder(self):
        self.builder_frame.place_forget()
        self.root.bind("<Button-1>", lambda event: NotImplemented)
