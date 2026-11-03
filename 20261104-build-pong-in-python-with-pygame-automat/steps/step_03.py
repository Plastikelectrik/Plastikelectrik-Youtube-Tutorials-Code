# Step 3: Move the Paddles
import pygame

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

left = pygame.Rect(30, HEIGHT // 2 - 50, 12, 100)
right = pygame.Rect(WIDTH - 42, HEIGHT // 2 - 50, 12, 100)
PADDLE_SPEED = 7
area = screen.get_rect()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # keys held down right now
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        left.y -= PADDLE_SPEED
    if keys[pygame.K_s]:
        left.y += PADDLE_SPEED
    if keys[pygame.K_UP]:
        right.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN]:
        right.y += PADDLE_SPEED
    # keep both paddles inside the window
    left.clamp_ip(area)
    right.clamp_ip(area)

    screen.fill((15, 20, 35))
    pygame.draw.rect(screen, (255, 255, 255), left)
    pygame.draw.rect(screen, (255, 255, 255), right)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
