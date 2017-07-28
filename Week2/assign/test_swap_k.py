import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    # Add your test methods for a1.swap_k here.
    def test_swap_k_case_1(self):
        """ Test swap_k with ([1], 0)."""
        actual = [1]
        a1.swap_k(actual,0)
        expected = [1]
        self.assertEqual(actual, expected)

    def test_swap_k_case_2(self):
        """ Test swap_k with ([1,2], 1). """
        actual = [1, 2]
        a1.swap_k(actual, 1)
        expected = [2, 1]
        self.assertEqual(actual, expected)

    def test_swap_k_case_3(self):
        """ Test swap_k with a general case ([1, 2, 3, 4, 5], 2). """
        actual = [1, 2, 3, 4, 5]
        a1.swap_k(actual, 2)
        expected = [4, 5, 3, 1, 2]
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(exit=False)
