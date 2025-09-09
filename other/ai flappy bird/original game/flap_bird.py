import pygame
import time
import random
import sys
game_over = True
def game():
    block = 20
    BLUE1 = (0, 0, 255)
    GREEN = (50, 200, 0)
    RED = (250, 0, 0)
    WHITE = (255, 255, 255)
    speed = 0.2
    pygame.init()
    font = pygame.font.Font(None, 25)

    pygame.display.set_caption('flappy bird')
    display = pygame.display.set_mode((480, 600))
    first_run = 0
    x, y = 240, 300  # Start in the middle
    run = 0
    t_x = 480
    t_y = 0
    score = 0
    direction = None
    running = True
    running1 = True

    text = font.render("press up button to start ",True,WHITE)
    display.blit(text, [150, 250])
    pygame.display.flip()


    def tower(run, y, x,score):
        gap_height = 150
        tower_width = block
        if run == 0:
            y = random.randint(50, 450)  # y is the top of the gap
        x = x - 20
        run = 1
        if x == 240:
            score += 1
        if x <= 0:
            x = 480
            run = 0

        # Top tower
        pygame.draw.rect(display, GREEN, pygame.Rect(x, 0, tower_width, y))
        # Bottom tower
        pygame.draw.rect(display, GREEN, pygame.Rect(x, y + gap_height, tower_width, 600 - (y + gap_height)))
        return run, y, x, score
        


    def bird(y, block):
        display.fill((0, 0, 0))
        pygame.draw.rect(display, BLUE1, pygame.Rect(x, y, block, block))
        
    
    def input(running, block, y, first_run):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit(1)  

                
        if keys[pygame.K_UP]:
            if y > 600:
                return  y, first_run
            y -= block
            first_run = 1
        else:
            if y < 10:
                return running, y, first_run
            if first_run != 0:
                if y + block <= 600 - block:  # Prevent bird from falling below screen
                    y += block
                else:
                    y = 600 - block  # Clamp to bottom
        return  y, first_run


    def col(x,y1,y,running):

        if 240 <= x <= 260:
            if 0 <= y <= y1 or y1+150<= y <= 600:
                print("out")
                running = False


        return running 

    def scoref(score):
        text = font.render("score: " + str(score),True,WHITE)
        display.blit(text, [0, 0])

    def game_over(score):
        run = False
        pygame.display.flip()
        text = font.render("GAME OVER   final score: " + str(score),True,WHITE)
        display.blit(text, [150, 250])
        pygame.display.flip()
        time.sleep(5)
        return run
    
        
    

    while running1:
        y, first_run = input(running1,block,y,first_run)
        if first_run != 0:
            bird(y,block)
            run, t_y, t_x, score = tower(run, t_y, t_x,score)
            running = col(t_x,t_y,y,running)
            scoref(score)
            
            pygame.display.flip()
            if running == False:
                running1 = game_over(score)
            
        
            speed -= 0.0001
            
        time.sleep(speed)
    

while game_over == True:
   game()


pygame.quit()
