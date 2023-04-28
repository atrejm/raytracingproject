from hittable import HitRecord, Hittable
from raycast import Ray

class Hittable_list():
    def __init__(self) -> None:
        self.objects = list()

    def add(self, object: Hittable):
        self.objects.append(object)

    def hit(self, ray: Ray, t_min, t_max):
        hit_anything = False
        closest_so_far = t_max
        temp_record = None

        for obj in self.objects:
            if obj.hit(ray, t_min, closest_so_far):
                hit_anything = True
                if (obj.hit_record.t < closest_so_far):
                    closest_so_far = obj.hit_record.t
                    temp_record = obj.hit_record
        
        return temp_record
        