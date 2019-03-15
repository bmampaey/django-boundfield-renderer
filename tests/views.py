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
	
	def form_valid(self, form):
		return self.render_to_response(self.get_context_data(form=form))
