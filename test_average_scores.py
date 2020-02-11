import unittest
import unittest.mock as mock
import sys
from format_output import average_scores

class FunctionTestCase(unittest.TestCase):
    def test_average(self):
        with mock.patch('builtins.input', side_effect=[2, 3, 4]):
            assert average_scores.average() == 3

    def test_average_exception(self):
        with self.assertRaises(ValueError):
            average_scores.average(-90, 89, 78)

if __name__ == '__main__':
    unittest.main()