def multiplier(x,y): #x*y
    answer = 0
    for i in range(y):
        answer +=x
    return answer
    
def exponent(x,y): #x^y
    answer = 1
    for i in range(y):
        answer *= x
    return answer

def square(x):
    return exponent(x,2)

def main():
    print(multiplier(4,5))
    print(exponent(2,4))
    print(square(7))

main()