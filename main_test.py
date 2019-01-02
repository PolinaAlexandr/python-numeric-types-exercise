import unittest
import main


class MainTest(unittest.TestCase):

    def test_square_area(self):
        self.assertEqual(main.square_area(5), 25)
    
    def test_rectangle_area(self):
        self.assertEqual(main.rectangle_area(3, 4), 12)
    
    def test_triangle_area(self):
        self.assertEqual(main.triangle_area(2, 3, 4), 24)
    
    def test_parallelogram_area_sin(self):
        self.assertEqual(main.parallelogram_area_sin(2, 4, 60), 480)
    
    def test_parallelogram_area_base(self):
        self.assertEqual(main.parallelogram_area_base(3, 6), 18)
    
    def test_degree_to_radians(self):
        result = main.degree_to_radians(57.29577951308232)
        expected = 1.0
    
        self.assertTrue(self.is_close(result, expected))
    
    @staticmethod
    def is_close(a, b, rel_tol=1e-13, abs_tol=0.0):
        return abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)
    
    def test_radians_to_degrees(self):
        result = main.radians_to_degrees(1.0)
        expected = 57.29577951308232
        
        self.assertTrue(self.is_close(result, expected))
    
    def test_square_equation_roots(self):
            self.assertEqual(main.square_equation_roots(1, 2, -48), (6.0, -8.0))
    
    def test_leap_year(self):
        self.assertTrue(main.is_leap(2004))

if __name__ == '__main__':
    unittest.main()