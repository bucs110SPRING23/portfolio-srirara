import random
import turtle 

screen = turtle.Screen()

todd = turtle.Turtle()

toddx = abs(todd.xcor())
toddy = abs(todd.ycor())
is_in_x = toddx < int(screen.window_width()) / 2
is_in_y = toddy < int(screen.window_height()) / 2

while is_in_x and is_in_y :
    flip = random.randrange(0,2)
    if flip == 0:
        todd.left(90)
    else:
        todd.right(90)
    todd.forward(50)

    toddx = abs(todd.xcor())
    toddy = abs(todd.ycor())
    is_in_x = toddx < int(screen.window_width()) / 2
    is_in_y = toddy < int(screen.window_height()) / 2
    
    if not (is_in_x and is_in_y):
        print("out of range")
        break

screen.exitonclick()