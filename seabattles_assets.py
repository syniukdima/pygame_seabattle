import pygame
from settings import *

pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
custom_font = pygame.font.Font(None, 40)

screen.fill("White")

title_surface = custom_font.render("Sea battle", True, "Black")

play_button_surface = pygame.Surface((300, 80))
play_button_surface.fill((201, 199, 199))

play_button_border = pygame.Surface((304, 84))
play_button_border.fill("Black")

play_text = custom_font.render("Play", True, "Black")
play_rect = play_text.get_rect(center=(950, 340))

rules_button_surface = pygame.Surface((300, 80))
rules_button_surface.fill((201, 199, 199))

rules_button_border = pygame.Surface((304, 84))
rules_button_border.fill("Black")
rules_button_text = custom_font.render("Rules", True, "Black")
rules_button_text_rect = rules_button_text.get_rect(center=(950, 540))
title_rect = title_surface.get_rect( center=(950, 50))


rules_surface = pygame.image.load("87743943.jpg").convert()
rules_surface = pygame.transform.scale(rules_surface, (WIDTH * 0.59, HEIGHT))

banner_surface = pygame.image.load("pic662920.jpg").convert()
banner_surface = pygame.transform.scale(banner_surface, (WIDTH * 0.59, HEIGHT))

ship_surface = pygame.image.load("ship.png").convert()
ship_surface = pygame.transform.scale(ship_surface, (40, 160))
ship_rect = ship_surface.get_rect(center=(400, 400))
draggable = False

is_rules_activated = False
game_mode = "Menu"
