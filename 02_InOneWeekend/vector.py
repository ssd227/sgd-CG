

from typing import TypeAlias
import numpy as np
from utils import my_random


class Vec3:
    def __init__(self, e0=0, e1=0, e2=0):
        self.e = [float(x) for x in [e0, e1, e2]]

    @property
    def x(self):
        return self.e[0]

    @property
    def y(self):
        return self.e[1]

    @property
    def z(self):
        return self.e[2]

    def to_tuple(self):
        return tuple(self.e)

    def length_squared(self):
        return self.x ** 2 + self.y ** 2 + self.z ** 2

    def length(self):
        return np.sqrt(self.length_squared())

    def near_zero(self):
        # // Return true if the vector is close to zero in all dimensions.
        epsilon = 1e-8
        return all([abs(self[i]) < epsilon for i in range(3)])

    # 直接索引 vec3的坐标值
    def __getitem__(self, key):
        return self.e[key]

    def __setitem__(self, key, value):
        self.e[key] = value

    def __str__(self):
        return " Vec3 : " + str(tuple(self.e))

    def __neg__(self):
        return Vec3(*[-x for x in self.e])

    def __add__(self, other):
        if isinstance(other, Vec3):
            return Vec3(*[self[i] + other[i] for i in range(3)])  # vector add
        elif isinstance(other, (int, float)):
            return Vec3(*[self[i] + other for i in range(3)])  # scalar add
        else:
            return NotImplemented  # 表示不支持的类型

    def __radd__(self, other):
        # 当整数在左侧时，调用 __radd__
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Vec3):
            return Vec3(*[self[i] - other[i] for i in range(3)])
        elif isinstance(other, (int, float)):
            return Vec3(*[self[i] - other for i in range(3)])
        else:
            return NotImplemented  # 表示不支持的类型

    def __mul__(self, other):
        if isinstance(other, Vec3):
            return Vec3(*[self[i] * other[i] for i in range(3)])
        elif isinstance(other, (int, float)):
            return Vec3(*[self[i] * other for i in range(3)])
        else:
            return NotImplemented  # 表示不支持的类型

    def __rmul__(self, other):
        # 当整数在左侧时，调用 __rmul__
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, Vec3):
            if other[0] != 0 and other[1] != 0 and other[2] != 0:
                return Vec3(*[self[i] / other[i] for i in range(3)])
            else:
                raise ValueError("Division by vector having zero items")

        elif isinstance(other, (int, float)):
            if other != 0:
                return Vec3(*[self[i] / other for i in range(3)])
            else:
                raise ValueError("Division by zero")
        else:
            return NotImplemented  # 表示不支持的类型

    def __eq__(self, other) -> bool:
        if isinstance(other, Vec3):
            return abs((self - other).length() - 0) < 1e-8
            # return all([self[i] == other[i] for i in range(3)])
        else:
            return False  # 表示不支持的类型

    def dot(self, other: 'Vec3') -> 'Vec3':
        return sum(self * other)

    # 右手定则
    def cross(self, other: 'Vec3') -> 'Vec3':
        u = self
        v = other
        return Vec3(*[
            u[1] * v[2] - u[2] * v[1],
            u[2] * v[0] - u[0] * v[2],
            u[0] * v[1] - u[1] * v[0]])

    def unit_vector(self) -> 'Vec3':
        return self / self.length()

    @staticmethod
    def random():
        # 使用静态方法创建类的实例
        return Vec3(my_random(), my_random(), my_random())

    @staticmethod
    def random_in_interval(_min, _max):
        # 使用静态方法创建类的实例
        return Vec3(my_random(_min, _max), my_random(_min, _max), my_random(_min, _max))


def random_in_unit_disk() -> Vec3:
    while True:
        p = Vec3(my_random(-1, 1), my_random(-1, 1), 0)
        if p.length_squared() < 1:
            return p


def random_in_unit_sphere() -> Vec3:
    while True:
        p = Vec3.random_in_interval(-1, 1)
        if p.length_squared() < 1:
            return p


def random_unit_vector() -> Vec3:
    return random_in_unit_sphere().unit_vector()


def random_on_hemisphere(normal: Vec3) -> Vec3:
    on_unit_sphere = random_unit_vector()
    if normal.dot(on_unit_sphere) > 0.0:  # In the same hemisphere as the normal
        return on_unit_sphere
    else:
        return -on_unit_sphere


def reflect(v: Vec3, n: Vec3) -> Vec3:
    return v - 2 * v.dot(n) * n


def refract(uv: Vec3, n: Vec3, etai_over_etat: float) -> Vec3:
    cos_theta = min(n.dot(-uv), 1.0)
    r_out_perp = etai_over_etat * (uv + cos_theta * n)
    r_out_parallel = -np.sqrt(abs(1.0 - r_out_perp.length_squared())) * n
    return r_out_perp + r_out_parallel


Color: TypeAlias = Vec3
Point3: TypeAlias = Vec3
