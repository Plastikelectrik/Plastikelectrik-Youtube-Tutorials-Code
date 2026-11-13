import pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
def draw_circle(x, y):
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 20)
draw_circle(100, 100)
game_loop = True
while game_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
    screen.fill((0, 0, 0))
    draw_circle(100, 100)
    pygame.display.flip()
    pygame.time.Clock().tick(60)
