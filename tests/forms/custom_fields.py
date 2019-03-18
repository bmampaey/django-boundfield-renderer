from django import forms
from django.template.loader import get_template
from django.core.exceptions import ValidationError
from boundfield_renderer.registries import default
from boundfield_renderer.utils import update_context

class MyCharField(forms.CharField):
	'''CharField that does not register a renderer but add some extra validation'''
	def clean(self, value):
		if value == 'Spanish Inquisition':
			raise ValidationError('I was not expecting the Spanish Inquisition!')
		else:
			return super().clean(value)

@default.register(renderer = get_template('custom/my_other_char_field.html').render)
class MyOtherCharField(forms.CharField):
	'''CharField that does register a renderer'''
	pass

@default.register(renderer = get_template('custom/my_field.html').render)
class MyField(forms.Field):
	'''A custom field with a custom renderer'''
	pass


@default.register(renderer = get_template('custom/my_field.html').render, context_modifier = update_context({'css_classes': 'bowtie'}))
class MySuperField(MyField):
	'''Just like MyField but with some extra class'''
	pass
