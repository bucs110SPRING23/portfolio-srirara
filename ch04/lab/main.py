import pygame
import math
import random
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode(size = (600,600))
dimensions = screen.get_size()

#betting
screen.fill("white")

font = pygame.font.Font(None, 48)
text = font.render("Who will win?", True, "black")
screen.blit(text, (50, 300))

red_button = pygame.Rect(50, 250, 100, 50)
blue_button = pygame.Rect(450, 250, 100, 50)

bet = 0 #1 if red, 2 if blue
betting = True

pygame.draw.rect(screen, "red", red_button)
pygame.draw.rect(screen, "blue", blue_button)
pygame.display.flip()

while betting:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            break
        elif event.type == MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            screen.fill("white")
            pygame.display.flip()
            if red_button.collidepoint(mouse_pos):
                font = pygame.font.Font(None, 48)
                text = font.render("Pray red wins!", True, "black")
                screen.blit(text, (50, 300))
                bet = 1
                pygame.display.flip()
                pygame.time.wait(1000)
                betting = False
                break 
            elif blue_button.collidepoint(mouse_pos):
                font = pygame.font.Font(None, 48)
                text = font.render("Pray blue wins!", True, "black")
                screen.blit(text, (50, 300))
                bet = 2
                pygame.display.flip()
                pygame.time.wait(1000)
                betting = False
                break
    

#actual game
screen.fill("yellow")
center = [dimensions[0] // 2, dimensions[1] // 2]
radius = 300
pygame.draw.circle(screen, "pink", center, radius)
pygame.draw.line(screen, "black", start_pos=(0,300), end_pos=(600,300))
pygame.draw.line(screen, "black", start_pos=(300,0), end_pos=(300,600))

pygame.display.flip()
pygame.time.wait(2000)

red_score = 0
blue_score = 0
round_num = 0

for i in range(20):
    randomX = random.randrange(0,601)
    randomY = random.randrange(0,601)
    landing_pos = [randomX, randomY]

    distance_from_center = math.hypot(randomX - 300, randomY - 300)
    is_in_circle = distance_from_center <= 600/2 
    if (is_in_circle == True):
        colorchange = -50
        point = True
    else:
        colorchange = +50
        point = False
    colornum = 150 + colorchange

    if(i % 2 == 0): #red
        color = (colornum, 0, 0)
        if(point): red_score += 1
    else: #blue
        color = (0, 0, colornum)
        if(point): blue_score += 1

    pygame.draw.circle(screen, color, landing_pos, 5)
    pygame.display.flip()
    pygame.time.wait(1000)

    round_num += 1
    print(f'Round {round_num}')
    print(f'red score:{red_score}')
    print(f'blue score: {blue_score}')
    print()

if red_score > blue_score:
    message = "Red wins,"
    if bet == 1:
        message += " you guessed right!"
    else:
        message += " try guessing better."
elif blue_score > red_score:
    message = "Blue wins,"
    if bet == 2:
        message += " you guessed right!"
    else:
        message += " try guessing better."
else:
    message = "Draw! You were neither right nor wrong. Try again?"

#winning message
font = pygame.font.Font(None, 48)
text = font.render(message, True, "white")
screen.blit(text, (0, 300)) # where <x> and<y> are coordinates on screen
pygame.display.flip()
pygame.time.wait(1000)


