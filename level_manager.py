import json


class LevelManager:
    def __init__(self, file):
        self.file = file

    def load_levels(self):
        with open(self.file, 'r') as a:
            levels = []
            file = json.load(a)
            for elem in file:
                levels.append(elem)
        return levels

    def write_level(self, level: dict):
        file = []
        with open(self.file, 'r') as a:
            file = json.load(a)
        file.apped(level)
        with open(self.file, 'w') as b:
            json.dump(file, b)

