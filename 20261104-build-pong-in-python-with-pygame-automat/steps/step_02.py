# Step 2: Draw the Paddles
import pygame

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

# a paddle is a rectangle: x, y, width, height
left = pygame.Rect(30, HEIGHT // 2 - 50, 12, 100)
right = pygame.Rect(WIDTH - 42, HEIGHT // 2 - 50, 12, 100)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((15, 20, 35))
    pygame.draw.rect(screen, (255, 255, 255), left)
    pygame.draw.rect(screen, (255, 255, 255), right)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
