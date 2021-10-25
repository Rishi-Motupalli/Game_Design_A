# Rishi Motupalli
# 10/25/2021
# Using differnt types of fonts and blit


import os, random, time
import pygame as py
py.init()
WHITE=(255,255,255)
WIDTH = 800
HEIGHT = 800
win = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Setting Window")

## TITLE_FONT = py.font.SysFont(name, size, bold=False, italic=False)
TITLE_FONT = py.font.SysFont('comicsans', 80,)
SUBTITLE_FONT = py.font.SysFont('comicsans', 40, italic = True)
def display_message(message):
    py.time.delay(100)
    text = TITLE_FONT.render(message, 1, WHITE) #message, thickness, color
    #win.blit(text, (WIDTH/2 - text.get_width()/2), HEIGHT/2 - text.get_height()/2) #centers the text
    win.blit(text, (WIDTH/2 - text.get_width()/2), 70)
    py.display.update()
    py.time.delay(100)



run = True
while run:
    for eve in py.event.get():
        if eve.type == py.QUIT:
            run = False
            py.quit()
    display_message("SETTINGS")
    py.time.delay(300)
    win.fill(0, 0, 0)
    display_message("oops")
    py.time.delay(300)
    win.fill(0, 0, 0)
py.quit()

##PRINT THE REST OF THE MENU
# NEED - window size, Background Color, Object color
# Just need to be able to open a window from the first menu
#for loop w/ display message sending title and text NEED TO HAVE THE X/Y COORDS to place the title in the right spot