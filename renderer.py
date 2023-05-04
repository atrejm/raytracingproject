import pygame, math, random
from pygame import Color, Vector3
from raycast import Ray
from sphere import Sphere
from camera import Camera
from material import Lambertian, Metal
from tracer_color import TracerColor
from hittable_list import Hittable_list

ASPECT_RATIO = 16 / 9
SCREEN_WIDTH = 300
SCREEN_HEIGHT = int(SCREEN_WIDTH / ASPECT_RATIO)
RENDER_SCALE = 5 # each pixel is scaled up by this amount
SAMPLES_PER_PIXEL = 20
SAMPLE_SCALE = 1/SAMPLES_PER_PIXEL
MAX_DEPTH = 40
 
def create_display(height, width):
    pygame.init()
    pygame.display.set_caption("minimal program")

    return pygame.display.set_mode((height,width))

def hit_sphere(center: Vector3, radius: Vector3, ray: Ray) -> bool:
    oc = ray.origin() - center
    a = ray.direction().dot(ray.direction())
    half_b = oc.dot(ray.direction())
    c = oc.dot(oc) - radius*radius
    discriminant = half_b*half_b - a*c

    if (discriminant < 0):
        return -1
    else:
        return (-half_b - math.sqrt(discriminant)) / a
        
def ray_color(ray: Ray, world, depth, debug = False) -> Color:
 
    if (depth <= 0):
        return TracerColor(0, 0, 0)
    
    hit = world.hit(ray, 0, math.inf)
    global last_world_ray
    if hit:
        bounceray = hit.object.material.scatter(ray, hit)
        attenuation = hit.object.material.albedo
        if(bounceray):
            return ray_color(bounceray, world, depth - 1, debug=True) * attenuation

        return TracerColor(0, 0, 0)
    
    unit_direction = ray.direction().normalize()
    last_world_ray = unit_direction
    t = 0.5*(unit_direction.y + 1)

    return TracerColor(180, 203, 242)
    c1 = TracerColor(255, 255, 255)*(1 - t)
    c2 = TracerColor(125, 180, 255)*t
    lerped = c1 + c2
    return lerped
    return TracerColor(37, 116, 245).lerp(TracerColor(255, 255, 255), t)

def main():
    screen = create_display(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.fill(TracerColor(200,200,200))

    world = Hittable_list()
    cam = Camera()

    world.add(Sphere(Vector3(0, 100.5, -1), 100, Lambertian(TracerColor(200, 200, 20))))
    world.add(Sphere(Vector3(0.5, 0, -1), 0.5, Metal(TracerColor(20, 80, 80), 0.4)))
    world.add(Sphere(Vector3(-0.5, 0, -1), 0.5, Metal(TracerColor(200, 200, 200), 0.1)))

    # define a variable to control the main loop
    running = True

    pixelarray = pygame.PixelArray(screen)
    color_dict = {}
    samplescale = 1/SAMPLES_PER_PIXEL

    for j in range(int(SCREEN_HEIGHT)):
        print("Scan Lines remaining: ", SCREEN_HEIGHT - j)
        for i in range(int(SCREEN_WIDTH)):

            new_color = TracerColor(0,0,0)
            samplescale = 1/SAMPLES_PER_PIXEL
            for s in range(SAMPLES_PER_PIXEL):
                u = (i + random.random()) / (SCREEN_WIDTH - 1)
                v = (j + random.random()) / (SCREEN_HEIGHT - 1)
                ray = cam.get_ray(u, v)

                color_to_add = ray_color(ray, world, MAX_DEPTH) * samplescale

                new_color = new_color + color_to_add

            color_dict[(i, j)] = TracerColor(new_color.r, new_color.g, new_color.b)

    for key, color in color_dict.items():
        pixelarray[key] = color


    while running:
        # event handling, gets all event from the event queue
        pygame.display.flip()

        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

if __name__ == "__main__":
    main()