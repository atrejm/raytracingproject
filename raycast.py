from pygame import Vector3

class Ray ():

    def __init__(self, origin: Vector3, direction: Vector3):
        self.orig = origin
        self.dir = direction

    def origin(self) -> Vector3:
        return self.orig
    
    def direction(self) -> Vector3:
        return self.dir
    
    def at(self, t) -> Vector3:
        # evaluate this ray at a specific paramater t
        
        return self.orig + t * self.dir
    