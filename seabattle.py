import pygame
import sys
from seabattles_assets import *
ship_taken = False
is_rules_activated = False


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

        player_ships.draw(screen)
        player_ships.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        for ship in player_ships:

            # movement mechanic
            if event.type == time_set and ship_taken:
                ship.apply_rotation()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if ship.rect.collidepoint((x, y)) and ship.rect.x >= 0 and ship.rect.y >= 0:
                        ship.draggable = True
                        ship_taken = True
                        ship.offset_x = ship.rect.x - x
                        ship.offset_y = ship.rect.y - y
            if event.type == pygame.MOUSEMOTION:
                if ship.rect.left <= 0 or ship.rect.top <= 0 or ship.rect.right >= WIDTH or ship.rect.bottom >= HEIGHT:
                    ship.draggable = False
                if ship.draggable:
                    x, y = event.pos
                    ship.rect.x = ship.offset_x + x
                    ship.rect.y = ship.offset_y + y
            if event.type == pygame.MOUSEBUTTONUP:
                ship.draggable = False
                if ship.orientation == "horizontal":
                    ship.image = pygame.transform.rotate(ship.image, 90)
                    ship.orientation = "vertical"
                    ship.rect = ship.image.get_rect(center=ship.start_position)
                ship.rect.center = ship.start_position



        if event.type == pygame.MOUSEBUTTONDOWN:
            # print("event")
            x, y = pygame.mouse.get_pos()
            if 800 <= x <= 1100 and 500 <= y <= 580:
                is_rules_activated = not is_rules_activated
            if 800 <= x <= 1100 and 300 <= y <= 380: # clicked play
                game_mode = "Preparation stage"

    gamemode_render(game_mode)

    pygame.display.update()
    clock.tick(60)