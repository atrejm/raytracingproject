import pygame, math, random, time
from pygame import Color, Vector3
from raycast import Ray
from sphere import Sphere
from camera import Camera
from hittable import HitRecord
from tracer_color import TracerColor
from hittable_list import Hittable_list

ASPECT_RATIO = 16 / 9
SCREEN_WIDTH = 500
SCREEN_HEIGHT = int(SCREEN_WIDTH / ASPECT_RATIO)
RENDER_SCALE = 5 # each pixel is scaled up by this amount
SAMPLES_PER_PIXEL = 50
MAX_DEPTH = 50
 
def create_display(height, width):
    pygame.init()
    # load and set the logo
    # logo = pygame.image.load("logo32x32.png")
    # pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
     
    # create a surface on screen that has the size of 240 x 180
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

    return (discriminant > 0)
        
def ray_color(ray: Ray, world, depth, debug = False) -> Color:
    # sphere_center = Vector3(-1, 0, -1)
    # t = hit_sphere(sphere_center, 0.5, ray)
    
    if (depth <= 0):
        return TracerColor(0, 0, 0)
    
    hit = world.hit(ray, 0, math.inf)
    if hit:
        rec = hit
        target = hit.point + hit.normal + random_unit_vector()
        bounceray = Ray(hit.point, target - hit.point)
        
        return ray_color(bounceray, world, depth - 1, debug=True) * 0.5
    
        r = int(abs(hit.normal.x*255))
        g = int(abs(hit.normal.y*255))
        b = int(abs(hit.normal.z*255))

        return Color(r, g, b)
    
    # if (t > 0):
    #     normal = (ray.at(t) - sphere_center).normalize()
    #     return Color(   int((normal.x*255 + 255)/2), 
    #                     int((normal.y*255 + 255)/2),
    #                     int((normal.z*255 + 255)/2))

    unit_direction = ray.direction().normalize()
    t = 0.5*(unit_direction.y + 1)

    c1 = TracerColor(255, 255, 255)*(1 - t)
    c2 = TracerColor(125, 180, 255)*t
    lerped = c1 + c2
    return lerped
    return TracerColor(37, 116, 245).lerp(TracerColor(255, 255, 255), t)

def random_in_unit_sphere():
    while True:
        p = Vector3(random.random(), random.random(), random.random())
        if p.magnitude() >=1:
            continue
        return p

def random_unit_vector():
    return random_in_unit_sphere().normalize()

def main():
    screen = create_display(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.fill(TracerColor(200,200,200))

    viewport_height = 2
    viewport_width = ASPECT_RATIO * viewport_height
    focal_length = 1

    origin = Vector3(0, 0, 0)
    horizontal = Vector3(viewport_width, 0, 0)
    vertical = Vector3(0, viewport_height, 0)
    lower_left_corner = origin - horizontal/2 - vertical/2 - Vector3(0, 0, focal_length)

    world = Hittable_list()
    cam = Camera()
    
    world.add(Sphere(Vector3(-0.5, 0.2, -1), 0.5))
    world.add(Sphere(Vector3(0.5, -0.2, -1), 0.5))
    #world.add(Sphere(Vector3(0, 90, -90), 120))

    

    # define a variable to control the main loop
    running = True

    pixelarray = pygame.PixelArray(screen)
    # for j in range(SCREEN_HEIGHT):
    #     for i in range(SCREEN_WIDTH):
    #         u = i / (SCREEN_WIDTH - 1)
    #         v = j / (SCREEN_HEIGHT - 1)
    #         ray = Ray(origin, lower_left_corner + u*horizontal + v*vertical - origin)
    #         pixelcolor = ray_color(ray, world)
    #         pixelarray[i, j] = pixelcolor

    movevector = Vector3(0.08, 0, 0)
    sphere = world.objects[0]
    samplescale = 1/SAMPLES_PER_PIXEL

    for j in range(int(SCREEN_HEIGHT)):
        print("Scan Lines remaining: ", SCREEN_HEIGHT - j)
        for i in range(int(SCREEN_WIDTH)):
            # u = (i + (random.betavariate(2, 2)-0.5) * 2) / (SCREEN_WIDTH - 1)
            # v = (j + (random.betavariate(2, 2)-0.5) * 2) / (SCREEN_HEIGHT - 1)
            # ray = cam.get_ray(u, v)
            # pixelarray[i,j] = ray_color(ray, world, MAX_DEPTH)
            # continue

            new_color = TracerColor(0,0,0)
            samplescale = 1/SAMPLES_PER_PIXEL
            for s in range(SAMPLES_PER_PIXEL):
                u = (i + random.random()) / (SCREEN_WIDTH - 1)
                v = (j + random.random()) / (SCREEN_HEIGHT - 1)
                ray = cam.get_ray(u, v)

                color_to_add = ray_color(ray, world, MAX_DEPTH) * samplescale
                # color_to_add.r = int(math.sqrt(samplescale*color_to_add.r))
                # color_to_add.g = int(math.sqrt(samplescale*color_to_add.g))
                # color_to_add.b = int(math.sqrt(samplescale*color_to_add.b))

                new_color = new_color + color_to_add

            pixelarray[i, j] = TracerColor(new_color.r, new_color.g, new_color.b)


    while running:
        # event handling, gets all event from the event queue
        pygame.display.flip()

        # raycasting

        # move sphere
        
        if sphere.cen.x > 1:
            movevector.x = -0.08
        if sphere.cen.x < -1:
            movevector.x = 0.08

        sphere.cen += movevector

        
                
                

        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

if __name__ == "__main__":
    main()