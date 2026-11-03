# Step 6: Bounce on the Paddles
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

# the ball: a small square that moves a few pixels every frame
ball = pygame.Rect(WIDTH // 2 - 8, HEIGHT // 2 - 8, 16, 16)
speed_x, speed_y = 5, 4

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        left.y -= PADDLE_SPEED
    if keys[pygame.K_s]:
        left.y += PADDLE_SPEED
    if keys[pygame.K_UP]:
        right.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN]:
        right.y += PADDLE_SPEED
    left.clamp_ip(area)
    right.clamp_ip(area)

    ball.x += speed_x
    ball.y += speed_y
    # bounce on the top and bottom edges
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        speed_y = -speed_y
    # bounce on a paddle only when the ball moves towards it
    if ball.colliderect(left) and speed_x < 0:
        speed_x = -speed_x
    if ball.colliderect(right) and speed_x > 0:
        speed_x = -speed_x
    screen.fill((15, 20, 35))
    pygame.draw.rect(screen, (255, 255, 255), left)
    pygame.draw.rect(screen, (255, 255, 255), right)
    pygame.draw.ellipse(screen, (255, 210, 60), ball)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
