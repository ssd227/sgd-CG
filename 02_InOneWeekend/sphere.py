from vector import Vec3, Point3
from hittable import HitRecord, Hittable
from math import sqrt
from typing import Tuple, Optional
from material import Material


class Sphere(Hittable):
    def __init__(self, center, radius, material):
        self.center: Point3 = center
        self.radius: float = radius
        self.material: Material = material

    def hit(self, ray, ray_t) -> Tuple[bool, Optional[HitRecord]]:
        oc: Vec3 = ray.origin() - self.center  # A-C
        a = ray.direction().length_squared()  # b*b
        half_b = oc.dot(ray.direction())  # b*(A-C)
        c = oc.length_squared() - self.radius * self.radius  # (A-C)*(A-C) - r*r

        discriminant = half_b * half_b - a * c  # 二次方程解的判定条件
        if discriminant < 0:
            return (False, None)

        sqrtd = sqrt(discriminant)

        # // Find the nearest root that lies in the acceptable range.
        root = (-half_b - sqrtd) / a  # 先选较小的值（但是这个值可能不正确）
        if not ray_t.surrounds(root):  # root <= ray_t.min or ray_t.max <= root
            root = (-half_b + sqrtd) / a  # 候选较大值
            if not ray_t.surrounds(root):
                return (False, None)

        # 存在合理碰撞，记录碰撞点
        t = root
        p = ray.at(t)
        hit_record = HitRecord(t=t, p=p, mat=self.material)

        # 判定ray在物体内外，并设置相逆的normal
        outward_normal = (p - self.center) / self.radius
        hit_record.set_face_normal(ray=ray, outward_normal=outward_normal)

        return (True, hit_record)
