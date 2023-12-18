from hittable import Hittable, HitRecord
from typing import Tuple, Optional
from interval import Interval


class HittableList(Hittable):
    def __init__(self):
        self.objects = []

    def add(self, obj: Hittable):
        self.objects.append(obj)

    def hit(self, ray, ray_t) -> Tuple[bool, Optional[HitRecord]]:
        # temp_rec = None # 由于python方面的设计思考，每次都返回一个新的hit_record
        res_rec = None  # 当前hit调用需要返回的最终结果
        hit_anything = False
        closest_so_far = ray_t.max

        # 遍历需要render的对象
        for obj in self.objects:
            hit, rec = obj.hit(ray, Interval(ray_t.min, closest_so_far))
            if hit:
                hit_anything = True
                closest_so_far = rec.t
                res_rec = rec

        if hit_anything:
            return (True, res_rec)

        return (False, None)
