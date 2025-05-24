 import unittest
from city_function import get_city_country

class CityCountryTestCase(unittest.TestCase):
    """Test for 'city_function.py'."""

    def test_city_country(self):
        """Do city-country pairs like 'Santiago, Chile' work?"""
        formatted_city_country = get_city_country('Santiago', 'Chile')
        self.assertEqual(formatted_city_country, 'Santiago, Chile')

if __name__ == '__main__':
    unittest.main()
