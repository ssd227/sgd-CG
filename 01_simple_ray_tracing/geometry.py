from vector import *


class Light:
    def __init__(self, pos=Vector3(-1000, 0, 1000), i=255):
        self.position = pos
        self.I = i

class HitRecord:
    def __init__(self, kakskdp, nvl, i):
        # for shading coefficients
        self.Ka, self.Ks, self.Kd, self.p = kakskdp

        # for vectors
        self.n, self.v, self.l = nvl

        # for light intense
        self.I = i


class Surface:

    def hit(self, ray, light, t0, t1):
        pass

class Ground(Surface):
    def __init__(self):
        self.p0_in_earth = Vector3(0, 0, 0)
        self.n = Vector3(0, 0, 1)
        self.Ka, self.Ks, self.Kd, self.p = (0.4, 0.5, 0.3, 20)

    def hit(self, ray, light, t0, t1):
        def black_white_ground(p):
            magic_number = (p.px//200+p.py//200) % 2
            if magic_number:
                return 0.8
            else:
                return 0.1

        ###########################
        is_hit = False

        # find t
        nd = self.n.dot(ray.direction)
        if abs(nd) < 0.001:
            return is_hit, None, None
        np0 = self.n.dot(self.p0_in_earth)
        nori = self.n.dot(ray.origin)

        t = (np0 - nori)/nd
        if not t0 < t < t1:
            return is_hit, None, None
        # end

        p = ray.origin.plus(ray.direction.s_multip(t))
        self.Kd = black_white_ground(p)

        v = ray.origin.minus(p)
        v.normalize()
        n = self.n
        n.normalize()
        l = light.position.minus(p)
        l.normalize()

        is_hit = True

        rec = HitRecord((self.Ka, self.Ks, self.Kd, self.p), (n, v, l), light.I)
        return is_hit, t, rec


class Sphere(Surface):
    def __init__(self, center=Vector3(0, 800, 0), radius=100, kakskdp=(0.4, 0.5, 0.3, 20)):
        #  shape of sphere
        self.center = center
        self.radius = radius

        # variables for shading
        self.Ka, self.Ks, self.Kd, self.p = kakskdp

    def hit(self, ray, light, t0, t1):
        def in_scope(t):
            if t0 < t < t1:
                return True
            else:
                return False

        is_hit = False

        # find t
        e_minus_c = ray.origin.minus(self.center)
        dd = ray.direction.dot(ray.direction)
        d_e_c =ray.direction.dot(e_minus_c)

        delta = d_e_c**2 \
                - dd * (e_minus_c.dot(e_minus_c) - self.radius**2)

        if delta < 0:
            return is_hit, None, None
        else:
            t_a = (-1 * d_e_c + sqrt(delta)) / dd
            t_b = (-1 * d_e_c - sqrt(delta)) / dd

        if in_scope(t_b):
            t = t_b
        elif in_scope(t_a):
            t = t_a
        else:
            return is_hit, None, None
        # end

        p = ray.origin.plus(ray.direction.s_multip(t))

        v = ray.origin.minus(p)
        v.normalize()
        n = p.minus(self.center)
        n.normalize()
        l = light.position.minus(p)
        l.normalize()

        is_hit = True

        rec = HitRecord((self.Ka, self.Ks, self.Kd, self.p), (n, v, l), light.I)
        return is_hit, t, rec



# class Triangle(Surface):
#     def __init__(self):
#         # shape of triangle
#         self.point_a =
#         self.point_b =
#         self.point_c =
#
#
#     def hit(self,ray,light,t0,t1):

