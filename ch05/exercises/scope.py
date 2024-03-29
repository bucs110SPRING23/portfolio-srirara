def multiplier(x,y): #x*y
    ''' multiplies two numbers without using *
        args: x (int), y(int)
        returns: (int)
    '''
    answer = 0
    for i in range(y):
        answer +=x
    return answer
    
def exponent(x,y): #x^y
    ''' raises a number to another number's power without using **
        args: x (int), y(int)
        returns: (int)
    '''
    answer = 1
    for i in range(y):
        answer *= x
    return answer

def square(x):
    ''' squares a number
        args: x (int)
        returns: (int)
    '''
    return exponent(x,2)

def main():
    x = int(input('Enter a number: '))
    y = int(input('Enter another number: '))
    print(f'{x} * {y} is {multiplier(x,y)}')
    print(f'{x} ^ {y} is {exponent(x,y)}')
    print(f'{x} ^ 2 is {square(x)}')
    print(f'{y} ^ 2 is {square(y)}')


main()