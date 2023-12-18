from PIL import Image
import numpy as np

from camera import *

from geometry import *


def iprint(v3):
    print(v3.px, v3.py, v3.pz)

#######################################
            # # refraction
            # K_r = 0.5
            # nv = rec.n.dot(rec.v)
            # if nv > 0:
            #     N = 1
            #     Nt = 1.5
            #
            #     d = rec.v.s_multip(-1)
            #     dn = -1 * nv
            #     term1 = d.minus((rec.n.s_multip(dn)))
            #     term11 = term1.s_multip((N/Nt))
            #
            #     tt = 1-(N**2 * (1 - dn**2))/(Nt**2)
            #     if tt > 0:
            #         term2 = sqrt(tt)
            #         term22 = rec.n.s_multip(term2)
            #         refr = term11.minus(term22)
            #         return K_r * ray_color(Ray(p, refr), t0, t1, depth+2)
            #
            #
            # else:
            #     N = 1.5
            #     Nt = 1
            #
            #     d = rec.v.s_multip(-1)
            #     dn = -1 * nv
            #     term1 = d.minus((rec.n.s_multip(dn)))
            #     term11 = term1.s_multip((N/Nt))
            #
            #     tt = 1-(N**2 * (1 - dn**2))/(Nt**2)
            #     if tt > 0:
            #         term2 = sqrt(tt)
            #         term22 = rec.n.s_multip(term2)
            #         refr = term11.minus(term22)
            #         c += K_r * ray_color(Ray(p, refr), t0, t1, depth+2)
            #

#######################################
# x = Vector3(1, 0, 0)
# y = Vector3(0, 1, 0)
# z = Vector3(0, 0, 1)
#
# y.vertical_rotation(90)
# z.vertical_rotation(90)
#
# x.horizontal_rotation(90)
# y.horizontal_rotation(90)
#
# iprint(x)
# iprint(y)
# iprint(z)

########################################
# n=0
# if n:
#     print(True)
# else:
#     print(False)

#########################################
# qiu = Sphere(Vector3(0, 500, 300), 300)
# is_hit, t, rec = qiu.hit(Ray(Vector3(0, 0, 0), Vector3(0, 1, 0)), Light(Vector3(0, 0, 200), 255), 5, 1000000)
#
# print('c')
# iprint(qiu.center)
# print('r')
# print(qiu.radius)
#
#
#
#
# print("is hit?:", is_hit)
# print("t ", t)
#
# print("ka ks kd p  ")
# print(rec.Ka)
# print(rec.Ks)
# print(rec.Kd)
# print(rec.p)
#
# print('n v l  ')
# iprint(rec.n)
# iprint(rec.v)
# iprint(rec.l)
#
# print('Intense of light', rec.I)


#########################################
# p1=Vector3(1,1,1)
# p2=Vector3(1,2,3)
#
# x=Vector3(1,0,0)
# y=Vector3(0,1,0)
# z=Vector3(0,0,1)
#
# p = Vector3(2,2,2)
# iprint(p)
# p.normalize()
# iprint(p)
# iprint(x.plus(y))
# iprint(x.minus(y))
# iprint(x.X(y))
#
# print(p1.dot(p2))
# iprint(p1.s_multip(-5))
#
# #######################################
# ca = Camera(100, 200)
#
# iprint(ca.eye_position)
#
# print('V')
# iprint(ca.V)
# print('W')
# iprint(ca.W)
# print('U')
# iprint(ca.U)
#
# print(ca.window_H, ca.window_W)
# print(ca.plane_H, ca.plane_W,)
# print(ca.t, ca.b, ca.l, ca.r)
# print(ca.d)
#
# ray = ca.ray_generator(0, 100)
# print("ray.origin")
# iprint(ray.origin)
# iprint(ray.direction)


#######################################

#a = np.arange(15).reshape(3, 5)
#print(a)


#im = Image.open('1.png')
#r,g,b = im.split()
#print(r)
#r.show()

#im = Image.new('L',(100,100),0)


