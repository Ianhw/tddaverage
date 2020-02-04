import unittest
from format_output import average_scores

class FunctionTestCase(unittest.TestCase):
    def test_average(self):
        self.assertEqual(3, average_scores.average( 2, 3, 4))




if __name__ == '__main__':
    unittest.main()