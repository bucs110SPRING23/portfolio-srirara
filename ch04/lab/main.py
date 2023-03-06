import pygame
import math
import random

#Part A
pygame.init()
screen = pygame.display.set_mode(size = (600,600))
dimensions = screen.get_size()

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

