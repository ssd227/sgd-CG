from vector import *

class Ray:
    def __init__(self, ori, dir):
        self.direction = dir
        self.origin = ori

class Camera:
    def __init__(self, height, width, eye_pos=Vector3(0, -100, 0),\
                 V = Vector3(0, 0, 1), W = Vector3(0, -1, 0)):

        self.eye_position = eye_pos

        # the three basis of the camera
        self.V = V
        V.normalize()
        self.W = W
        W.normalize()
        self.U = self.V.X(self.W)

        # the fllowing h and w are the size of the origin image
        self.window_H = height
        self.window_W = width

        # keep the scale of the view plane
        self.plane_H = 100
        self.plane_W = self.plane_H * width/height

        # top down left right of the view plane
        self.t = self.plane_H / 2
        self.b = -self.plane_H / 2
        self.l = -self.plane_W / 2
        self.r = self.plane_W / 2

        # distance from the eye to the view plane
        self.d = 100

    def ray_generator(self, i, j):
        u = self.l + self.plane_W * ((j+0.5) / self.window_W)
        v = self.b + self.plane_H * ((i+0.5) / self.window_H)

        # print((j+0.5) / self.window_W)
        # print((i+0.5) / self.window_H)
        # print("in the fun ray_generator",u,v)

        uU = self.U.s_multip(u)
        vV = self.V.s_multip(v)
        _dW = self.W.s_multip(-1 * self.d)

        # -dW + uU +vV
        dir = _dW.plus(vV).plus(uU)
        dir.normalize()
        dir.pz *= (-1)

        ori = self.eye_position

        return Ray(ori, dir)


class CameraV2:
    def __init__(self, height, width, eye_pos=Vector3(0, -100, 0), theta=0):

        self.eye_position = eye_pos

        # the three basis of the camera
        self.V = Vector3(0, 0, 1)
        self.W = Vector3(0, -1, 0)
        self.U = Vector3(1, 0, 0)

        # rotation
        self.W.horizontal_rotation(theta)
        self.U.horizontal_rotation(theta)


        # the fllowing h and w are the size of the origin image
        self.window_H = height
        self.window_W = width

        # keep the scale of the view plane
        self.plane_H = 100
        self.plane_W = self.plane_H * width/height

        # top down left right of the view plane
        self.t = self.plane_H / 2
        self.b = -self.plane_H / 2
        self.l = -self.plane_W / 2
        self.r = self.plane_W / 2

        # distance from the eye to the view plane
        self.d = 100

    def ray_generator(self, i, j):
        u = self.l + self.plane_W * ((j+0.5) / self.window_W)
        v = self.b + self.plane_H * ((i+0.5) / self.window_H)

        # print((j+0.5) / self.window_W)
        # print((i+0.5) / self.window_H)
        # print("in the fun ray_generator",u,v)

        uU = self.U.s_multip(u)
        vV = self.V.s_multip(v)
        _dW = self.W.s_multip(-1 * self.d)

        # -dW + uU +vV
        dir = _dW.plus(vV).plus(uU)
        dir.normalize()
        dir.pz *= (-1)

        ori = self.eye_position

        return Ray(ori, dir)
