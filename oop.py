

class Ship:
    def __init__(self, surf, rect, coords, size):
        self.surf = surf
        self.rect = rect
        self.coords = coords
        self.size = size

class Board:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def area_calc(self):
        return self.height * self.width

class Playerboard(Board):
    def __init__(self, height, width, display):

        super().__init__(height, width)
        self.display = display
class Ai(Board):
    def __init__(self, height, width, surface):
        super().__init__(height, width)
        self.surface = surface
player_board = Playerboard(10, 10, None)
AI_board = Ai(10, 10, None)
print(player_board.area_calc())
print(AI_board.area_calc())
