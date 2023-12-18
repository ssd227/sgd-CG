from vector import Color
from interval import Interval
from math import sqrt
import numpy as np


def intensity():
    return Interval(_min=0.000, _max=0.999)


def linear_to_gamma(linear_component):
    return np.sqrt(linear_component)


# 暂时是0-1的颜色，转为0-255的uint8格式
def write_color(pixel_color: Color, samples_per_pixel: int):
    scale = 1.0 / samples_per_pixel
    return Color(*[int(
        255.999 * intensity().clamp(
            linear_to_gamma(
                1.0*pixel_color[i] * scale)))
        for i in range(3)])
