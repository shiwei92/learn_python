import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
	def test_first_last_name(self):
		formatted_name=get_formatted_name("tony","stark")
		self.assertEqual(formatted_name,"Tony Stark")
	def test_first_middle_last_name(self):
		formatted_name=get_formatted_name("tony","stark","edward")
		self.assertEqual(formatted_name,"Tony Edward Stark")
unittest.main()
