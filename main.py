from tkinter import Tk
from gui import Gui

"""
    Matches puzzle game made by Froltsev Vlad K-11
    In this game you can solve matches puzzles that was made by game creator
    or make your own puzzles and then test it.
    Game process consists of: replacing, adding or removing matches on the game field
                                in order to complete task that given in the upper-left 
                                screen corner.
"""


def main():
    root = Tk()

    Gui(root)

    root.mainloop()


if __name__ == "__main__":
    main()
