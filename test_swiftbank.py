import unittest
from unittest.mock import patch
from main import make_deposit, make_withdrawal

class TestSwiftBank(unittest.TestCase):
    @patch('builtins.input', side_effect=['Bank Transfer', 100])
    def test_make_deposit(self, mock_input):
        # Test make_deposit function with mock input
        make_deposit()
        # Add assertions here to check if the function behaves as expected

    @patch('builtins.input', side_effect=['Credit/Debit Card', 50])
    def test_make_withdrawal(self, mock_input):
        # Test make_withdrawal function with mock input
        make_withdrawal()
        # Add assertions here to check if the function behaves as expected

if __name__ == '__main__':
    unittest.main()
