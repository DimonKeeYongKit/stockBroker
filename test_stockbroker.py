import unittest
from stockbroker import is_valid_trade, process_trade

class TestStockBroker(unittest.TestCase):

    def setUp(self):
        self.valid_stocks = {"AAPL", "GOOG", "TSLA"}

    def test_buy_aapl_valid(self):
        self.assertTrue(is_valid_trade("buy", "AAPL", 1000.00, 100, self.valid_stocks))

    def test_sell_aapl_valid(self):
        self.assertTrue(is_valid_trade("sell", "AAPL", 1000.10, 10, self.valid_stocks))

    def test_sell_aapl_edge_max_volume(self):
        self.assertTrue(is_valid_trade("sell", "AAPL", 1200.00, 1000000, self.valid_stocks))

    def test_buy_googl_valid(self):
        self.assertFalse(is_valid_trade("buy", "GOOGL", 1200.00, 200, self.valid_stocks))

    def test_buy_aapl_invalid_price_too_low(self):
        self.assertFalse(is_valid_trade("buy", "AAPL", 0.49, 50, self.valid_stocks))

    def test_buy_invalid_stock_code(self):
        self.assertFalse(is_valid_trade("buy", "MSFT", 1000.00, 100, self.valid_stocks))

    def test_sell_aapl_valid_price_extreme(self):
        self.assertTrue(is_valid_trade("sell", "AAPL", 2000.00, 5, self.valid_stocks))

    def test_sell_aapl_negative_price(self):
        self.assertFalse(is_valid_trade("sell", "AAPL", -2000.00, 5, self.valid_stocks))

    def test_sell_aapl_negative_volume(self):
        self.assertFalse(is_valid_trade("sell", "AAPL", 1200.00, -1, self.valid_stocks))

    def test_sell_aapl_zero_volume(self):
        self.assertFalse(is_valid_trade("sell", "AAPL", 1200.00, 0, self.valid_stocks))

    def test_sell_aapl_volume_exceeds_max(self):
        self.assertFalse(is_valid_trade("sell", "AAPL", 1200.00, 2000000, self.valid_stocks))

    def test_process_new_trade(self):
        orders = []
        process_trade(["buy", "AAPL", 100.00, 50], orders)
        self.assertEqual(len(orders), 1)
        self.assertEqual(orders[0], ["buy", "AAPL", 100.00, 50])

    def test_process_existing_trade(self):
        orders = [["buy", "AAPL", 100.00, 50]]
        process_trade(["buy", "AAPL", 100.00, 25], orders)
        self.assertEqual(len(orders), 1)
        self.assertEqual(orders[0][3], 75)

if __name__ == "__main__":
    unittest.main()