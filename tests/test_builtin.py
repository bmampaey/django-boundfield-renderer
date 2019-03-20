from django.test import TestCase
from django.template.loader import get_template

from forms import BuiltinForm

class TestBuiltin(TestCase):
	def setUp(self):
		self.template = get_template('default/form.html')
	
	def test_unbound(self):
		form = BuiltinForm()
		self.assertHTMLEqual(str(form), self.template.render({'form': form}))
		
		form = BuiltinForm(required = True)
		self.assertHTMLEqual(str(form), self.template.render({'form': form}))
		
		form = BuiltinForm(disabled = True)
		self.assertHTMLEqual(str(form), self.template.render({'form': form}))
		
		form = BuiltinForm(with_errors = True)
		self.assertHTMLEqual(str(form), self.template.render({'form': form}))
	
	def test_bound(self):
		form = BuiltinForm({})
		self.assertHTMLEqual(str(form), self.template.render({'form': form}))

	def test_initial(self):
		form = BuiltinForm(with_initial = True)
		self.assertHTMLEqual(str(form), self.template.render({'form': form}))
