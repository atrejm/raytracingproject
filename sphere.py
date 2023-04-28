from hittable import Hittable, HitRecord
from raycast import Ray
from pygame import Vector3
import math

class Sphere(Hittable):

    def __init__(self, center: Vector3, radius: float) -> None:
        self.cen = center
        self.r = radius
        super().__init__()

    def hit(self, ray: Ray, t_min: float, t_max:float) -> bool:
        oc = ray.origin() - self.cen 
        a = ray.direction().magnitude_squared()
        half_b = oc.dot(ray.direction())
        c = oc.magnitude_squared() - self.r*self.r

        discriminant = half_b*half_b - a*c
        if(discriminant) < 0:
            return False
        
        sqrtd = math.sqrt(discriminant)

        # find hte nearest root that lies in the acceptable range
        root = (-half_b - sqrtd) / a
        # if (root < t_min or t_max > root):
        #     return False
        
        outward_normal = (ray.at(root) - self.cen) / self.r
        self.hit_record = HitRecord(ray.at(root), outward_normal, root)
        # self.hit_record.t = root
        # self.hit_record.point = ray.at(self.hit_record.t)
        self.hit_record.set_face_normal(ray, outward_normal)

        return self.hit_record
