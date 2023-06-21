

class Ship:
    def __init__(self, surf, rect, coords):
        self.surf = surf
        self.rect = rect
        self.coords = coords


class Two_sized_ship(Ship):

    def __init__(self, surf, rect, coords, size=2):

        super().__init__(surf, rect, coords)
        self.size = size

parentShip = Ship(4, 5, 6)
ship = Two_sized_ship(1, 2, 3, 6)

print(ship.size)
print(parentShip.size)

