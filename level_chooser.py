from constants import *


class LevelChooser:
    def __init__(self, root, levels_amount):
        self.root = root
        self.levels_amount = levels_amount
        self.levels_buttons =[]
        self.levels_ready_to_delete = False

        self._create_chooser_screen()

    def _create_chooser_frame(self):
        self.chooser_frame = Frame(self.root)
        self.chooser_frame.configure(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.chooser_frame.configure(bg="blue")

    def _create_levels_buttons(self):
        multiplier_x = 1
        multiplier_y = 1
        for i in range(self.levels_amount):
            self.levels_buttons.append(Button(self.chooser_frame, text="Level {}".format(i+1), relief=RAISED))
            self.levels_buttons[-1].configure(bg="pink", width=10, height=5)
            self.levels_buttons[-1].place(relx=0.1 * (multiplier_x), rely=0.1 * multiplier_y)
            multiplier_x += 1
            if multiplier_x % 8 == 0:
                multiplier_x = 1
                multiplier_y += 1.8

    def _create_delete_level_button(self):
        self._delete_level_button = Button(self.chooser_frame, text="Delete level", relief=RAISED)
        self._delete_level_button.configure(bg="red", width=15, height=2)
        self._delete_level_button.place(relx=0.5, rely=0.9)

    def _create_back_button4(self):
        self._back_button4 = Button(self.chooser_frame, text="Back to main menu", relief=RAISED)
        self._back_button4.configure(bg="pink", width=15, height=2)
        self._back_button4.place(relx=0.25, rely=0.9)

    def _create_chooser_screen(self):
        self._create_chooser_frame()
        self._create_levels_buttons()
        self._create_delete_level_button()
        self._create_back_button4()

    def set_level_chooser(self):
        self.chooser_frame.place(relx=0, rely=0)

    def hide_level_chooser(self):
        self.chooser_frame.place_forget()
