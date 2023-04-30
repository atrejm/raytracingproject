from pygame import Color

class TracerColor(Color):

    def __init__(self, r, g, b):
        super().__init__(r, g, b)

    def __add__(self, other):
        self.r += int(other.r)
        self.g += int(other.g)
        self.b += int(other.b)

        return self
    
    def __mul__(self, other):
        self.r = int(self.r*other)
        self.g = int(self.g*other)
        self.b = int(self.b*other)

        return self
    