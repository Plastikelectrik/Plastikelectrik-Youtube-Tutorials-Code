# Step 1: Open the Window
import pygame

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

running = True
while running:
    # read every event: closing the window ends the loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((15, 20, 35))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
