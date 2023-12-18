import random
import time

# Usings

# using std::shared_ptr;
# using std::make_shared;
# using std::sqrt;

# Constants

INF = float('inf')  # 正无穷大
# negative_infinity = float('-inf') # 负无穷大

PI = 3.1415926535897932385


# Utility Functions

def degrees_to_radians(degrees):
    return degrees * PI / 180.0

def my_random(_min=0, _max=1):
    # Returns a random real in [min,max).
    return _min + (_max - _min) * random.random()


# Common Headers
# from ray import *
# from vector import *
# from interval import *


def timing(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"{func.__name__} took {elapsed_time:.4f} seconds to execute.")
        return result

    return wrapper
