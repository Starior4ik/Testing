import unittest

import rectangle

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
       res = rectangle.area(10, 0)
       self.assertEqual(res, 0)
       
    def test_square_mul(self):
       res = rectangle.area(10, 10)
       self.assertEqual(res, 100)
    
    def test_edge_mul(self):
       res = rectangle.area(9857465879, 567375868)
       self.assertEqual(res, 9857465879 * 567375868)

    def test_area_float(self):
       res = rectangle.area(3.14, 3.25)
       self.assertAlmostEqual(res, 3.14 * 3.25)
   
    def test_perimeter(self):
      res = rectangle.perimeter(23,2)
      self.assertEqual(res, 50)
   
    def test_perimeter_edge(self):
      res = rectangle.perimeter(347543345, 43858954879345)
      self.assertEqual(res,(347543345 + 43858954879345) * 2)
    
    def test_perimeter_float(self):
       res = rectangle.perimeter(3.14, 3.25)
       self.assertAlmostEqual(res, (3.14 + 3.25) * 2)
