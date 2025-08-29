import pygame
import random
from enum import Enum
from collections import namedtuple
import numpy as np




pygame.init()
font = pygame.font.Font(None, 25)

#reset
#reward
#play(action) -> direction
#game_iteration
#is_collison




class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

Point = namedtuple('point', 'x, y')
WHITE = (255, 255, 255)
RED = (200,0,0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
BLACK = (0,0,0)
BLOCK_SIZE = 20
SPEED = 20



class SnakeGameAI:
    def __init__(self, w=640, h=480):
        self.w = w
        self.h = h
        #start desplay

        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Sanke')
        self.clock = pygame.time.Clock()
        self.reset()
        self.fram_iterations = 0

    
    def reset(self):
                #init game state
        self.direction = Direction.RIGHT

        self.head = Point(self.w/2, self.h/2)
        self.snake = [self.head, 
                      Point(self.head.x-BLOCK_SIZE, self.head.y)
                     ,Point(self.head.x-(2*BLOCK_SIZE), self.head.y)]
        self.score = 0
        self.food = None
        self._place_food()


    def _place_food(self):
        x = random.randint(0, (self.w-BLOCK_SIZE )//BLOCK_SIZE )*BLOCK_SIZE 
        y = random.randint(0, (self.h-BLOCK_SIZE )//BLOCK_SIZE )*BLOCK_SIZE
        self.food = Point(x,y)
        if self.food in self.snake:
            self._place_food()



    def play_step(self, action):
        # collect user input
        for event in pygame.event.get():
            if event.type == pygame.    QUIT:
                pygame.quit()
                quit()
        
        #move snkr
        self._move(action)
        self.snake.insert(0, self.head)

        #check if game over
        reward = 0
        game_over = False
        if self._is_collison() or self.fram_iterations > 100*len(self.snake):
            game_over = True
            reward = -10
            return reward ,game_over, self.score

        #place new food or judt move snake
        if self.head == self.food:
            self.score += 1
            reward = 10
            self._place_food()
        else:
            self.snake.pop()

        #update ui and clock
        self._update_ui()
        self.clock.tick(SPEED)

        #reture game over and socre
        
        return reward, game_over, self.score

    def _is_collison(self, pt=None):
        if pt is None:
            self.head
        #hits boundy
        if pt.x > self.w - BLOCK_SIZE or pt.x < 0 or pt.y > self.h - BLOCK_SIZE or pt < 0:
            return True

        #hit it self
        if self.head in self.snake[1:]:
            return True
        
        return False
    

    def _update_ui(self):
        self.display.fill(BLACK)

        for pt in self.snake:
            pygame.draw.rect(self.display, BLUE1, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, BLUE2, pygame.Rect(pt.x+4, pt.y+4, 12, 12))
        pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE ))
        text = font.render("score: " + str(self.score),True,WHITE)
        self.display.blit(text, [0, 0])
        pygame.display.flip()
    def _move(self, action):
        #]stright, right,left

        clock_wise = [Direction.RIGHT, Direction.DOWN, Direction.LEFT, Direction.UP]
        idx = clock_wise.index(self.direction)

        if np.array_equal(action, [1,0,0]):
            new_dir = clock_wise[idx]
        if np.array_equal(action, [0,1,0]):
            next_idx = (idx + 1)%4
            new_dir = clock_wise[next_idx]
        else:
            next_idx = (idx + 1)%4
            new_dir = clock_wise[next_idx]
        self.direction = new_dir

        x = self.head.x
        y = self.head.y
        if self.direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif self.direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif self.direction == Direction.UP:
            y -= BLOCK_SIZE
        elif self.direction == Direction.DOWN:
            y += BLOCK_SIZE
        
        self.head = Point(x, y)





if __name__ == '__main__':
    game = SnakeGameAI()
    while True:
        game_over, score = game.play_step()
        if game_over == True:
            print("final score", score)
            break


        #brake if game over
    pygame.quit()


