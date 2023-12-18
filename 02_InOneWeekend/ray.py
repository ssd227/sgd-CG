from vector import Point3, Vec3


class Ray:
    def __init__(self, ori=Point3(0, 0, 0), dire=Vec3(0, 0, 0)):
        self.ori = ori
        self.dire = dire

    def origin(self):
        return self.ori

    def direction(self):
        return self.dire

    def at(self, t):
        return self.ori + t * self.dire
