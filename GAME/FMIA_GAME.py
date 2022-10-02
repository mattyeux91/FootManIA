import pygame
from fmia_pitch import Pitch
import fmia_settings as settings

_WIDTH = 1200
_HEIGHT = 800

# Initialisation
running = True
pygame.init()
root = pygame.display.set_mode((_WIDTH, _HEIGHT))
pygame.display.set_caption("Football Manager IA")
background = pygame.display.get_surface()
game_pitch = Pitch()
soccer = game_pitch.soccer
debug = True


def draw_pitch():
    root.blit(game_pitch.pitch_frame, (0, 0))
    game_pitch.render()


while running:
    background.fill((255, 255, 255))
    root.blit(background, (0, 0))
    draw_pitch()

    for event in pygame.event.get():
        # if debug:
        #     pygame.key.set_repeat(int(settings.GENERAL_SETTINGS["REPEAT_ACTION_DELAI"]/settings.GENERAL_SETTINGS["SMOOTHLESSMODE"]))
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        elif event.type == pygame.KEYDOWN:
            if keys[pygame.K_RIGHT] and keys[pygame.K_LSHIFT]:
                soccer.move(2, True)
            if keys[pygame.K_LEFT] and keys[pygame.K_LSHIFT]:
                soccer.move(4, True)
            if keys[pygame.K_UP] and keys[pygame.K_LSHIFT]:
                soccer.move(1, True)
            if keys[pygame.K_DOWN] and keys[pygame.K_LSHIFT]:
                soccer.move(3, True)
            if keys[pygame.K_RIGHT]:
                soccer.move(2, False)
            if keys[pygame.K_LEFT]:
                soccer.move(4, False)
            if keys[pygame.K_UP]:
                soccer.move(1, False)
            if keys[pygame.K_DOWN]:
                soccer.move(3, False)

    pygame.display.update()
