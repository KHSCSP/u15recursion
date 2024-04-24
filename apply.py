import pygame, random, sys
import my_functions as f

# setup
pygame.init()
w = 800
h = 800
screen = pygame.display.set_mode([w, h])
screen.fill((255, 255, 255))

# TODO vert_lines


# TODO squares



# TODO h_tree



# stay on screen
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
      