import turtle
import numpy as np

def fibonacci(terms=150):
    ''' returns a fibonacci sequence for the number of terms specified by the user, starting with (1, 1, ...)
        args: terms (int)
        return: fib_sequence (list)
    '''
    x, y = 1, 1
    fib_sequence = [x, y]
    for i in range(terms-2):
        x, y = y, x+y
        fib_sequence.append(y)
    return fib_sequence

def fib_draw(fib_sequence):
    ''' draws a fibonacci-esque pattern using Turtle and a given fibonacci sequence. uses log base 2 of each term to the 1.2 power to modulate the growth of the sequence
        args: fib_sequence (list)
        return: None
    '''
    screen = turtle.Screen()
    pencil = turtle.Turtle()
    pencil.speed(0)

    colors = ["red", "orange", "blue", "green"]
    angle = 0

    for term in fib_sequence:
        length = np.log2(float(term)) ** 1.2
        index = fib_sequence.index(term)

        pencil.color(colors[index % 4])

        if index % 4 == 0:
            for i in range(4):
                pencil.backward(length)
                pencil.right(angle)
        elif index % 4 == 1:
            for i in range(4):
                pencil.forward(length)
                pencil.left(angle)
        elif index % 4 == 2:
            for i in range(4):
                pencil.forward(length)
                pencil.right(angle)
        else:
            for i in range(4):
                pencil.backward(length)
                pencil.left(angle)
        angle += 0.325
    screen.exitonclick()
        
    
def main():
    terms = int(input("Enter the desired number of terms in the fibonacci sequence: "))
    sequence = fibonacci(terms)
    fib_draw(sequence)

main()
