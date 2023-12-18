# from tqdm import tqdm
from PIL import Image
import numpy as np
import multiprocessing
from math import tan

from utils import INF, degrees_to_radians
from color import write_color
from hittable import HitRecord, Hittable
from ray import Ray
from vector import *
from interval import Interval
from utils import timing


# from material import

class Camera:
    def __init__(self,
                 aspect_ratio=1.0,
                 image_width=100,
                 samples_per_pixel=10,
                 max_depth=10,
                 vfov=90,
                 lookfrom=Point3(0, 0, -1),
                 lookat=Point3(0, 0, 0),
                 vup=Vec3(0, 1, 0),
                 defocus_angle=0,
                 focus_dist=1
                 ) -> None:

        # public
        self.aspect_ratio = aspect_ratio  # Ratio of image width over height
        self.image_width = image_width  # Rendered image width in pixel count
        self.samples_per_pixel = samples_per_pixel  # Count of random samples for each pixel
        self.max_depth = max_depth  # Maximum number of ray bounces into scene
        self.vfov = vfov  # Vertical view angle (field of view)

        self.lookfrom = lookfrom  # Point camera is looking from
        self.lookat = lookat  # Point camera is looking at
        self.vup = vup  # Camera-relative "up" direction

        self.defocus_angle = defocus_angle  # Variation angle of rays through each pixel
        self.focus_dist = focus_dist  # Distance from camera lookfrom point to plane of perfect focus

    def initialize(self):
        """
        
        # private
        self.image_height : int     # Rendered image height
        self.camera_center : Point3        # Camera center
        self.pixel00_loc : Point3   # Location of pixel 0, 0
        self.pixel_delta_u : Vec3   # Offset to pixel to the right
        self.pixel_delta_v : Vec3   # Offset to pixel below

        """

        # Calculate the image height, and ensure that it's at least 1.
        self.image_height = int(self.image_width / self.aspect_ratio)
        self.image_height = 1 if self.image_height < 1 else self.image_height

        self.camera_center = self.lookfrom  # 相机坐标

        # Determine viewport dimensions.
        theta = degrees_to_radians(self.vfov)
        h = tan(theta / 2)
        viewport_height = 2 * h * self.focus_dist  # 聚焦平面被放大到外部
        viewport_width = viewport_height * (float(self.image_width) / self.image_height)

        # Calculate the u,v,w unit basis vectors for the camera coordinate frame.
        w = (self.lookfrom - self.lookat).unit_vector()
        u = self.vup.cross(w).unit_vector()
        v = w.cross(u)

        # Calculate the vectors across the horizontal and down the vertical viewport edges.
        viewport_u = viewport_width * u  # Vector across viewport horizontal edge
        viewport_v = viewport_height * -v  # Vector down viewport vertical edge

        # Calculate the horizontal and vertical delta vectors from pixel to pixel.
        self.pixel_delta_u = viewport_u / self.image_width
        self.pixel_delta_v = viewport_v / self.image_height

        # Calculate the location of the upper left pixel.
        viewport_upper_left = self.camera_center - (self.focus_dist * w) - viewport_u / 2 - viewport_v / 2
        self.pixel00_loc = viewport_upper_left + 0.5 * (self.pixel_delta_u + self.pixel_delta_v)  # P(0,0)坐标

        # Calculate the camera defocus disk basis vectors.
        defocus_radius = self.focus_dist * tan(degrees_to_radians(self.defocus_angle / 2))
        self.defocus_disk_u = u * defocus_radius
        self.defocus_disk_v = v * defocus_radius

    def render_one_pixel(self, params):
        i, j, world = params

        # 计算ray碰撞颜色
        pixel_color = Color(0, 0, 0)
        for _ in range(self.samples_per_pixel):
            ray = self.get_ray(i, j)
            pixel_color += self.ray_color(ray=ray, depth=self.max_depth, world=world)

        # output
        img_rgb_color = write_color(pixel_color, self.samples_per_pixel)
        return img_rgb_color.to_tuple()

    # 多线程，快了非常多。但是图像有点问题
    @timing
    def render(self, world: Hittable):
        self.initialize()
        cpu_cores = multiprocessing.cpu_count()

        image_array = [[None] * self.image_width for _ in range(self.image_height)]
        params_list = [(i, j, world) for j in range(self.image_height) for i in range(self.image_width)]

        with multiprocessing.Pool(cpu_cores) as p:
            color_res = p.map(self.render_one_pixel, params_list)
        for idx, (i, j, _) in enumerate(params_list):
            image_array[j][i] = color_res[idx]

        im = Image.fromarray(np.uint8(image_array))
        im.save("images/render.png", "PNG")

    # 采样像素(i,j)中的一条光线
    def get_ray(self, i: int, j: int) -> Ray:
        # Get a randomly-sampled camera ray for the pixel at location i,j, originating from
        # the camera defocus disk.
        pixel_center = self.pixel00_loc + (i * self.pixel_delta_u) + (j * self.pixel_delta_v)
        pixel_sample = pixel_center + self.pixel_sample_square()

        # ray_origin = self.camera_center
        ray_origin = self.camera_center if self.defocus_angle <= 0 else self.defocus_disk_sample()
        ray_direction = pixel_sample - ray_origin

        return Ray(ray_origin, ray_direction)

    def pixel_sample_square(self) -> Vec3:
        # Returns a random point in the square surrounding a pixel at the origin.
        px = -0.5 + my_random()  # a random real in [0,1).
        py = -0.5 + my_random()  # a random real in [0,1).
        return (px * self.pixel_delta_u) + (py * self.pixel_delta_v)

    def defocus_disk_sample(self) -> Point3:
        # Returns a random point in the camera defocus disk.
        p = random_in_unit_disk()
        return self.camera_center + (p.x * self.defocus_disk_u) + (p.y * self.defocus_disk_v)

    def ray_color(self, ray: Ray, depth: int, world: Hittable) -> Color:
        # If we've exceeded the ray bounce limit, no more light is gathered.
        if depth <= 0:
            return Color(0, 0, 0)

        hit, rec = world.hit(ray, Interval(_min=0.001, _max=INF))
        if hit:

            ok, scattered, attenuation = rec.material.scatter(ray, rec)
            if ok:
                # 衰减系数 * 光线反射后看到的全局光照颜色
                return attenuation * self.ray_color(scattered, depth - 1, world)
            # 无折射光线
            return Color(0, 0, 0)

            # direction = random_on_hemisphere(rec.normal)
            # direction = rec.normal + random_unit_vector()

            # 无限递归不得慢死？(新的随机光线没撞到物体上，那就是天空的蓝白色，跳出递归) 
            # 漫反射物体每次削减50%的光线，由于rgb三通道等效衰减，所以物体是蓝灰灰色的？？
            # return 0.5 * self.ray_color(Ray(rec.p, direction), depth-1, world); 

        # 背景
        unit_direction = ray.direction().unit_vector()
        a = 0.5 * (unit_direction.y + 1.0)  # 取值范围在[0.25, 0.75]左右
        return (1.0 - a) * Color(1.0, 1.0, 1.0) + a * Color(0.5, 0.7, 1.0)  # 白色到固定颜色的渐变(线性插值)
