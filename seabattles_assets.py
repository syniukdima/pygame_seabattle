import pygame
from settings import *

pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
custom_font = pygame.font.Font(None, 40)

screen.fill("White")

title_surface = custom_font.render("Sea battle", True, "Black")

play_button_surface = pygame.Surface((300 / 1200 * WIDTH, 80))
play_button_surface.fill((201, 199, 199))

play_button_border = pygame.Surface((304 / 1200 * WIDTH, 84))
play_button_border.fill("Black")

play_text = custom_font.render("Play", True, "Black")
play_rect = play_text.get_rect(center=(WIDTH * 0.79, HEIGHT * 0.566))

rules_button_surface = pygame.Surface((300 / 1200 * WIDTH, 80))
rules_button_surface.fill((201, 199, 199))

rules_button_border = pygame.Surface((304 / 1200 * WIDTH, 84))
rules_button_border.fill("Black")
rules_button_text = custom_font.render("Rules", True, "Black")
rules_button_text_rect = rules_button_text.get_rect(center=(WIDTH * 0.79, HEIGHT * 0.9))
title_rect = title_surface.get_rect( center=(WIDTH * 0.79, HEIGHT * 0.083))


rules_surface = pygame.image.load("87743943.jpg").convert()
rules_surface = pygame.transform.scale(rules_surface, (WIDTH * 0.59, HEIGHT))

banner_surface = pygame.image.load("pic662920.jpg").convert()
banner_surface = pygame.transform.scale(banner_surface, (WIDTH * 0.59, HEIGHT))

class Ship(pygame.sprite.Sprite):
    def __init__(self, length, start_position):
        super().__init__()
        self.image = pygame.image.load("ship.png").convert()
        self.image = pygame.transform.scale(self.image, (40, 160))
        self.rect = self.image.get_rect(center=start_position)
        self.length = length
        self.start_position = start_position
        self.offset_x = None
        self.offset_y = None
        self.draggable = None

    def apply_rotation(self):

        keys = pygame.key.get_pressed()
        x, y = pygame.mouse.get_pos()
        if keys[pygame.K_SPACE] and self.rect.collidepoint((x, y)):
            self.image = pygame.transform.rotate(self.image, 90)
            self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.apply_rotation()

player_ships = pygame.sprite.Group()

player_ships.add(
    Ship(4, (50, 400)),
    Ship(3, (100, 400)),
    Ship(3, (150, 400)),
    Ship(2, (200, 400)),
    Ship(2, (250, 400)),
    Ship(2, (300, 400)),
    Ship(1, (350, 400)),
    Ship(1, (400, 400)),
    Ship(1, (450, 400)),
    Ship(1, (500, 400)),
)

is_rules_activated = False
game_mode = "Menu"
