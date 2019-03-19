from django import forms
from .custom_fields import MyCharField, MyOtherCharField, MyField, MySuperField

class CharFieldForm(forms.Form):
	'''Form to test the rendering of default CharField'''
	charfield = forms.CharField()

class MyCharFieldForm(forms.Form):
	'''Form to test the rendering of MyCharField'''
	mycharfield = MyCharField(initial='Spanish Inquisition')

class MyOtherCharFieldForm(forms.Form):
	'''Form to test the rendering of MyOtherCharField'''
	myothercharfield = MyOtherCharField(initial='Spanish Inquisition')
	
class MyFieldForm(forms.Form):
	'''Form to test the rendering of MyField'''
	myfield = MyField()
	
class MySuperFieldForm(forms.Form):
	'''Form to test the rendering of MySuperField'''
	mysuperfield = MySuperField()

class CustomForm(forms.Form):
	charfield = forms.CharField()
	mycharfield = MyCharField(initial='Spanish Inquisition')
	myothercharfield = MyOtherCharField(initial='Spanish Inquisition')
	myfield = MyField()
	mysuperfield = MySuperField()
