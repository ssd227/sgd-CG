

from collections import namedtuple

from vector import Vec3, Color, random_unit_vector, reflect, refract
from abc import ABC, abstractmethod
from typing import Tuple, Optional
from hittable import HitRecord
from ray import Ray
import numpy as np
from utils import my_random

ScatterResult = namedtuple('ScatterResult', 'is_scattered, ray, attenuation')


# 抽象基类
class Material(ABC):
    @abstractmethod
    def scatter(self, ray_in: Ray, rec: HitRecord) -> ScatterResult:
        pass


class Lambertian(Material):
    def __init__(self, a) -> None:
        super().__init__()

        self.albedo: Color = a

    def scatter(self, ray_in: Ray, rec: HitRecord) -> ScatterResult:
        scatter_direction = rec.normal + random_unit_vector()

        # Catch degenerate scatter direction
        if (scatter_direction.near_zero()):
            scatter_direction = rec.normal

        scattered = Ray(rec.p, scatter_direction)

        # return (True, scattered, attenuation)
        return ScatterResult(
            is_scattered=True,
            ray=scattered,
            attenuation=self.albedo)


class Metal(Material):
    def __init__(self, a, f) -> None:
        super().__init__()

        self.albedo: Color = a
        self.fuzz = f if f < 1 else 1

    def scatter(self, ray_in: Ray, rec: HitRecord) -> ScatterResult:
        reflected = reflect(ray_in.direction().unit_vector(), rec.normal);

        scattered = Ray(rec.p, reflected + + self.fuzz * random_unit_vector())

        return ScatterResult(
            is_scattered=rec.normal.dot(scattered.direction()) > 0,  # 方向与法线同向才进一步反射
            ray=scattered,
            attenuation=self.albedo)


class Dielectric (Material):
    def __init__(self, index_of_refraction):
        self.ir = index_of_refraction # 折射系数

    def scatter(self, ray_in:Ray, rec:HitRecord) -> ScatterResult:
        refraction_ratio = 1.0/self.ir if rec.front_face else self.ir # 根据光线入射方向，决定折射率

        unit_direction = ray_in.direction().unit_vector()

        ## Reflection/refraction choice: calculate both and choose later
        cos_theta = min(rec.normal.dot(-unit_direction), 1.0)
        sin_theta = np.sqrt(1.0 - cos_theta**2)
        cannot_refract = refraction_ratio * sin_theta > 1.0

        direction = None
        if cannot_refract or reflectance(cos_theta, refraction_ratio) > my_random():
            direction = reflect(unit_direction, rec.normal) # 反射后角度
        else:
            direction = refract(unit_direction, rec.normal, refraction_ratio) # 折射后角度

        return ScatterResult(
                is_scattered = True,
                ray = Ray(rec.p, direction),
                attenuation = Color(1.0, 1.0, 1.0)) # 没有衰减


def reflectance(cosine, ref_idx):
    # // Use Schlick's approximation for reflectance.
    r0 = (1 - ref_idx) / (1 + ref_idx)
    r0 = r0 * r0
    return r0 + (1 - r0) * (1 - cosine)**5
