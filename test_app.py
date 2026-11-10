import unittest
from app import add_numbers, greet


class TestApp(unittest.TestCase):

    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_greet(self):
        self.assertEqual(greet("Jenkins"), "Hello, Jenkins! Update: Welcome to the CI/CD pipeline.")


if __name__ == "__main__":
    unittest.main()