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
        with open(self.file, 'r') as a:
            file = json.load(a)
        level["current"] = level["start"]
        file.append(level)
        with open(self.file, 'w') as b:
            json.dump(file, b)

    def delete_level(self, level_index, root):
        with open(self.file, 'r') as a:
            file = json.load(a)
        file.pop(level_index)
        with open(self.file, 'w') as b:
            json.dump(file, b)
        root.quit()

    @property
    def LevelsAmount(self):
        with open(self.file, 'r') as a:
            file = json.load(a)
            return len(file)


