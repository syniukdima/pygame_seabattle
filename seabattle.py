import pygame
import sys
from seabattles_assets import *


def gamemode_render(mode):
    if mode == "Menu":
        screen.blit(title_surface, title_rect)
        if is_rules_activated:
            screen.blit(rules_surface, (0, 0))
        else:
            screen.blit(banner_surface, (0, 0))
        screen.blit(play_button_border, (WIDTH * 0.666 - 2, 0.513 * HEIGHT - 2))
        screen.blit(play_button_surface, (WIDTH * 0.666, 0.513 * HEIGHT))
        screen.blit(play_text, play_rect)

        screen.blit(rules_button_border, (WIDTH * 0.666 - 2, 0.85 * HEIGHT - 2))
        screen.blit(rules_button_surface, (WIDTH * 0.666, 0.85 * HEIGHT))
        screen.blit(rules_button_text, rules_button_text_rect)

    if mode == "Preparation stage":
        screen.fill("white")
        screen.blit(ship_surface, ship_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print("event")
            x, y = pygame.mouse.get_pos()
            if 800 <= x <= 1100 and 500 <= y <= 580:
                is_rules_activated = not is_rules_activated
            if 800 <= x <= 1100 and 300 <= y <= 380: # clicked play
                game_mode = "Preparation stage"



            print(ship_rect.collidepoint((x, y)))
            if ship_rect.collidepoint((x, y)) and ship_rect.x >= 0 and ship_rect.y >= 0:
                draggable = True
                offset_x = ship_rect.x - x
                offset_y = ship_rect.y - y
        if event.type == pygame.MOUSEMOTION:
            print(draggable)
            print(ship_rect.left)
            if ship_rect.left <= 0 or ship_rect.top <= 0 or ship_rect.right >= WIDTH or ship_rect.bottom >= HEIGHT:
                draggable = False
            if draggable:
                x, y = event.pos
                ship_rect.x = offset_x + x
                ship_rect.y = offset_y + y
        if event.type == pygame.MOUSEBUTTONUP:
            draggable = False
            ship_rect.left = 400
            ship_rect.top = 400

    gamemode_render(game_mode)

    pygame.display.update()
    clock.tick(60)