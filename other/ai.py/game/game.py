import pygame
import time
import random
last_key = 5
BLUE1 = (0, 0, 255)
pygame.init()
pygame.display.set_caption('Sanke')
display = pygame.display.set_mode((480, 600))
x = 0
y = 0

running = True
while running:
    display.fill((0, 0, 0))
    pygame.draw.rect(display, BLUE1, pygame.Rect(x, y, 20, 20))
    x1 = random.randint(0,600)
    y1 = random.randint(0,480)
    pygame.draw.rect(display, BLUE1, pygame.Rect(x1, y1, 20, 20))

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 10
        last_key = 0
    if keys[pygame.K_RIGHT]:
        x += 10
        last_key = 1
    if keys[pygame.K_UP]:
        y -= 10
        last_key = 2
    if keys[pygame.K_DOWN]:
        y += 10
        last_key = 3
    else:
        if last_key == 0: x -= 20
        elif last_key == 1: x += 20
        elif last_key == 2: y -= 20
        else: y += 20

    

    time.sleep(0.1)
pygame.quit()
