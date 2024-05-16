import pygame
from pygame.locals import *
import time
import random

SIZE = 40
BG=(110,110,5)
class snake:
    def __init__(self,surface,length):
        self.length=length
        self.screen=surface
        self.block=pygame.image.load("block.jpg").convert()
        self.block_x=[SIZE]*length
        self.block_y=[SIZE]*length
        self.direction='right'

    def increase_length(self):
        self.length+=1
        self.block_x.append(-1)
        self.block_y.append(-1)
    def draw(self):
        self.screen.fill(BG)
        for i in range(self.length):
            self.screen.blit(self.block,(self.block_x[i],self.block_y[i]))
        pygame.display.flip()


    def move_left(self):
        self.direction='left'
    def move_right(self):
        self.direction='right'
    def move_up(self):
        self.direction='up'
    def move_down(self):
        self.direction='down'
    
    def walk(self):

        for i in range (self.length-1,0,-1):
            self.block_x[i] = self.block_x[i-1]
            self.block_y[i] = self.block_y[i-1]

        if self.direction == 'left':
            self.block_x[0] -= SIZE
        if self.direction == 'right':
            self.block_x[0] +=SIZE
        if self.direction == 'up':
            self.block_y[0] -=SIZE
        if self.direction == 'down':
            self.block_y[0] +=SIZE
        self.draw()
        

class apple:
    def __init__(self,screen):
        self.image=pygame.image.load("apple.jpg").convert()
        self.screen=screen
        self.block_x=SIZE * 3
        self.block_y=SIZE * 3
    def draw(self):
        self.screen.blit(self.image,(self.block_x,self.block_y))
        pygame.display.flip()
    def move(self):
        self.block_x = random.randint(0,23)*40
        self.block_y = random.randint(0,18)*40


class game:
    def __init__(self):
        pygame.init()
        self.surface =pygame.display.set_mode((1000,800))
        self.snake=snake(self.surface,1)
        self.snake.draw()
        self.apple = apple(self.surface)
        self.apple.draw()
    def is_collision(self,x1,y1,x2,y2):
        if x1 >= x2 and x1 < x2+SIZE:
            if y1 >= y2 and y1 < y2+SIZE:
                return True
    
        
        return False
    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.display()
        pygame.display.flip()
        if self.is_collision(self.snake.block_x[0],self.snake.block_y[0],self.apple.block_x,self.apple.block_y):
            self.snake.increase_length()
            self.apple.move()




        for i in range(4,self.snake.length):
            if self.is_collision(self.snake.block_x[0],self.snake.block_y[0],self.snake.block_x[i],self.snake.block_y[i]):
                exit(0)
    

    def display(self):
        font=pygame.font.SysFont('arial',30)
        score= font.render(f"Score:{self.snake.length}",True,(255,255,255))
        self.surface.blit(score,(800,10))

    def show_game_over(self):
        self.surface.fill(BG)
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game is over! Your score is {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(line1, (200, 300))
        pygame.display.flip()




    def run(self):
        run=True
        while run:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key==K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    elif event.type == QUIT:
                        run=False
            try:
                self.play()
            except Exception as e:
                self.show_game_over()
            time.sleep(0.2)


if __name__ == "__main__":
    G=game()
    G.run()