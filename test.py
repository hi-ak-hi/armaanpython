import pygame
pygame.init()

display = pygame.display.Info()
screen = pygame.display.set_mode((display.current_w, display.current_h))
pygame.display.set_caption("Game")

fps = 60
clock = pygame.time.Clock()

run = True

while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()