from django import template

register = template.Library()

@register.filter
def hidden_fields_errors(form):
	'''Return a dict with the form's hidden field errors'''
	errors = dict()
	
	for boundfield in form.hidden_fields():
		errors[boundfield.name] = boundfield.errors
	
	return errors
