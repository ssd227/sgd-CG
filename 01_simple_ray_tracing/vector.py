from functools import reduce
from math import sqrt, sin, cos

class Vector3:
    def __init__(self, x, y, z):
        self.px = x
        self.py = y
        self.pz = z

    def dot(self, v3):
        s = self.px * v3.px + self.py * v3.py + self.pz * v3.pz
        return s

    def X(self, v3):
        x = self.py * v3.pz - self.pz * v3.py
        y = self.pz * v3.px - self.px * v3.pz
        z = self.px * v3.py - self.py * v3.px
        return Vector3(x, y, z)

    def plus(self, v3):
        x = self.px + v3.px
        y = self.py + v3.py
        z = self.pz + v3.pz
        return Vector3(x, y, z)

    def minus(self, v3):
        x = self.px - v3.px
        y = self.py - v3.py
        z = self.pz - v3.pz
        return Vector3(x, y, z)

    def s_multip(self, k):
        x = k * self.px
        y = k * self.py
        z = k * self.pz
        return Vector3(x, y, z)


    def normalize(self):
        def f(x):
            return x**2
        def g(a,b):
            return a+b
        def h(a,b):
            return a/b

        mo = map(f, [self.px, self.py, self.pz])
        mo = sqrt(reduce(g, mo))
        self.px /= mo
        self.py /= mo
        self.pz /= mo

    def horizontal_rotation(self, theta):
        pi = 3.1415926
        theta_r = theta * pi / 180
        new_x = cos(theta_r) * self.px - sin(theta_r) * self.py
        new_y = sin(theta_r) * self.px + cos(theta_r) * self.py

        self.px = new_x
        self.py = new_y


