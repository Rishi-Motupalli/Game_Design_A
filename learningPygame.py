# Rishi Motupalli
# 10/15/2021
# Learning display, opening windows, changing size, basic loop of game

import pygame 
#first thing to do is initilaize pygame
pygame.init()
check = True
height = " "
width = " "
colors = {'black':(0, 0, 0), 'red' :(255, 0, 0), 'green' :(0, 255, 0), 'blue':(0, 0, 255), 'white' :(255, 255, 255)}
while check:
    height = input("Height of the window: (100 - 1000)")
    width = input("Height of the window: (100 - 1000)")
    color = input("What color do your prefer: Red, Green, Blue, Black & White")
    try:
        height = int(height)
        width = int(width)
        check = False
    except ValueError:
        check = True
color = color.lower()
color = colors.get(str(color))
window = pygame.display.set_mode((400, 400)) # resolution/size
window.fill(color) # color
pygame.display.flip() # refresh window with new color
#c hange the title
pygame.diplay.set_caption("My Game Window") #add windows = if this doesn't work
pygame.display.flip()
run=True

#main loop for the game:
while run:
    pygame.time.delay(1000)
    for case in pygame.event.get():
        if case.type == pygame.QUIT:
            run = False

pygame.quit()
