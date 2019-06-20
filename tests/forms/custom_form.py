from django import forms
from .custom_fields import MyCharField, MyOtherCharField, MyField, MySuperField

from .configurable_form import ConfigurableForm

class CharFieldForm(ConfigurableForm):
	'''Form to test the rendering of default CharField'''
	charfield = forms.CharField()

class MyCharFieldForm(ConfigurableForm):
	'''Form to test the rendering of MyCharField'''
	mycharfield = MyCharField(initial='Spanish Inquisition')

class MyOtherCharFieldForm(ConfigurableForm):
	'''Form to test the rendering of MyOtherCharField'''
	myothercharfield = MyOtherCharField(initial='Spanish Inquisition')
	
class MyFieldForm(ConfigurableForm):
	'''Form to test the rendering of MyField'''
	myfield = MyField()
	
class MySuperFieldForm(ConfigurableForm):
	'''Form to test the rendering of MySuperField'''
	mysuperfield = MySuperField()

class CustomForm(ConfigurableForm):
	charfield = forms.CharField()
	mycharfield = MyCharField(initial='Spanish Inquisition')
	myothercharfield = MyOtherCharField(initial='Spanish Inquisition')
	myfield = MyField()
	mysuperfield = MySuperField()
