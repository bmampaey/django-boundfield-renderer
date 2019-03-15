
class FormRendererRegistry:
	'''
	Registry for the form renderers.
	
	A renderer is a function that takes a context dict and returns the html
	representation of the form field, for example the render method of a
	Template instance.
	
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
	
	def __init__(self, **kwargs):
		self.registry = dict()
		self.registry.update(kwargs)
	
	def register(self, *args, renderer = None):
		'''
		A Form Field class decorator. Can be passed the renderer method explicitly
		as a key word argument. Usage examples:
		'''
		
		if args:
			for form_field_class in args:
				self.registerer(renderer)(form_field_class)
		else:
			return self.registerer(renderer)
	
	def registerer(self, renderer = None):
		def _register(form_field_class):
			if renderer is None:
				self.registry[form_field_class] = getattr(form_field_class, 'render')
			else:
				self.registry[form_field_class] = renderer
			return form_field_class
		return _register


renderer_registry = FormFieldRendererRegistry()

input_template = template.Template('''
<div class="form-group">
	<label for="{{ id }}" {% if required %}class="required"{% endif %}>{{ label }}</label>
	<input type="{{ widget.input_type }}" name="{{ name }}" value="{{ value|default_if_none:'' }}" id="{{ id }}" class="form-control{% if css_classes %} {{css_classes}}{% endif %}{% if errors %} is-invalid{% endif %}"{% if required %} required{% endif %}{% if disabled %} disabled{% endif %}>{% if help_text %}
	<small class="form-text">{{ help_text }}</small>{% endif %}{% if errors %}
	<ul class="invalid-feedback list-unstyled">
		{% for error in errors %}
		<li>{{ error }}</li>
		{% endfor %}
	</ul>{% endif %}
</div>
''')

# TODO register all Django built-in form fields
#renderer_registry.register(forms.CharField, forms.EmailField, renderer = input_template.render)
