from main import fib
from unittest import TestCase


class FibonacciTestCase(TestCase):

    def test_first_fibonacci_number_is_1(self):
        x = fib(1)
        self.assertEqual(1, x)
