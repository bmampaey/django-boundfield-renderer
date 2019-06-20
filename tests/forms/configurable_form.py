from django import forms

class ConfigurableForm(forms.Form):
	'''A base form that allows to configure easily all the fields'''
	
	def __init__(self, *args, required = False, disabled = False, with_errors = False, with_initial = False, **kwargs):
		super().__init__(*args, **kwargs)
		
		self.with_errors = with_errors
		
		for field in self.fields.values():
			field.required = required
			field.disabled = disabled
		
		if with_initial:
			self.initial.update(self.get_initial())
	
	def get_initial(self):
		'''Return initial values for the form'''
		return {}
	
	def clean(self):
		cleaned_data = super().clean()
		# Add errors to the form and the fields
		if self.with_errors:
			self.add_error(None, 'Form error #1')
			self.add_error(None, 'Form error #2')
			for name, field in self.fields.items():
				self.add_error(name, name + ' error #1')
				self.add_error(name, name + ' error #2')
		
		return cleaned_data
