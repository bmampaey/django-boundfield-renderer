import inspect

class RendererRegistry:
	'''
	Registry for the form field renderers.
	
	A renderer is a function that takes a context dict and returns the html
	representation of the form field, for example the render method of a
	Template instance.
	
	'''
	
	def __init__(self, **kwargs):
		self.registry = dict()
		self.registry.update(kwargs)
	
	def __getitem__(self, key):
		'''Return the best renderer function for the field'''
		
		# The registry needs the form field class, not an instance
		if not inspect.isclass(key):
			key = type(key)
		
		# Look up the chain of inheritance for a registered renderer
		for form_class in inspect.getmro(key):
			try:
				return self.registry[form_class]
			except KeyError:
				pass
		
		# If no renderer was found raise an Exception
		raise ValueError('No renderer found for field %s' % key)
	
	def register(self, *args, renderer, context_modifier = None):
		'''
		Register a form field class into the registry.
		The renderer and context_modifier functions must be passed as keyword arguments.
		
		Can be called directly like so:
		renderer_registry.register(forms.CharField, forms.IntegerField, ... , renderer=my_renderer, context_modifier=my_context_modifier)
		
		Or as a decorator like so:
		renderer_registry.register(renderer=my_renderer, context_modifier=my_context_modifier)
		class MyField(forms.Field):
			pass
		'''
		
		if args: # register is called directly
			for form_field_class in args:
				self.registry[form_field_class] = renderer, context_modifier
		else: # register is called as a decorator
			return self._register(renderer, context_modifier)
		
	def _register(self, renderer, context_modifier):
		def registerer(form_field_class):
			self.registry[form_field_class] = renderer, context_modifier
			return form_field_class
		return registerer
