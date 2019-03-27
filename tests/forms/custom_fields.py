from django import forms
from django.core.exceptions import ValidationError
from boundfield_renderer.registries import default
from boundfield_renderer.utils import template_renderer

class MyCharField(forms.CharField):
	'''CharField that does not register a renderer but add some extra validation'''
	def clean(self, value):
		if value == 'Spanish Inquisition':
			raise ValidationError('I was not expecting the Spanish Inquisition!')
		else:
			return super().clean(value)

@default.register(template_renderer('custom/my_other_char_field.html'))
class MyOtherCharField(forms.CharField):
	'''CharField that does register a renderer'''
	pass

@default.register(template_renderer('custom/my_field.html'))
class MyField(forms.Field):
	'''A custom field with a custom renderer'''
	pass


@default.register(template_renderer('custom/my_field.html', css_classes = 'bowtie'))
class MySuperField(MyField):
	'''Just like MyField but with some extra class'''
	pass
