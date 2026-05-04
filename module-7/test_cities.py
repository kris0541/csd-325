# Name: Kris Kleiner
# Date: May 3 2026
# Assignment: Module 7 - Test Cases
# Purpose: Use unittest to verify the city_country function works correctly.

import unittest
from city_functions import city_country


class CityCountryTestCase(unittest.TestCase):
    """Tests for city_functions.py."""

    def test_city_country(self):
        """Test basic city, country format."""
        formatted_location = city_country("santiago", "chile")
        self.assertEqual(formatted_location, "Santiago, Chile")


if __name__ == "__main__":
    unittest.main()