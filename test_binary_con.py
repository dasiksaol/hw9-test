import unittest
from binary_con import binary_con


class TestBinary_Con(unittest.TestCase):
    def test_binary_con_to_decimal(self):
        self.assertEqual(binary_con('bd', 1001), 9)
        self.assertEqual(binary_con('bd', 101), 5)

    def test_binary_con_to_binary(self):
        self.assertEqual(binary_con('db', 90), 1011010)
        self.assertEqual(binary_con('db', 44), 101100)


if __name__ == '__main__':
    unittest.main()
