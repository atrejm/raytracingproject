from raycast import Ray
from pygame import Vector3

class Camera():
    def __init__(self) -> None:
        self.aspect_ratio = 16 / 9
        self.viewport_height = 2
        self.viewport_width = self.aspect_ratio * self.viewport_height
        self.focal_length = 1

        self.origin = Vector3(0, 0, 0)
        self.horizontal = Vector3(self.viewport_width, 0, 0)
        self.vertical = Vector3(0, self.viewport_height, 0)
        self.lower_left_corner = self.origin - self.horizontal/2 - self.vertical/2 - Vector3(0, 0, self.focal_length)

    def get_ray(self, u, v):
        return Ray(self.origin, self.lower_left_corner + u*self.horizontal + v*self.vertical - self.origin)