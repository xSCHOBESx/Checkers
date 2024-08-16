import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

#rgb
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (95, 0, 160)

CROWN = pygame.transform.scale(pygame.image.load(r'P:\Projects\Python\Checkers\assets\crown.png'), (44, 25))