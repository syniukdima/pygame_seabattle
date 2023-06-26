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

ship_surface = pygame.image.load("ship.png").convert()
ship_surface = pygame.transform.scale(ship_surface, (40, 160))
ship_rect = ship_surface.get_rect(center=(400, 400))
draggable = False

class Ship(pygame.sprite.Sprite):
    def __init__(self, length, start_position):
        super().__init__()
        self.image = pygame.image.load("ship.png").convert()
        self.image = pygame.transform.scale(ship_surface, (40, 160))
        self.rect = ship_surface.get_rect(center=start_position)
        self.length = length


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
