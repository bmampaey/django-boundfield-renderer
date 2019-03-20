from django.views.generic import TemplateView

class DisplayFormView(TemplateView):
	
	def get_form(self, form_class, **form_kwargs):
		''' Create and return a form with the proper kwargs'''
		# Add the args options
		for option in ('required', 'disabled', 'with_errors', 'with_initial'):
			form_kwargs[option] = option in self.kwargs
		# Add the data
		if self.request.method in ('POST', 'PUT'):
			form_kwargs.update({
				'data': self.request.POST,
				'files': self.request.FILES,
			})
		# If with errors we must pass data or else the errors will be empty
		elif self.kwargs.get('with_errors', False):
			form_kwargs['data'] = {}
		
		return form_class(**form_kwargs)
		
	def get_context_data(self, **kwargs):
		forms = {name: self.get_form(form_class, prefix=name) for name, form_class in self.kwargs['form_classes'].items()}
		return super().get_context_data(**forms, **kwargs)
	
	def post(self, request, *args, **kwargs):
		return self.get(request, *args, **kwargs)
