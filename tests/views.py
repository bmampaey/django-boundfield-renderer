from django.views.generic import FormView
from django.urls import reverse

from forms import TestForm

class TestFormView(FormView):
	form_class = TestForm
	template_name = 'test_form.html'
	
	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		for option in ('required', 'disabled', 'with_errors'):
			if option in self.kwargs:
				kwargs[option] = self.kwargs[option]
		return kwargs
	
	def get_initial(self):
		# TODO remove this
		from datetime import date, datetime, timedelta
		from django.contrib.auth.models import User
		
		return {
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
	
	def form_valid(self, form):
		return self.render_to_response(self.get_context_data(form=form))
