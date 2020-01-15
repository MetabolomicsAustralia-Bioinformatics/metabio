from django.test import SimpleTestCase
from django.urls import reverse, resolve
import metabioapp.conc as conc


class TestConc(SimpleTestCase):

	def test_is_metabolite(self):
	    assert conc.is_metabolite("Glucose") == True


	def test_normalise_self(is_list):
		assert conc.normalise_self([0, 1, 2, 3]) == [0.0, 1.0, 2.0, 3.0]
		assert conc.normalise_self([2, 4, 6, 8]) == [1.0, 2.0, 3.0, 4.0]

	def test_cal_equation(y, equation, origin):



	def normalising_factor(input_dic):