from decimal import Decimal
from django.utils.translation import gettext_lazy as _

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
	return getattr(boundfield.field, 'min_value', None)

def get_max(boundfield):
	return getattr(boundfield.field, 'max_value', None)

def get_step(boundfield):
	decimal_places = getattr(boundfield.field, 'decimal_places', None)
	if decimal_places is not None:
		return str(Decimal(1).scaleb(-decimal_places)).lower()
	else:
		return 'any'

def get_minlength(boundfield):
	return getattr(boundfield.field, 'min_length', None)

def get_maxlength(boundfield):
	return getattr(boundfield.field, 'max_length', None)

def make_options(choices, value):
	if not isinstance(value, (tuple, list)):
		value = [value]
	value = [str(v) if v is not None else '' for v in value]
	print(list(choices), value)
	return [{'value': str(choice[0]), 'label': choice[1], 'selected': str(choice[0]) in value} for choice in choices]

def get_options(boundfield):
	choices = getattr(boundfield.field, 'choices', [])
	value = boundfield.value()
	return make_options(choices, value)

def get_optgroups(boundfield):
	choices = getattr(boundfield.field, 'choices', [])
	value = boundfield.value()
	if choices and isinstance(choices[0][1], (list, tuple)):
		return {choice[0]: make_options(choice[1], value) for choice in choices}
	else:
		return {}

def get_null_boolean_options(boundfield):
	options = [
		(None, _('Unknown')),
		(True, _('Yes')),
		(False, _('No')),
	]
	return make_options(options, [boundfield.value()])

def to_iso(boundfield):
	value = boundfield.value() or ''
	print('to_iso', value)
	if isinstance(value, str):
		return value
	else:
		return value.isoformat()
