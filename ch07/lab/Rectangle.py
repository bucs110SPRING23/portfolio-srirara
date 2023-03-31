class Rectangle:
    def __init__(self, x, y, h, w):
        self.x = abs(x)
        self.y = abs(y)
        self.height = abs(h)
        self.width = abs(w)
    def __str__(self):
        ''' 
        returns a string of the instance variables
            args: self (Rectangle)
            returns: str
        '''
        return f"(x: {self.x}, y: {self.y}), width: {self.width}, height: {self.height}"