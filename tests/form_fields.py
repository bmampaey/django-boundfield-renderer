from django import forms
from django.template.loader import get_template
from django.core.exceptions import ValidationError
from formrenderer.registries import default
from formrenderer.utils import update_context

class MyCharField(forms.CharField):
	'''CharField that does not register a renderer'''
	def clean(self, value):
		if value == 'Spanish Inquisition':
			raise ValidationError('I was not expecting the Spanish Inquisition!')
		else:
			return super().clean(value)


@default.register(renderer = get_template('default/my_field.html').render)
class MyField(forms.Field):
	'''A field that for which I have defined a custom renderer'''
	pass


@default.register(renderer = get_template('default/my_field.html').render, context_modifier = update_context({'css_classes': 'bowtie'}))
class MySuperField(MyField):
	'''Just like MyField but with some extra class'''
	pass
