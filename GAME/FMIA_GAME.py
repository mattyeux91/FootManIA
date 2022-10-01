import pygame
from fmia_pitch import Pitch

_WIDTH = 1200
_HEIGHT = 800


# Initialisation
running = True
pause = False
pygame.init()
root = pygame.display.set_mode((_WIDTH, _HEIGHT))
pygame.display.set_caption("Football Manager IA")
background = pygame.display.get_surface()
game_pitch = Pitch()


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
            if event.key == pygame.K_p:
                pause = not pause
    pygame.display.update()
