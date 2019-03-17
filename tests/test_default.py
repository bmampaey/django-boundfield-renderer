from datetime import date, datetime, timedelta
from django.test import SimpleTestCase
from django.template.loader import get_template
from django.contrib.auth.models import User


from .forms import TestForm

class TestDefault(SimpleTestCase):
	def setUp(self):
		self.template = get_template('default/form.html')
	
	def test_unbound(self):
		form = TestForm()
		self.assertHTMLEqual(str(form), self.template.render({'form': form}))
		
		form = TestForm(required = True)
		self.assertHTMLEqual(str(form), self.template.render({'form': form}))
		
		form = TestForm(disabled = True)
		self.assertHTMLEqual(str(form), self.template.render({'form': form}))
		
		form = TestForm(with_errors = True)
		self.assertHTMLEqual(str(form), self.template.render({'form': form}))
	
	def test_bound(self):
		form = TestForm({})
		self.assertHTMLEqual(str(form), self.template.render({'form': form}))

	def test_initial(self):
		initial = {
			'boolean': True,
			'char': 'test',
			'choice': '1',
			'typedchoice': 1,
			'date': date.today(),
			'datetime': datetime.now(),
			'decimal': 0.1,
			'duration': timedelta(1),
			'email': 'test@test.com',
			'file': 'TODO',
			'filepath': '/tmp',
			'float': 0.1,
			'image': 'TODO',
			'integer': 0,
			'genericipaddress': '127.0.0.1',
			'multiplechoice': ['1', '2'],
			'typedmultiplechoice': [1, 2],
			'nullboolean': True,
			'regex': 'test',
			'slug': 'test',
			'time': datetime.now().time(),
			'url': 'http://127.0.0.1',
			'uuid': '12345678123456781234567812345678',
			'combo': 'test@test.com',
			'splitdatetime': datetime.now(),
			'modelchoice': User.objects.first(),
			'modelmultiplechoice': User.objects.all(),
			'hidden': 'test',
			'textarea': 'multiline\ntest',
			'radio': '1',
			'helptext': 'test',
			'initial': 'Some OTHER initial value',
			'label': 'test',
			'mycharfield': 'Not the Spanish Inquisition',
			'myfield': 'test',
			'mysuperfield': 'test',
		}
		form = TestForm()
		self.assertHTMLEqual(str(form), self.template.render({'form': form}))
