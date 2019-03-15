import importlib
from django import template
from django.conf import settings

register = template.Library()

@register.filter(name = 'render')
def render(boundfield, registry = None):
	'''
	Render a boundfield to html using the specified renderer registry
	
	The context dict contains the following key/values:
		form: The form the field belongs to
		boundfield: The bound field itself
		widgets: The widget instances of the field
		name: The name HTML attribute for the field
		value: The current value of the field
		label: The label of the field
		id: The id for the label of the field
		help_text: The help_text of the field
		errors: The list of Validation errors for the field
		disabled: True if the field is disabled
		is_hidden: True if the field is hidden
		required: True if the field is required
	'''
	
	# Get the registry
	if registry is None:
		registry = settings.FORM_RENDERER_DEFAULT_REGISTRY
	
	# If the registry is a path, resolve it
	if isinstance(registry, str):
		try:
			module_name, registry_name = registry.rsplit('.', 1)
			module = importlib.import_module(module_name)
			registry = getattr(module, methoregistry_named_name)
		except Exception as why:
			raise ValueError('Could not find registry "%s"', registry) from why
	
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
	
	return renderer(context_modifier(context))
