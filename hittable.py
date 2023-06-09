from collections import namedtuple
from pygame import Vector3
from raycast import Ray

#HitRecord = namedtuple("HitRecord", "point normal t front_face")
class HitRecord:
    
    def __init__(self, point, normal, t, material, object) -> None:
        self.point = point
        self.normal = normal
        self.t = t
        self.material = material
        self.object = object
        pass

    def set_face_normal(self, ray: Ray, outward_normal: Vector3):
        self.front_face = ray.direction().dot(outward_normal) < 0
        if (self.front_face):
            self.normal = outward_normal
        else:
            self.normal = -outward_normal

class Hittable:

    def hit(ray: Ray, t_min: float, t_max: float, hit_record: HitRecord) -> bool:
        return