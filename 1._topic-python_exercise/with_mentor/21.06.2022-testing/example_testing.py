import unittest


class FirstTest(unittest.TestCase):
    def test_first(self):
        self.assertEqual(2, 2)

    def test_second(self):
        self.assertEqual(2, 3)


# class SecondTest(unittest.TestCase):
#     def test_second(self):
#         self.assertEqual(1, 1)
#