from raycast import Ray

class WorldRay():
    def __init__(self, ray:Ray) -> None:
        self.last_ray_into_sky = ray
        return