import unittest

class TestBuiltins(unittest.TestCase):
    def test_membership(self):
        self.assertIn("A", "Andalusia")
        self.assertTrue("a" in "Andalusia")
        self.assertNotIn("r" in "Andalusia")

    def test_instances(self):
        self.assertIsInstance(5, int)
        self.assertTrue(isinstance(5, int))

    def test_falsehood(self):
        self.assertFalse(False)

    def test_instances(self):
        self.assertNotIsInstance(5.5, int)  # 5.0 is a float, it is True
        self.assertIsInstance(5.0, float)  # 5.0 is float it is True

    def test_falsehood(self):
        self.assertFalse(False)

