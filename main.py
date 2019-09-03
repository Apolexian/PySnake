import pygame
import random
PURPLE = (255,0,255)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode([500, 500])


class Segment():
    def __init__(self, x, y, colour, width=10):
        self.x, self.y = x, y
        self.colour = colour
        self.width = width

    def SegmentDraw(self):
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.width), 0)


class Snake():
    def __init__(self, colour, length=5):
        self.colour = colour
        self.length = length
        self.segments = []
        self.x, self.y = 30, 30
        self.xVel,self.yVel = 0,0
        for i in range(length):
            self.segments.append(Segment(self.x, self.y, colour))
            self.x += self.segments[i].width

    def SnakeDraw(self):
        for i in range(len(self.segments)):
            self.segments[i].SegmentDraw()



clock = pygame.time.Clock()
snake = Snake(PURPLE)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_UP:
                snake.xVel -= 10
            elif event.type == pygame.K_DOWN:
                snake.yVel += 10
            elif event.type == pygame.K_LEFT:
                snake.xVel -= 10
            elif event.type == pygame.K_RIGHT:
                snake.xVel += 10

    pygame.draw.rect(screen, BLACK, (0, 0, 500, 500), 0)
    snake.SnakeDraw()
    pygame.display.update()
    clock.tick(10)
