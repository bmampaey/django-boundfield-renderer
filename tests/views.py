from django.views.generic import FormView
from forms import BuiltinForm

class CompareFormView(FormView):
	form_class = BuiltinForm
	template_name = 'builtin/compare_form.html'
	
	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		for option in ('required', 'disabled', 'with_errors', 'with_initial'):
			if option in self.kwargs:
				kwargs[option] = self.kwargs[option]
		return kwargs
	
	def form_valid(self, form):
		return self.render_to_response(self.get_context_data(form=form))
