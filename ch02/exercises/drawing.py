import turtle

sides = int(input("Enter the number of sides: "))
length = float(input("Enter the length of each side: "))
internal_angle = 360 / sides
print(internal_angle)

wn = turtle.Screen()
ant = turtle.Turtle()
ant.color("blue")

for _ in range(sides):
    ant.forward(length)
    ant.left(internal_angle)

wn.exitonclick()