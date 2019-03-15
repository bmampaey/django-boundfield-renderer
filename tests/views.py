from django.views.generic import FormView
from django.urls import reverse

from forms import TestForm

class TestFormView(FormView):
	form_class = TestForm
	template_name = 'test_form.html'
	
	def form_valid(self, form):
		return self.render_to_response(self.get_context_data(form=form))
