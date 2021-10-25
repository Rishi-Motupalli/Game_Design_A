#Rishi Motupalli
#10/21/2021
#Learning diplay,
# opening windows,
# changing size window,
# basic game loop
# K_UP                  up arrow
# K_DOWN                down arrow
# K_RIGHT               right arrow
# K_LEFT                left arrow

import pygame, os, random
#first thing to do is to initilialize pygame
pygame.init()
check=True
height=600
width=700
colors = {'black':(0,0,0), 'red':(255,0,0), 'green':(0,255,0), 'blue':(0,0,255), 'white':(255,255,255), 'purple':(150,0,150)}
while check:
    # height= input("Height of the window: (100- 1000) ")
    # width = input(" Width of your window:  (10-1000 ")
    color= input("What color do you prefer red, green, blue, white, black, or purple")
    try:
        height= int(height)
        width=int(width)
        check = False
    except ValueError:
        check = True
 

color= colors.get(str(color))
window= pygame.display.set_mode((height,width)) #set up color
window.fill(color)
pygame.display.flip() # refresh window with new color
#change title of your window
pygame.display.set_caption("My Game Window")
pygame.display.flip()
hbox=50
wbox=50
speed=5
rect=pygame.Rect(width/2,height/2, wbox, hbox )
pygame.draw.rect(window, colors.get('purple'), rect)
pygame.display.flip()
run=True
 
#main loop for the game:
while run:
    pygame.time.delay(100)
    for case in pygame.event.get():
        if case.type == pygame.QUIT:
            run= False
    #how to get the position of the mouse
    # x,y=pygame.mouse.get_pos()
    # print("( "+ str(x)+ " , "+ str(y)+" )")
    keyPressed= pygame.key.get_pressed()
    if keyPressed[pygame.K_UP]:
        rect.y -= speed
    if keyPressed[pygame.K_DOWN]:
        rect.y += speed
    if keyPressed[pygame.K_LEFT]:
        rect.x -= speed
    if keyPressed[pygame.K_RIGHT]:
        rect.x += speed
   
    window.fill(color)
    pygame.display.flip()
    pygame.draw.rect(window, colors.get('purple'), rect)
    pygame.display.flip()
 