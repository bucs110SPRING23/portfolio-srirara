import pygame

pygame.init()

screen = pygame.display.set_mode()
dimensions = screen.get_size() #width and height

starting_point = [dimensions[0] // 2, dimensions[1] // 2]
radius = 50

for _ in range (3):
    pygame.draw.circle(screen, "blue", starting_point, radius)
    starting_point[1] = starting_point[1] - radius
    radius //= 2
    starting_point[1] = starting_point[1] - radius

pygame.display.flip()
pygame.time.wait(2000)
