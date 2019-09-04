import pygame
import random
import sys

# Some parameters for the game and init of pygame window
PURPLE = (255, 0, 255)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode([500, 500])
pygame.init()
font_name = pygame.font.match_font('arial')


# Segment is a block of the Snake
# The snake is constructed of these segments
class Segment():
    def __init__(self, x, y, colour, width=10):
        self.x, self.y = x, y
        self.colour = colour
        self.width = width

# Draw the segment at the specified coordinates
# Segments are squares with dimensions of width*width
    def SegmentDraw(self):
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width,
                                               self.width), 0)


# Snake class
# Length controls starting number of segments
# self.segments is used to store the segments of the snake
# xVel and yVel are velocities used to determine snake movement
# direction is a label of the current direction of the snake
class Snake():
    def __init__(self, colour, length=5):
        self.colour = colour
        self.length = length
        self.segments = []
        self.x, self.y = 250, 250
        self.xVel, self.yVel = -10, 0
        self.direction = ''
        for i in range(length):
            self.segments.append(Segment(self.x, self.y, colour))
            self.x += self.segments[i].width

    def SnakeDraw(self):
        for i in range(len(self.segments)):
            self.segments[i].SegmentDraw()

    def SnakeMove(self):
        self.x += self.xVel
        self.y += self.yVel
        self.segments.insert(0, Segment(self.x, self.y, self.colour))
        self.segments.pop()


# Utility fucntion to display text on the screen
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, PURPLE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


# Util function to redraw the window
def update_window(screen):
    global snake
    screen.fill(BLACK)
    draw_text(screen, str(snake.length), 30, 250, 10)
    snake.SnakeDraw()
    pygame.display.update()

# the start screen
# if key pressed, start screen loop terminates and game loop begins


def start_screen(screen):
    terminate = False
    while not terminate:
        draw_text(screen, 'Press any key to play!', 40, 200, 200)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                terminate = True
                break
        pygame.display.flip()


# Game loop
clock = pygame.time.Clock()
snake = Snake(PURPLE)
start_screen(screen)
while True:
    # Get key press
    # Give ability to quit using the x in the window corner
    # Key directions determine velocity of the snake and current direction
    # Snake can not go in same direction as its currently going
    # To avoid stacking of velocities and infinite acceleration
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if keys[pygame.K_UP] and not snake.direction == 'UP':
                snake.direction = 'UP'
                snake.yVel -= 10
                snake.xVel = 0
            elif keys[pygame.K_DOWN] and not snake.direction == 'DOWN':
                snake.direction = 'DOWN'
                snake.yVel += 10
                snake.xVel = 0
            elif keys[pygame.K_LEFT] and not snake.direction == 'LEFT':
                snake.direction = 'LEFT'
                snake.xVel -= 10
                snake.yVel = 0
            elif keys[pygame.K_RIGHT] and not snake.direction == 'RIGHT':
                snake.direction = 'RIGHT'
                snake.xVel += 10
                snake.yVel = 0

    snake.SnakeMove()
    update_window(screen)
    clock.tick(10)
