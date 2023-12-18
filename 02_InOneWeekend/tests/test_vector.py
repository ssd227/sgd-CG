import unittest
import logging
from vector import Vec3
# from vector_np import Vec3

# class TestVec3Base(unittest.TestCase):
#     def test_init(self):
#         self.assertEqual(vc, va+vb)
        

class TestVec3Add(unittest.TestCase):
    def test_elem_add(self):
        va = Vec3(1,2,3)
        vb = Vec3(1,1,1)
        vc = Vec3(2,3,4)
        self.assertEqual(vc, va+vb)
    
    # 左加: int + Vec3
    def test_scalar_radd(self):
        va = Vec3(1,2,3)
        vc = Vec3(2,3,4)
        self.assertEqual(vc, 1+va)
    
    # 右加: vec3 + float
    def test_scalar_add(self):
        va = Vec3(1,2,3)
        vc = Vec3(3,4,5)
        self.assertEqual(vc, va+2.0)
        
class TestVec3Sub(unittest.TestCase):
    def test_elem_sub(self):
        va = Vec3(0,1,2)
        vb = Vec3(1,1,1)
        vc = Vec3(-1,0,1)
        self.assertEqual(va-vb, vc)
    
    def test_neg(self):
        va = Vec3(1,2,3)
        vc = Vec3(-1,-2,-3)
        self.assertEqual(-va, vc)
    
    def test_scalar_sub(self):
        va = Vec3(1,2,3)
        vc = Vec3(-2,-1,0)
        self.assertEqual(va-3.0, vc)

class TestVec3Multiply(unittest.TestCase):
    def test_elem_multiply(self):
        va = Vec3(1,2,3)
        vb = Vec3(1,1,2)
        vc = Vec3(1,2,6)
        self.assertEqual(va*vb, vc)
        
    def test_scalar_multiply(self):
        va = Vec3(1,2,3)
        vc = Vec3(2,4,6)
        self.assertEqual(2*va, vc)
        
class TestVec3Div(unittest.TestCase):
    def test_elem_truediv(self):
        va = Vec3(1,2,3)
        vb = Vec3(2,1,2)
        vc = Vec3(0.5, 2, 1.5)
        self.assertEqual(va/vb, vc)
        
    def test_scalar_truediv(self):
        va = Vec3(1,2,3)
        vc = Vec3(0.5,1,1.5)
        self.assertEqual(va/2, vc)
    
    def test_divide_by_zero_vector(self):
        with self.assertRaises(ValueError) as context:
            va = Vec3(1,2,3)
            vb = Vec3(0.5,1,0)
            va/vb
        self.assertEqual(str(context.exception), "Division by vector having zero items")
        
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError) as context:
            res = Vec3(1,2,3) / 0
        self.assertEqual(str(context.exception), "Division by zero")

class TestVec3Ops(unittest.TestCase):
    def test_length(self):
        va = Vec3(1,0,0)
        self.assertEqual(va.length(), 1)

    def test_dot(self):
        va = Vec3(1,2,3)
        vb = Vec3(1,1,1)
        self.assertEqual(va.dot(vb), 6)

    def test_corss(self):
        vx = Vec3(1,0,0)
        vy = Vec3(0,1,0)
        vz = Vec3(0,0,1)
        self.assertEqual(vx.cross(vy), vz)
        
    def test_unit_length(self):
        va = Vec3(-12,100,2)
        self.assertTrue(abs(va.unit_vector().length()-1) < 1e-8)
        

if __name__ == '__main__':
    unittest.main()