import pygame
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
def classify(x): return 'yes' if x > 0.5 else 'no'
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    text = classify(10)
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, (0, 0, 0))
    screen.blit(text_surface, (width // 2 - text_surface.get_width() // 2, height // 2 - text_surface.get_height() // 2))
    pygame.display.flip()
pygame.quit()
