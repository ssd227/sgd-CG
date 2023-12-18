from utils import INF


class Interval:
    def __init__(self, _min=INF, _max=-INF):  # Default interval is empty

        self.min: float = _min
        self.max: float = _max

    def contains(self, x):
        return self.min <= x <= self.max

    def surrounds(self, x):
        return self.min < x < self.max

    def clamp(self, x):
        if x < self.min: return self.min
        if x > self.max: return self.max
        return x


interval_empty = Interval(INF, -INF)
interval_universe = Interval(-INF, INF)
