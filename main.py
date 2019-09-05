import pygame
import random
import sys

# Some parameters for the game and init of pygame window
PURPLE = (255, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode([500, 500])
pygame.init()
font_name = pygame.font.match_font('arial')


# Segment is a block of the Snake
# The snake is constructed of these segments
class Segment:
    def __init__(self, x, y, colour, width=10):
        self.x, self.y = x, y
        self.colour = colour
        self.width = width

# Draw the segment at the specified coordinates
# Segments are squares with dimensions of width*width
    def segment_draw(self):
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width,
                                               self.width), 0)


# Food is the objective that snake is meant to reach
# Food will cause the snake to grow and score to increase
class Food:
    def __init__(self, x, y, colour=RED, width=10):
        self.x, self.y = x, y
        self.colour = colour
        self.width = width

# Place the food at the specified coordinates
# Food is a square of width*width dimension
    def food_draw(self):
        pygame.draw.rect(screen, self.colour, (self.x, self.y,
                                               self.width, self.width), 0)


# Border is surrounding the playable area
# Snake running into the boarder will result in a lost game
class Border:
    def __init__(self, size, colour=WHITE, width=10):
        self.size = size
        self.colour = colour
        self.width = width
        self.coordinates = [(x, y) for x in range(size) for y in range(size)]

# TODO get the list of coorrdinates right
# Draw the border of specified width around the area specified by the size
    def border_draw(self):
        pass #TODO draw the actual border


# Snake class
# Length controls starting number of segments
# self.segments is used to store the segments of the snake
# xVel and yVel are velocities used to determine snake movement
# direction is a label of the current direction of the snake
class Snake:
    def __init__(self, colour, length=5):
        self.colour = colour
        self.initial_length = length
        self.length = length
        self.segments = []
        self.x, self.y = 250, 250
        self.xVel, self.yVel = -10, 0
        self.direction = 'LEFT'
        for i in range(length):
            self.segments.append(Segment(self.x, self.y, colour))
            self.x += self.segments[i].width

# Function to create the snake
    def snake_draw(self):
        for i in range(len(self.segments)):
            self.segments[i].segment_draw()

    def snake_move(self):
        self.x += self.xVel
        self.y += self.yVel
        self.segments.insert(0, Segment(self.x, self.y, self.colour))
        self.segments.pop()

    def snake_grow(self):
        self.x += self.xVel
        self.y += self.yVel
        self.segments.insert(0, Segment(self.x, self.y, self.colour))


def check_collisions(snake, border, food):
    pass #TODO write it


# Utility function to display text on the screen
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, PURPLE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


# Utility function to redraw the window
def update_window(screen):
    global snake
    screen.fill(BLACK)
# The score = delta length
    draw_text(screen, str(snake.length-snake.initial_length), 30, 250, 10)
    snake.snake_draw()
# TODO draw borders and food
    pygame.display.update()


# The start screen
# If key pressed, start screen loop terminates and game loop begins
def start_screen(screen):
    terminate = False
    while not terminate:
        draw_text(screen, 'Press any key to play!', 40, 250, 150)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                terminate = True
                break
            pygame.display.flip()


# The game over screen that is displayed when game is lost
def game_over_screen(screen):
    draw_text(screen, "Game over lul", 40, 250, 150)


# Game loop
clock = pygame.time.Clock()
border = Border(500)
food = Food(0, 0)
snake = Snake(PURPLE)
start_screen(screen)
while True:
    # Get key press
    # Give ability to quit using the x in the window corner
    # Key directions determine velocity of the snake and current direction
    # Snake can not go in same direction as its currently going
    # To avoid stacking of velocities and infinite acceleration
    # Snake can not move in opposite direction to current
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if keys[pygame.K_UP] and not (snake.direction == 'UP' or
                                          snake.direction == 'DOWN'):
                snake.direction = 'UP'
                snake.yVel -= 10
                snake.xVel = 0
            elif keys[pygame.K_DOWN] and not (snake.direction == 'DOWN' or
                                              snake.direction == 'UP'):
                snake.direction = 'DOWN'
                snake.yVel += 10
                snake.xVel = 0
            elif keys[pygame.K_LEFT] and not (snake.direction == 'LEFT' or
                                              snake.direction == 'RIGHT'):
                snake.direction = 'LEFT'
                snake.xVel -= 10
                snake.yVel = 0
            elif keys[pygame.K_RIGHT] and not (snake.direction == 'RIGHT' or
                                               snake.direction == 'LEFT'):
                snake.direction = 'RIGHT'
                snake.xVel += 10
                snake.yVel = 0

    snake.snake_move()
# TODO check for collisions
    update_window(screen)
    clock.tick(10)
