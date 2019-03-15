from django import template
from django.conf import settings

register = template.Library()

@register.filter(name = 'render')
def render(boundfield, registry = None):
	'''Render a form boundfield to html using the formrender library'''
	
	# Get the registry
	if registry is None:
		registry = settings.registry
	
	# TODO check how to import the registry from string
	if isinstance(registry, str):
		raise NotImplementedError('string with the path to the registry')
	
	# Get the approriate renderer
	renderer, context_modifier = registry[boundfield.field]
	
	# Create the context dict
	context = {
		'form': boundfield.form,
		'boundfield': boundfield,
		'widgets': boundfield.subwidgets,
		'name': boundfield.html_name,
		'value': boundfield.value(),
		'label': boundfield.label,
		'id': boundfield.id_for_label,
		'help_text': boundfield.help_text,
		'errors': boundfield.errors,
		'disabled': boundfield.field.disabled,
		'is_hidden': boundfield.is_hidden,
		'required': boundfield.field.required,
	}
	
	return renderer.render(context_modifier(context))
