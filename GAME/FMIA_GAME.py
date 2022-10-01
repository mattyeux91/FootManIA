import pygame


_WIDTH = 1000
_HEIGHT = 500


# Initialisation
running = True
pause = False
pygame.init()
root = pygame.display.set_mode((_WIDTH, _HEIGHT))
pygame.display.set_caption("Football Manager IA")
background = pygame.display.get_surface()

while running:
    background.fill((126, 200, 80))
    root.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
            if event.key == pygame.K_p:
                pause = not pause
    pygame.display.update()
