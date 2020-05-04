from matches import Matches
from constants import *


class GameScreen:
    def __init__(self, root, levels):
        self.root = root
        self.game_started = False

        self._levels = levels
        self.current_level = self._levels[0]
        self._current_level_index = 0

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
        self._back_button2.place(relx=0.38, rely=0.7)

    def _create_next_level_button(self):
        self._next_level_button = Button(self.win_frame, text="Next level", relief=RAISED)
        self._next_level_button.configure(bg="grey", width=15, height=2)
        self._next_level_button.place(relx=0.38, rely=0.3)
        self._next_level_button.configure(command=self._to_next_level)

    def _create_reset_button(self):
        self._reset_button = Button(self.win_frame, text="Restart level", relief=RAISED)
        self._reset_button.configure(bg="green", width=15, height=2)
        self._reset_button.place(relx=0.38, rely=0.5)
        self._reset_button.configure(command=self._reset_current_level)

    def _create_task_label(self):
        self._task_label = Label(self.game_frame, text=self.current_level["task"])
        self._task_label.configure(bg="pink", font=("Lora", 18, "bold"), bd=5)
        self._task_label.place(relx=0.1, rely=0.01)


    def _create_win_label(self):
        self._win_label = Label(self.win_frame, text="You solved this puzzle!\n "
                                                     "Wanna try next one or return to main menu?")
        self._win_label.configure(bg="grey", fg="darkred", font=("Lora", 18, "bold"), relief=SUNKEN, bd=5)
        self._win_label.place(relx=0.18, rely=0.1)


    def click(self, event):
        """check for click on match after that:
            1) if click on existed match highlights it and all possible places to set it
            2) if click on non-existed match while existed already chosen place it on that spot
                and check if current matches layout is winning"""
        self.draw_matches()
        for i in range(self.matches.Length):
            if self.current_level["current"][i] and self.matches[i].inside_of_rectangle([event.x, event.y]):
                print(i)
                self.draw_spaces()
                self.matches[i].draw(self.canvas, 'red')
                self.chosen_match = i
                return
            elif not self.current_level["current"][i] and self.matches[i].inside_of_rectangle(
                    [event.x, event.y]) and self.chosen_match + 1:
                self.current_level["current"][i] = 1
                self.current_level["current"][self.chosen_match] = 0
                self.chosen_match = -1
                self._check_for_win()
                self.hide_spaces()
                self.draw_matches()
                return
        # self.chosen_match = -1
        self.refresh_game_elements()

    def _check_for_win(self):
        for i in range(len(self.current_level["current"])):
            if self.current_level["current"][i] != self.current_level["expected"][i]:
                return False
        self.show_win_message()
        return True

    def show_win_message(self):
        self._set_win_frame()

    def _reset_current_level(self):
        for i in range(len(self.current_level["current"])):
            self.current_level["current"][i] = self.current_level["start"][i]
        self.hide_win_frame()
        self.refresh_game_elements()

    def _to_next_level(self):
        self._reset_current_level()
        self._current_level_index += 1
        self.current_level = self._levels[self._current_level_index]
        self.hide_win_frame()
        self.refresh_game_elements()

    def _create_matches(self):
        self.matches = Matches(FIELD_POWER)

    def draw_matches(self):
        self.matches.draw_visible_matches(self.canvas, self.current_level["current"])

    def draw_spaces(self):
        self.matches.draw_invisible_matches(self.canvas, self.current_level["current"], "yellow")

    def hide_spaces(self):
        self.matches.draw_invisible_matches(self.canvas, self.current_level["current"], GAME_FRAME_BG)

    def refresh_game_elements(self):
        self._task_label["text"] = self.current_level["task"]
        self.hide_spaces()
        self.draw_matches()

    def _create_game_screen(self):
        self._create_game_frame()
        self._create_canvas()
        self._create_matches()
        self._create_back_button()
        self.draw_matches()
        self._create_task_label()
        self._create_win_frame()
        self._create_win_label()
        self._create_next_level_button()
        self._create_back_button2()
        self._create_reset_button()

    def _set_win_frame(self):
        self.win_frame.place(relx=0, rely=0)

    def _create_win_frame(self):
        self.win_frame = Frame(self.game_frame)
        self.win_frame.configure(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, bg='lightyellow')

    def hide_win_frame(self):
        self.win_frame.place_forget()

    def set_game_screen(self, level_index):
        print(self._levels[level_index]["start"], self._levels[level_index]["expected"], sep="\n")
        self._current_level_index = level_index
        self.current_level = self._levels[level_index]
        self.refresh_game_elements()
        self.game_frame.place(relx=0.01, rely=0.01)
        self.root.bind("<Button-1>", self.click)

    def hide_game_screen(self):
        self.game_frame.place_forget()
        self.root.bind("<Button-1>", lambda event: NotImplemented)
