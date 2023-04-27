from collections import namedtuple
from pygame import Vector3
from raycast import Ray

HitRecord = namedtuple("HitRecord", "point normal t front_face")

class Hittable:
    

    def set_face_normal(self, ray: Ray, outward_normal: Vector3):
        self.front_face = ray.direction().dot(outward_normal) <0
        if (self.front_face):
            HitRecord.normal = outward_normal
        else:
            HitRecord.normal = -outward_normal

    def hit(ray: Ray, t_min: float, t_max: float, hit_record: HitRecord) -> bool:
        return