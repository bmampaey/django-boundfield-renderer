def update_context(values):
	'''
	A utility fonction that can be passed as the context_modifier function with a dict as parameter to update the context.
	Example:
	@registry.register(renderer=my_renderer, context_modifier=update_context({'style': 'color: red;'}))
	class MyField(forms.Field):
		pass
	
	The context dict that will be passed to my_renderer will have an item 'style': 'color: red;'
	'''
	def context_updater(context):
		context.update(values)
		return context
	return context_updater
