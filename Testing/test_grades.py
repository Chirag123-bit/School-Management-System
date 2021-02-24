import unittest
import model.Grades

class Test_Grades(unittest.TestCase):
    def setUp(self):
        self.g = model.Grades.Grades()

    def test_set_math(self):
        self.g.set_math(100)
        self.assertEqual(100,self.g.get_math())  # Test Passed
        self.g.set_math(90)
        self.assertEqual(90, self.g.get_math())  # Test Passed
        self.assertRaises(ValueError,self.g.set_math, 900)  # Test Passed
        self.assertRaises(TypeError,self.g.set_math, "100")  # Test Passed


    def test_set_science(self):
        self.g.set_science(50)
        self.assertEqual(50,self.g.get_science())  # Test Passed
        self.g.set_science(10)
        self.assertEqual(10, self.g.get_science())  # Test Passed
        self.assertRaises(ValueError, self.g.set_science, 900)  # Test Passed
        self.assertRaises(TypeError, self.g.set_science, "100")  # Test Passed


    def test_set_geography(self):
        self.g.set_geography(100)
        self.assertEqual(100, self.g.get_geography())  # Test Passed
        self.g.set_geography(90)
        self.assertEqual(90, self.g.get_geography())  # Test Passed
        self.assertRaises(TypeError,self.g.set_geography,"11")  # Test Passed
        self.assertRaises(ValueError,self.g.set_geography, 1110)  # Test Passed


    def test_set_computer(self):
        self.g.set_computer(100)
        self.assertEqual(100, self.g.get_computer())  # Test Passed
        self.g.set_computer(90)
        self.assertEqual(90, self.g.get_computer())  # Test Passed
        self.assertRaises(TypeError,self.g.set_computer,"100")  # Test Passed
        self.assertRaises(ValueError,self.g.set_computer, 101)  # Test Passed

    def tearDown(self):
        del self.g