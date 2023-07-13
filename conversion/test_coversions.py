import unittest
import binary_to_int
import int_to_binary


class TestCoversions(unittest.TestCase):

    def test_binary_to_int(self):
        self.assertEqual(binary_to_int.binary_to_int(100), int(str(100), 2), "Binary to integer conversion is wrong.")

    def test_int_to_binary(self):
        self.assertEqual(int_to_binary.int_to_binary(4), int('{0:b}'.format(4)), "Integer to binary conversion is wrong.")


if __name__ == '__main__':
    unittest.main(verbosity=2)