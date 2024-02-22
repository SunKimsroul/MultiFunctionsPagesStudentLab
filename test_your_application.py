# test_application.py

import unittest
from data_processor import format_name, calculate_age

class TestDataProcessor(unittest.TestCase):
    def test_format_name(self):
        self.assertEqual(format_name('john', 'doe'), 'John Doe')
    
    def test_calculate_age(self):
        # Assuming the current year is 2024 for this example
        self.assertEqual(calculate_age(2000), 24)

if __name__ == '__main__':
    unittest.main()
