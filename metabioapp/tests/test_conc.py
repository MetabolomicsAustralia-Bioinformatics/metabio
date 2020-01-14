from django.test import SimpleTestCase
from django.urls import reverse, resolve
import metabioapp.conc as conc


class TestConc(SimpleTestCase):

	def test_is_metabolite(self):
	    assert conc.is_metabolite("Glucose") == True

	def test_normalise_self(is_list):
		"""Test can't be written because conc.normalise_self doesn't have a return statement.
		"""
		pass

	def test_cal_equation(y, equation, origin):
		


	def normalising_factor(input_dic):