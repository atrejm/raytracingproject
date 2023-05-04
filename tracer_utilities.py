import random
from pygame import Vector3

def random_in_unit_sphere():
    while True:
        p = Vector3(random.random(), random.random(), random.random())
        if p.magnitude() >=1:
            continue
        return p

def random_unit_vector():
    return random_in_unit_sphere().normalize()