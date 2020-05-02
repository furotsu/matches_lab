from constants import *
from math import fabs, sqrt

class Matches:
    def __init__(self, field_power):
        self.field_power = field_power
        self.indent = INDENT_BETWEEN_MATCHES

        self._create_cells()
        self._create_matches()

    def draw_visible_matches(self, canvas, active_list: list):
        for i in range(len(self.matches)):
            if active_list[i]:
                self.matches[i].draw(canvas, "pink")

    def draw_invisible_matches(self, canvas, active_list: list, color):
        for i in range(len(self.matches)):
            if not active_list[i]:
                self.matches[i].draw(canvas, color)

    def _create_matches(self):
        self.matches = []
        for i in range(len(self.cells)):
            try:
                if (i + 1) % (self.field_power + 1) != 0:
                    self.matches.append(self.cells[i].connect_to(self.cells[i + 1]))
                if (i + 1) % (self.field_power + 1) != 0 and i + 1 < (self.field_power + 1) ** 2 - self.field_power:
                    self.matches.append(self.cells[i].connect_to(self.cells[i + self.field_power + 2]))
                if i + 1 < (self.field_power + 1) ** 2 - self.field_power:
                    self.matches.append(self.cells[i].connect_to(self.cells[i + self.field_power + 1]))
                if i + 1 < (self.field_power + 1) ** 2 - self.field_power and (i + 1) % (self.field_power + 1) != 1:
                    self.matches.append(self.cells[i].connect_to(self.cells[i + self.field_power]))
            except IndexError:
                print("Cannot draw one of the matches")
                print(i)

    def _create_cells(self):
        self.cells = []
        for i in range(self.field_power + 1):
            for j in range(self.field_power + 1):
                self.cells.append(Cell((j + 1) * self.indent, (i + 1) * self.indent))
        print(len(self.cells))

    @property
    def Length(self):
        return len(self.matches)

    def __getitem__(self, item):
        return self.matches[item]


class Match:
    def __init__(self, coords: list):
        self.coords = [coords[0] + MATCH_INDENT_X, coords[1] + MATCH_INDENT_Y,
                       coords[2] + MATCH_INDENT_X, coords[3] + MATCH_INDENT_Y]

    def draw(self, canvas, color):
        canvas.create_line(self.coords, fill=color, width=MATCH_WIDTH)

    def inside_of_rectangle(self, point: list) -> bool:
        """check if point is within a rectangle"""
        px, py = point[0], point[1]

        if self.coords[0] == self.coords[2]:
            x1 = self.coords[0] + MATCH_WIDTH/2
            x2 = self.coords[0] - MATCH_WIDTH/2
            x3 = self.coords[2] - MATCH_WIDTH/2
            y1 = y2 = self.coords[1]
            y3 = self.coords[3]
            first = 0 < self.scalar_product([x1-x2, y1-y2], [px-x2, py-y2]) < self.scalar_product([x1-x2, y1-y2], [x1-x2, y1-y2])
            second = 0 < self.scalar_product([x3-x2, y3-y2], [px-x2, py-y2]) < self.scalar_product([x3-x2, y3-y2], [x3-x2, y3-y2])
            return first and second
        elif self.coords[1] == self.coords[3]:
            y1 = self.coords[1] + MATCH_WIDTH/2
            y2 = self.coords[1] - MATCH_WIDTH/2
            y3 = self.coords[3] - MATCH_WIDTH/2
            x1 = x2 = self.coords[0]
            x3 = self.coords[2]
            first = 0 < self.scalar_product([x1-x2, y1-y2], [px-x2, py-y2]) < self.scalar_product([x1-x2, y1-y2], [x1-x2, y1-y2])
            second = 0 < self.scalar_product([x3-x2, y3-y2], [px-x2, py-y2]) < self.scalar_product([x3-x2, y3-y2], [x3-x2, y3-y2])
            return first and second
        else:

            if self.coords[0] < self.coords[2]:
                x1 = self.coords[0] + MATCH_WIDTH / 2
                x2 = self.coords[0] - MATCH_WIDTH / 2
                x3 = self.coords[2] - MATCH_WIDTH / 2
                y1 = self.coords[1] - MATCH_WIDTH / 2
                y2 = self.coords[1] + MATCH_WIDTH / 2
                y3 = self.coords[3] + MATCH_WIDTH / 2
                first = 0 < self.scalar_product([x1 - x2, y1 - y2], [px - x2, py - y2]) < self.scalar_product([x1 - x2, y1   - y2], [x1 - x2, y1 - y2])
                second = 0 < self.scalar_product([x3 - x2, y3 - y2], [px - x2, py - y2]) < self.scalar_product([x3 - x2, y3 - y2], [x3 - x2, y3 - y2])
                return first and second
            elif self.coords[0] > self.coords[2]:
                x1 = self.coords[0] + MATCH_WIDTH / 2
                x2 = self.coords[0] - MATCH_WIDTH / 2
                x3 = self.coords[2] - MATCH_WIDTH / 2
                y1 = self.coords[1] + MATCH_WIDTH / 2
                y2 = self.coords[1] - MATCH_WIDTH / 2
                y3 = self.coords[3] - MATCH_WIDTH / 2
                first = 0 < self.scalar_product([x1 - x2, y1 - y2], [px - x2, py - y2]) < self.scalar_product([x1 - x2, y1 - y2], [x1 - x2, y1 - y2])
                second = 0 < self.scalar_product([x3 - x2, y3 - y2], [px - x2, py - y2]) < self.scalar_product([x3 - x2, y3 - y2], [x3 - x2, y3 - y2])
                return first and second

    def _line_length(self, point1, point2):
        x = fabs(point1[0] - point2[0])
        y = fabs(point1[1] - point2[1])
        return sqrt(x ** 2 + y ** 2)

    def scalar_product(self, vector1, vector2):
        return vector1[0] * vector2[0] + vector1[1] * vector2[1]


class Cell:
    def __init__(self, pos_x, pos_y):
        self.pos_x, self.pos_y = pos_x, pos_y

    def connect_to(self, other_cell):
        return Match([self.pos_x, self.pos_y, other_cell.X, other_cell.Y])

    @property
    def X(self):
        return self.pos_x

    @property
    def Y(self):
        return self.pos_y
