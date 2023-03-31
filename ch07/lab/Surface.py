from Rectangle import Rectangle
class Surface:
    def __init__(self, filename, x, y, h, w):
        self.image = filename
        self.rect = Rectangle(x, y, h, w)
    def getRect(self):
        '''
        returns the Rectangle attribute of a Surface
            args: self (Surface)
            returns: self.rect (Rectangle)
        '''
        return self.rect