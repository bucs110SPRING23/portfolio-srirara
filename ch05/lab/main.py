import pygame

#Part A
def threenp1count(n):
    count = 0
    while n > 1.0:
        count += 1
        if n % 2 == 0:
            n = int(n/2)
        else:
            n = int(3 * n + 1)
    return count

def threenp1range(upper_limit):
    objs_in_sequence = {}
    for i in range(2, upper_limit + 1):
        key = i
        value = threenp1count(i)
        objs_in_sequence.update({key:value})
    return objs_in_sequence

#Part B
def graph_coordinates(threenplus1_iters_dict):
    screen = pygame.display.set_mode()
    screen.fill("white")

    coords = list(threenplus1_iters_dict.items())
    if len(coords) < 2:
        return print("Error: not enough coordinates for a line")
    else:
        screen = pygame.display.get_surface()
        pygame.draw.lines(screen, "blue", False, coords)

    new_screen = pygame.transform.flip(screen, False, True)
    factor = 5
    w, h = screen.get_size()
    new_screen = pygame.transform.scale(new_screen, (w*factor,h*factor))
    screen.blit(new_screen, (0,-4*h))

    max_so_far = 0
    for key, value in coords:
        if value > max_so_far:
            max_so_far = value
        else:
            continue

    font = pygame.font.Font(None, 35)
    msg = font.render(f"Largest number of iterations so far: {max_so_far}", False, "red")
    screen.blit(msg, (10,10))

    pygame.display.flip()
    pygame.time.wait(5000)

def main():
    request = int(input("Enter an upper limit: "))
    coords = threenp1range(request)

    pygame.init()
    return(graph_coordinates(coords))

main()