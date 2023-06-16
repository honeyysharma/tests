import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])

    def test_assert_raises(self):
        s = 'hello world'

        # check that s.split fails when the separator is not a string
        # s.split(2) will raise a TypeError. if raised the test will pass else fail. Try ValueError for an experiment.
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main(verbosity=2)