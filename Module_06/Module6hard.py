import math


def _is_valid_color(r, g, b):
    its_color_num = lambda c: isinstance(c, int) and c in range(256)
    return its_color_num(r) and its_color_num(g) and its_color_num(b)


class Figure:
    sides_count = 0

    def __init__(self, color):
        self._color = [*color]
        self._sides = None
        self.filled = False

    def __len__(self):
        return sum(self._sides)

    def get_color(self):
        return self._color

    def set_color(self, r, g, b):
        if _is_valid_color(r, g, b):
            self._color = [r, g, b]

    def get_sides(self):
        return self._sides

    def set_sides(self, *new_sides):
        if (
                len(new_sides) == self.sides_count and
                self._is_valud_sides(*new_sides)
        ):
            self._sides = [*new_sides]

    def _is_valud_sides(self, *sides):
        if len(sides) == self.sides_count:
            for side in sides:
                if not isinstance(side, int) or side < 0:
                    return False
            return True
        else:
            return False


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color)
        # set _sides list
        if len(sides) == 1:
            self._sides = [sides[0] for _ in range(self.sides_count)]
        else:
            self._sides = [1 for _ in range(self.sides_count)]
        self.__radius = len(self)

    def get_square(self):
        return 2 * math.pi * self.__radius


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color)
        # set _sides list
        if len(sides) == 1:
            self._sides = [sides[0] for _ in range(self.sides_count)]
        elif len(sides) == self.sides_count:
            self._sides = [*sides]
        else:
            self._sides = [1 for _ in range(self.sides_count)]
        # set __height list
        self.__height = self._triangle_heights()

    def _triangle_heights(self):
        square = self.get_square()
        sides = self.get_sides()
        return [2 * square / side for side in sides]

    def get_square(self):
        p = sum(self.get_sides()) / 2
        sides = self.get_sides()
        return math.sqrt(p * math.prod([p - side for side in sides]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color)
        # set _sides list
        if len(sides) == 1:
            self._sides = [sides[0] for _ in range(self.sides_count)]
        else:
            self._sides = [1 for _ in range(self.sides_count)]

    def get_volume(self):
        return self._sides[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
