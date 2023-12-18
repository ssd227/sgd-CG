from vector import Vec3, Color, Point3
from hittable_list import HittableList
from sphere import Sphere
from camera import Camera
from material import Lambertian, Metal, Dielectric
from utils import PI, my_random


def scene_dielectrics():
    # World
    world = HittableList()

    material_ground = Lambertian(Color(0.8, 0.8, 0.0))
    material_center = Dielectric(1.5)
    material_left = Dielectric(1.5)
    material_right = Metal(Color(0.8, 0.6, 0.2), 1.0)  # 光滑玻璃

    world.add(Sphere(Point3(0.0, -100.5, -1.0), 100.0, material_ground))
    world.add(Sphere(Point3(0.0, 0.0, -1.0), 0.5, material_center))
    world.add(Sphere(Point3(-1.0, 0.0, -1.0), 0.5, material_left))
    world.add(Sphere(Point3(-1.0,    0.0, -1.0),   -0.4, material_left))
    world.add(Sphere(Point3(1.0, 0.0, -1.0), 0.5, material_right))

    # camera
    aspect_ratio = 16.0 / 9.0
    image_width = 200
    samples_per_pixel = 5
    max_depth = 20

    vfov = 90  # 视角90°
    lookfrom = Point3(0, 0, 0)
    lookat = Point3(0, 0, -1)
    vup = Vec3(0, 1, 0)

    defocus_angle = 0
    focus_dist = 1

    camera = Camera(aspect_ratio=aspect_ratio,
                    image_width=image_width,
                    samples_per_pixel=samples_per_pixel,
                    max_depth=max_depth,
                    vfov=vfov,
                    lookfrom=lookfrom,
                    lookat=lookat,
                    vup=vup,
                    defocus_angle=defocus_angle,
                    focus_dist=focus_dist, )

    # render
    camera.render(world)


def scene_ball_3():
    # World
    world = HittableList()

    # R = cos(PI/4)
    # material_left  =  Lambertian(Color(0,0,1))
    # material_right =  Lambertian(Color(1,0,0))
    # world.add(Sphere(Point3(-R, 0, -1), R, material_left))
    # world.add(Sphere(Point3( R, 0, -1), R, material_right))

    material_ground = Lambertian(Color(0.8, 0.8, 0.0))
    material_center = Lambertian(Color(0.1, 0.2, 0.5))
    material_left = Dielectric(1.5)
    material_right = Metal(Color(0.8, 0.6, 0.2), 0.0)  # 光滑玻璃

    # material_center = Dielectric(1.5) # 电介质
    # material_center = Lambertian(Color(0.7, 0.3, 0.3))
    # material_left   = Dielectric(1.5) # 电介质
    # material_left   = Metal(Color(0.8, 0.8, 0.8), 0.3) # 光滑金属
    # material_right  = Metal(Color(0.8, 0.6, 0.2), 1.0) # 毛金属

    world.add(Sphere(Point3(0.0, -100.5, -1.0), 100.0, material_ground))
    world.add(Sphere(Point3(0.0, 0.0, -1.0), 0.5, material_center))
    world.add(Sphere(Point3(-1.0, 0.0, -1.0), 0.5, material_left))
    world.add(Sphere(Point3(-1.0, 0.0, -1.0), -0.4, material_left))
    world.add(Sphere(Point3(1.0, 0.0, -1.0), 0.5, material_right))

    # camera
    aspect_ratio = 16.0 / 9.0
    image_width = 400
    samples_per_pixel = 5
    max_depth = 10

    vfov = 20  # 视角90°
    lookfrom = Point3(-2, 2, 1)
    lookat = Point3(0, 0, -1)
    vup = Vec3(0, 1, 0)

    defocus_angle = 10.0
    focus_dist = 3.4

    camera = Camera(aspect_ratio=aspect_ratio,
                    image_width=image_width,
                    samples_per_pixel=samples_per_pixel,
                    max_depth=max_depth,
                    vfov=vfov,
                    lookfrom=lookfrom,
                    lookat=lookat,
                    vup=vup,
                    defocus_angle=defocus_angle,
                    focus_dist=focus_dist, )

    # render
    camera.render(world)


def scene_final():
    # World
    world = HittableList()

    ground_material = Lambertian(Color(0.5, 0.5, 0.5))
    world.add(Sphere(Point3(0, -1000, 0), 1000, ground_material))

    for a in range(-5, 5):
        for b in range(-5, 5):
            choose_mat = my_random()
            center = Point3(a + 0.9 * my_random(), 0.2, b + 0.9 * my_random())

            if (center - Point3(4, 0.2, 0)).length() > 0.9:
                sphere_material = None

                if choose_mat < 0.8:
                    # diffuse
                    albedo = Color.random() * Color.random()
                    sphere_material = Lambertian(albedo)
                    world.add(Sphere(center, 0.2, sphere_material))
                elif choose_mat < 0.95:
                    # metal
                    albedo = Color.random_in_interval(0.5, 1)
                    fuzz = my_random(0, 0.5)
                    sphere_material = Metal(albedo, fuzz)
                    world.add(Sphere(center, 0.2, sphere_material))
                else:
                    # glass
                    sphere_material = Dielectric(1.5)
                    world.add(Sphere(center, 0.2, sphere_material))

    # 三个大球
    material1 = Dielectric(1.5)
    world.add(Sphere(Point3(0, 1, 0), 1.0, material1))

    material2 = Lambertian(Color(0.4, 0.2, 0.1))
    world.add(Sphere(Point3(-4, 1, 0), 1.0, material2))

    material3 = Metal(Color(0.7, 0.6, 0.5), 0.0)
    world.add(Sphere(Point3(4, 1, 0), 1.0, material3))

    material_ground = Lambertian(Color(0.8, 0.8, 0.0))
    material_center = Lambertian(Color(0.1, 0.2, 0.5))
    material_left = Dielectric(1.5)
    material_right = Metal(Color(0.8, 0.6, 0.2), 0.0)  # 光滑玻璃

    world.add(Sphere(Point3(0.0, -100.5, -1.0), 100.0, material_ground))
    world.add(Sphere(Point3(0.0, 0.0, -1.0), 0.5, material_center))
    world.add(Sphere(Point3(-1.0, 0.0, -1.0), 0.5, material_left))
    world.add(Sphere(Point3(-1.0, 0.0, -1.0), -0.4, material_left))
    world.add(Sphere(Point3(1.0, 0.0, -1.0), 0.5, material_right))

    # camera
    aspect_ratio = 16.0 / 9.0
    image_width = 400
    samples_per_pixel = 5
    max_depth = 10
    vfov = 20  # 视角90°
    lookfrom = Point3(13, 2, 3)
    lookat = Point3(0, 0, 0)
    vup = Vec3(0, 1, 0)
    defocus_angle = 0.6
    focus_dist = 10

    camera = Camera(aspect_ratio=aspect_ratio,
                    image_width=image_width,
                    samples_per_pixel=samples_per_pixel,
                    max_depth=max_depth,
                    vfov=vfov,
                    lookfrom=lookfrom,
                    lookat=lookat,
                    vup=vup,
                    defocus_angle=defocus_angle,
                    focus_dist=focus_dist,)

    # render
    camera.render(world)


if __name__ == '__main__':
    render_case = 3

    if render_case == 1:
        scene_ball_3()

    elif render_case == 2:
        scene_dielectrics()

    elif render_case == 3:
        scene_final()
