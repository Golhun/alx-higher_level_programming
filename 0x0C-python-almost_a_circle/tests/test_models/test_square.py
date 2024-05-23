import unittest
import io
import contextlib
from models.square import Square

class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def test_instantiation(self):
        """Test instantiation of Square."""
        s = Square(5)
        self.assertIsInstance(s, Square)

    def test_size_initialization(self):
        """Test initialization of size attribute."""
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_x_and_y_attributes(self):
        """Test initialization of x and y attributes."""
        s = Square(5, 2, 3)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_order_of_initialization(self):
        """Test order of initialization."""
        with self.assertRaises(TypeError):
            Square(5, 2, 3, 4)

    def test_area_method(self):
        """Test the area method of Square."""
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_stdout(self):
        """Test stdout output."""
        s = Square(5)
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            print(s)
            output = buf.getvalue().strip()
        self.assertEqual(output, '[Square] (1) 0/0 - 5')

    def test_update_methods(self):
        """Test update methods of Square."""
        s = Square(5)
        s.update(10)
        self.assertEqual(s.size, 10)
        s.update(20, 2, 3)
        self.assertEqual(s.size, 20)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_to_dictionary_method(self):
        """Test to_dictionary method of Square."""
        s = Square(5, 2, 3)
        expected_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        self.assertDictEqual(s.to_dictionary(), expected_dict)

if __name__ == "__main__":
    unittest.main()
