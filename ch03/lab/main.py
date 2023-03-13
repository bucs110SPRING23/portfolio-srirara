import pygame
import random
import math

#Part A
pygame.init()
screen = pygame.display.set_mode(size = (600,600))
dimensions = screen.get_size()

screen.fill("blue")
center = [dimensions[0] // 2, dimensions[1] // 2]
radius = 300
pygame.draw.circle(screen, "pink", center, radius)
pygame.draw.line(screen, "black", start_pos=(0,300), end_pos=(600,300))
pygame.draw.line(screen, "black", start_pos=(300,0), end_pos=(300,600))

pygame.display.flip()
pygame.time.wait(2000)

#Part B
for i in range(10):
    randomX = random.randrange(0,601)
    randomY = random.randrange(0,601)
    landing_pos = [randomX, randomY]

    distance_from_center = math.hypot(randomX - 300, randomY - 300)
    is_in_circle = distance_from_center <= 600/2 
    if (is_in_circle == True):
        color = "green"
    else:
        color = "red"
    
    pygame.draw.circle(screen, color, landing_pos, 5)
    pygame.display.flip()
    pygame.time.wait(1000)