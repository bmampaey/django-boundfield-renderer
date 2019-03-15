from django import forms
from django.contrib.auth.models import User

class TestForm(forms.Form):
	'''Form to test the rendering of all fields types'''
	boolean = forms.BooleanField()
	char = forms.CharField(min_length=3, max_length=5)
	choice = forms.ChoiceField(choices=[('1', 'tomato'), ('2', 'apple')])
	typedchoice = forms.TypedChoiceField(choices=[('1', 'tomato'), ('2', 'apple')], coerce=int, empty_value = None)
	date = forms.DateField()
	datetime = forms.DateTimeField()
	decimal = forms.DecimalField(min_value=0, max_value=99, max_digits=5, decimal_places=3)
	duration = forms.DurationField()
	email = forms.EmailField(min_length=5, max_length=50)
	file = forms.FileField(max_length=100)
	filepath = forms.FilePathField(path='/tmp')
	float = forms.FloatField()
	image = forms.ImageField()
	integer = forms.IntegerField(min_value=0, max_value=100)
	genericipaddress = forms.GenericIPAddressField()
	multiplechoice = forms.MultipleChoiceField(choices=[('1', 'tomato'), ('2', 'apple')])
	typedmultiplechoice = forms.TypedMultipleChoiceField(choices=[('1', 'tomato'), ('2', 'apple')], coerce=int, empty_value = None)
	nullboolean = forms.NullBooleanField()
	regex = forms.RegexField(regex=r'\w+')
	slug = forms.SlugField()
	time = forms.TimeField()
	url = forms.URLField(min_length=3, max_length=100)
	uuid = forms.UUIDField()
	combo = forms.ComboField(fields=[forms.CharField(max_length=20), forms.EmailField()])
	splitdatetime = forms.SplitDateTimeField()
	modelchoice = forms.ModelChoiceField(queryset=User.objects.all())
	modelmultiplechoice = forms.ModelMultipleChoiceField(queryset=User.objects.all())
	hidden = forms.CharField(widget=forms.HiddenInput)
	textarea = forms.CharField(widget=forms.Textarea)
	radio = forms.ChoiceField(choices=[('1', 'tomato'), ('2', 'apple')], widget=forms.RadioSelect)
	helptext = forms.CharField(help_text = 'Some help text')
	initial = forms.CharField(initial = 'Some initial value')
	label = forms.CharField(label = 'Some specific label')
	
	def __init__(self, *args, required = False, disabled = False, with_errors = False, **kwargs):
		super().__init__(*args, **kwargs)
		
		self.with_errors = with_errors
		
		for field in self.fields.values():
			field.required = required
			field.diabled = disabled
	
	def clean(self):
		cleaned_data = super().clean()
		if self.with_errors:
			self.add_error(None, 'Form error #1')
			self.add_error(None, 'Form error #2')
			for name, field in self.fields.items():
				self.add_error(name, name + ' error #1')
				self.add_error(name, name + ' error #2')
		return cleaned_data
