from vector import Vec3
from abc import ABC, abstractmethod
from typing import Tuple, Optional


# from material import Material

# 记录ray碰撞结果
class HitRecord:
    def __init__(self, p, t, mat) -> None:
        self.p = p
        self.t = t
        self.material = mat

    def set_face_normal(self, ray, outward_normal):
        # Sets the hit record normal vector.
        # NOTE: the parameter `outward_normal` is assumed to have unit length.

        self.front_face = outward_normal.dot(ray.direction()) < 0  # 向量逆向，dot值为负数
        self.normal = outward_normal if self.front_face else -outward_normal


# 抽象基类
class Hittable(ABC):
    @abstractmethod
    def hit(self, ray, ray_t) -> Tuple[bool, Optional[HitRecord]]:
        pass

    # @abstractmethod
    # def is_visible(self):
    #     pass
