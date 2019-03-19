from decimal import Decimal

def update_context(**kwargs):
	'''
	A utility fonction that can be passed as the context_modifier function to update the context.
	Example:
	@registry.register(renderer=my_renderer, context_modifier=update_context(style = 'color: red;'))
	class MyField(forms.Field):
		pass
	
	The context dict that will be passed to my_renderer will have an item ('style', 'color: red;')
	'''
	def context_updater(context):
		boundfield = context['boundfield']
		for key, value in kwargs.items():
			if callable(value):
				context[key] = value(boundfield)
			else:
				context[key] = value
		return context
	return context_updater

def get_min(boundfield):
	return getattr(boundfield, 'min_value', None)

def get_max(boundfield):
	return getattr(boundfield, 'max_value', None)

def get_step(boundfield):
	decimal_places = getattr(boundfield, 'decimal_places', None)
	if decimal_places:
		return str(Decimal(1).scaleb(-self.decimal_places)).lower()
	else:
		return 'any'

def get_minlength(boundfield):
	return getattr(boundfield, 'min_length', None)

def get_maxlength(boundfield):
	return getattr(boundfield, 'max_length', None)

def make_options(choices, values):
	print(choices, values)
	return [{'value': str(choice[0]), 'label': choice[1], 'selected': choice[0] in values} for choice in choices]

def get_options(boundfield):
	choices = getattr(boundfield.field, 'choices', [])
	values = [boundfield.value()] if boundfield.value() is not None else []
	return make_options(choices, values)

def get_optgroups(boundfield):
	choices = getattr(boundfield.field, 'choices', [])
	values = [boundfield.value()] if boundfield.value() is not None else []
	if choices and isinstance(choices[0][1], (list, tuple)):
		return {choice[0]: make_options(choice[1], values) for choice in choices}
	else:
		return {}

def get_options_multiple(boundfield):
	choices = getattr(boundfield.field, 'choices', [])
	values = boundfield.value() if boundfield.value() is not None else []
	return make_options(choices, values)

def get_optgroups_multiple(boundfield):
	choices = getattr(boundfield.field, 'choices', [])
	values = boundfield.value() if boundfield.value() is not None else []
	if choices and isinstance(choices[0][1], (list, tuple)):
		return {choice[0]: make_options(choice[1], values) for choice in choices}
	else:
		return {}

def get_null_boolean_options(boundfield):
	values = [boundfield.value()] if boundfield.value() is not None else []
	return make_options([('unknown', 'Unknown'), ('true', 'Yes'), ('false', 'No')], values)
