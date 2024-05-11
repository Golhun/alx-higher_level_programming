import unittest
from your_module import Rectangle

class TestRectangle(unittest.TestCase):
    def test_init(self):
        rect = Rectangle(10, 20, 5, 5)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 5)

    def test_area(self):
        rect = Rectangle(10, 20, 5, 5)
        self.assertEqual(rect.area(), 200)

    def test_perimeter(self):
        rect = Rectangle(10, 20, 5, 5)
        self.assertEqual(rect.perimeter(), 60)

    def test_translate(self):
        rect = Rectangle(10, 20, 5, 5)
        rect.translate(10, 10)
        self.assertEqual(rect.x, 15)
        self.assertEqual(rect.y, 15)

if __name__ == '__main__':
    unittest.main()
