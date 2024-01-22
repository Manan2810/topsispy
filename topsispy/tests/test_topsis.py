import unittest
from topsispy.topsis import topsis

class TestTOPSIS(unittest.TestCase):

    def test_topsis_positive_impact(self):
        matrix = [
            [250, 16, 12, 4],
            [200, 8, 15, 2],
            [300, 20, 10, 5],
            [275, 18, 18, 3]
        ]
        weights = [0.25, 0.25, 0.25, 0.25]
        impacts = ['+', '+', '+', '-']

        result = topsis(matrix, weights, impacts)

        # Add assertions based on expected results
        self.assertAlmostEqual(result[0], 0.693, places=3)
        self.assertAlmostEqual(result[1], 0.554, places=3)
        self.assertAlmostEqual(result[2], 0.832, places=3)
        self.assertAlmostEqual(result[3], 0.770, places=3)

    # Add more test methods for different test cases if needed

if __name__ == '__main__':
    unittest.main()
