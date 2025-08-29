import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 500, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Game")

x, y = WIDTH // 2, HEIGHT // 2
vel = 5
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (0, 255, 0), (x, y, 50, 50))
    pygame.display.update()
    clock.tick(60)
