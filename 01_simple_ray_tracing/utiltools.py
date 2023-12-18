import time
from functools import wraps


def timing(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        t1 = time.time()
        res = f(*args, **kwargs)
        cost_time = time.time() - t1
        print("cost:{:.2f}s".format(cost_time))
        return res
    return decorated