from hittable import HitRecord
from raycast import Ray
from tracer_utilities import random_unit_vector, random_in_unit_sphere
from pygame import Vector3
from tracer_color import TracerColor

class Material():

    def __init__(self, albedo) -> None:
        self.albedo = albedo
    
    def scatter(self, r_in: Ray, hit_record: HitRecord, attenuation: TracerColor, scattered: Ray):
        return
    
class Lambertian(Material):

    def scatter(self, r_in: Ray, hit_record: HitRecord):
        scatter_direction = hit_record.normal + random_unit_vector()

        if self.near_zero(scatter_direction):
            scatter_direction = hit_record.normal

        scattered = Ray(hit_record.point, scatter_direction)
        attenuation = self.albedo
        return scattered

    def near_zero(self, vector: Vector3):
        s = 1e-8
        return (vector.x < s) and (vector.y < s) and (vector.z < s)
    
class Metal(Material):
    def __init__(self, albedo: TracerColor, fuzz: float) -> None:
        self.fuzz = fuzz
        super().__init__(albedo)

    def scatter(self, r_in: Ray, hit_record: HitRecord):
        reflected = Vector3(r_in.direction().normalize()).reflect(hit_record.normal)
        scattered = Ray(hit_record.point, reflected + self.fuzz*random_in_unit_sphere())
        
        return scattered