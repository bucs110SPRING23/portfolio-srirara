import random

class Powerup:
    def __init__(self, height):
        types = ["super_mushroom", "mini_mushroom", 'fire_flower']
        self.type = types[random.randint(1,3)]
        self.unlocked = False
        self.height = height

class Goomba:
    def __init__(self,num):
        self.id = num
        self.alive = True
        self.contact = False
        self.speed = 1

class Pipe:
    def __init__(self, orientation):
        self.pos = 10 
        self.spawned = False
        self.orient = orientation