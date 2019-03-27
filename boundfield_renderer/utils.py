from decimal import Decimal
from django.template.loader import get_template
from django.utils.translation import gettext_lazy as _

def template_renderer(template_name, **kwargs):
	'''
	A utility fonction that return a renderer function that renders a template by passing it the context.
	Optional keywords can be specified to be added to the context before rendering the template.
	If the value of the keyword is callable, it will be called with the boundfield as parameter.
	Examples:
	template_renderer('path/to/my_template.html', color = 'red')
	This will add the item ('color': 'red') to the context before rendering the template
	
	template_renderer('path/to/my_template.html', color = lambda b: 'red' if b.value() < 0 else 'blue')
	This will add the item ('color': 'red') to the context if the value of the boundfield is negative,
	else it will add the the item ('color': 'blue') before rendering the template.
	'''
	def render_template(context):
		template = get_template(template_name)
		boundfield = context['boundfield']
		for key, value in kwargs.items():
			if callable(value):
				context[key] = value(boundfield)
			else:
				context[key] = value
		return template.render(context)
	return render_template

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
	return [{'value': str(choice[0]), 'label': choice[1], 'selected': str(choice[0]) in value} for choice in choices]

def get_options(boundfield):
	choices = getattr(boundfield.field, 'choices', [])
	value = boundfield.value()
	return make_options(choices, value)

def get_optgroups(boundfield):
	choices = getattr(boundfield.field, 'choices', [])
	value = boundfield.value()
	if choices and isinstance(choices[0][1], (list, tuple)):
		return [{'label': choice[0], 'options': make_options(choice[1], value)} for choice in choices]
	else:
		return {}

def get_null_boolean_options(boundfield):
	choices = [
		(None, _('Unknown')),
		(True, _('Yes')),
		(False, _('No')),
	]
	value = boundfield.value()
	return make_options(choices, value)

def to_iso(boundfield):
	value = boundfield.value() or ''
	if isinstance(value, str):
		return value
	else:
		return value.isoformat()
