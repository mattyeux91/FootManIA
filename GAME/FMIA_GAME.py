import pygame
from fmia_pitch import Pitch

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


def draw_pitch():
    root.blit(game_pitch.pitch_frame, (0, 0))
    game_pitch.render()


while running:
    background.fill((255, 255, 255))
    root.blit(background, (0, 0))
    draw_pitch()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        elif event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT] and keys[pygame.K_LSHIFT]:
                soccer.newposition(2, 1)
            elif keys[pygame.K_LEFT] and keys[pygame.K_LSHIFT]:
                soccer.newposition(4, 1)
            elif keys[pygame.K_UP] and keys[pygame.K_LSHIFT]:
                soccer.newposition(1, 1)
            elif keys[pygame.K_DOWN] and keys[pygame.K_LSHIFT]:
                soccer.newposition(3, 1)
            elif keys[pygame.K_RIGHT]:
                soccer.newposition(2, 0)
            elif keys[pygame.K_LEFT]:
                soccer.newposition(4, 0)
            elif keys[pygame.K_UP]:
                soccer.newposition(1, 0)
            elif keys[pygame.K_DOWN]:
                soccer.newposition(3, 0)
    pygame.display.update()
