import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    # Add your test methods for a1.stock_price_summary here.
    def test_stock_price_summary_1(self):
        """ Test stock_price_summary with [1,0,-1]. """
        actual = a1.stock_price_summary([1,0,-1])
        expected = (1,-1)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_2(self):
        """ Test stock_price_summary with [0] to see if it can handle the simplest situation."""
        actual = a1.stock_price_summary([0])
        expected = (0, 0)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_3(self):
        """ Test stock_price_summary with [1,-1,1,-1] to see if it can return (0,0)."""
        actual = a1.stock_price_summary([1,-1,1,-1, 0])
        expected = (2, -2)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_4(self):
        """ Test stock_price_summary with blank list []. """
        actual = a1.stock_price_summary([])
        expected = (0, 0)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_5(self):
        """ Test stock_price_summary with one single item [1]. """
        self.assertEqual((0,0), a1.stock_price_summary([1]))

    def test_stock_price_summary_6(self):
        """ Test stock_price_summary with one single item [-1]. """
        self.assertEqual((0, 0), a1.stock_price_summary([-1]))

    def test_stock_price_summary_7(self):
        """ Test stock_price_summary with one single item [0]. """
        self.assertEqual((0, 0), a1.stock_price_summary([0]))


if __name__ == '__main__':
    unittest.main(exit=False)
