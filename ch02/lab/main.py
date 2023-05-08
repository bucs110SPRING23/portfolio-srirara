import random
import turtle
import pygame
import math

#Part A
wn = turtle.Screen()
    #Race 1
donatello = turtle.Turtle()
donatello.color("purple")
donatello.goto(-100, 20)
donatello.forward(random.randrange(1,101))

leonardo = turtle.Turtle()
leonardo.color("blue")
leonardo.goto(-100, -20)
leonardo.forward(random.randrange(1,101))

donatello.goto(-100,20)
leonardo.goto(-100,-20)

    #Race 2
turtles = [donatello, leonardo]
for _ in range(1,11):
    donatello.forward(random.randrange(1,11))
    leonardo.forward(random.randrange(1,11))

donatello.goto(-100,20)
leonardo.goto(-100,-20)

wn.exitonclick()

#Part B
pygame.init()
window = pygame.display.set_mode()
dimensions = window.get_size()

polygon_sides = [3, 4, 6, 20, 100, 360]
points = []
side_length = 300
xpos = dimensions[0] // 2
ypos = dimensions[1] // 2

for sides in polygon_sides:
    window.fill("yellow")
    for i in range(sides):
        angle = 360/sides
        radians = math.radians(angle * i)
        x = xpos + side_length * math.cos(radians)
        y = ypos + side_length * math.sin(radians)
        points.append([x,y])
        print(points)
    pygame.draw.polygon(window, "red", points)
    pygame.display.flip()
    pygame.time.wait(1000)
    points.clear()



