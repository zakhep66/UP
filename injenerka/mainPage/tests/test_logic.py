from django.test import TestCase

from tests.logic import operations


class LogicTestCase(TestCase):
	def test_plus(self):
		result = operations(1, 2, '+')
		self.assertEqual(3, result)
