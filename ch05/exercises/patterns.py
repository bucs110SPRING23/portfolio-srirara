def star_pyramid():
    rows = int(input("How many rows?"))
    multiplier = 1
    for i in range(rows):
        print("*" * multiplier)
        multiplier += 1

star_pyramid()

def rstar_pyramid():
    rows = int(input("How many rows?"))
    multiplier = rows
    for i in range(rows):
        print("*" * multiplier)
        multiplier -= 1

rstar_pyramid()
