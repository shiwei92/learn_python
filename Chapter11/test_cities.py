import unittest
from city_functions import get_city_country
 
class CityCountryTestCase(unittest.TestCase):
	def test_city_country(self):
		city_country=get_city_country("zhengzhou","china")
		self.assertEqual(city_country,"Zhengzhou China")
	def test_city_country_population(self):
		city_country_population=get_city_country("shanghai","china",500000)
		self.assertEqual(city_country_population,"Shanghai China 500000")
unittest.main()