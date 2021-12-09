"""Tests for Levenshtein distance"""

import unittest
from levenshtein import calculate_distance as distance


class LevenshteinTest(unittest.TestCase):
    """
    Class to test Levenshtein distance function
    """
    def setUp(self):
        """
        Data setup for test
        """
        self.test_data = [
            ("", "", 0),
            ("qwe", "", 3),
            ("", "w", 1),
            ("q", "w", 1),
            ("import", "import", 0),
            ("import", "impakf", 3),
            ("import", "imp", 3),
            ("тевирп", "привет", 6)
        ]

    def test_dist(self):
        """
        Test fund
        """
        for data in self.test_data:
            self.assertEqual(distance(data[0], data[1]), data[2])
