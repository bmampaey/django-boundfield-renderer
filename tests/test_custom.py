from django.test import TestCase
from django.template.loader import get_template

from forms import CharFieldForm, MyCharFieldForm, MyOtherCharFieldForm, MyFieldForm, MySuperFieldForm

class TestCustom(TestCase):
	def setUp(self):
		self.template = get_template('default/form.html')
	
	def test_CharField(self):
		form = CharFieldForm()
		with self.assertTemplateUsed('default/field.html', count=1):
			self.template.render({'form': form})
	
	def test_MyCharField(self):
		form = MyCharFieldForm()
		with self.assertTemplateUsed('default/field.html', count=1):
			self.template.render({'form': form})
	
	def test_MyOtherCharField(self):
		form = MyOtherCharFieldForm()
		with self.assertTemplateUsed('custom/my_other_char_field.html', count=1):
			self.template.render({'form': form})
	
	def test_MyField(self):
		form = MyFieldForm()
		with self.assertTemplateUsed('custom/my_field.html', count=2):
			self.template.render({'form': form})
	
	def test_MySuperField(self):
		form = MySuperFieldForm()
		with self.assertTemplateUsed('custom/my_field.html', count=2):
			self.template.render({'form': form})
