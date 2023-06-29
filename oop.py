

class Ship:
    def __init__(self, surf, rect, coords, size):
        self.surf = surf
        self.rect = rect
        self.coords = coords
        self.size = size

    def __str__(self):
        return f"Ship {self.size}-sized on {self.coords}" \
               f" position {self.rect}"

class Board:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def area_calc(self):
        return self.height * self.width

    def __str__(self):
        return f"Board {self.height}x{self.width} with (...)"

class Playerboard(Board):
    def __init__(self, height, width, display):
        self.height = 2
        super().__init__(height, width)
        self.display = display



class Ai(Board):
    def __init__(self, height, width, surface):
        super().__init__(height, width)
        self.surface = surface


player_board = Playerboard(8, 10, None)
AI_board = Ai(10, 10, None)

print(player_board)
print(AI_board)

ship1 = Ship(1, 2, 5, 3)

print(ship1)