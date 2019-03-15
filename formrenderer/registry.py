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
		A Form Field class decorator. Must be passed the renderer method explicitly
		as a key word argument. Usage examples:
		'''
		
		for form_field_class in args:
			self.registerer(renderer)(form_field_class)
	
	def registerer(self, renderer = None):
		def _register(form_field_class):
			self.registry[form_field_class] = renderer
			return form_field_class
		return _register
