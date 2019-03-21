from datetime import date, datetime, timedelta
from django import forms
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.contenttypes.models import ContentType

class BuiltinForm(forms.Form):
	'''Form to test the rendering of all built-in fields types'''
	boolean_field = forms.BooleanField()
	char_field = forms.CharField(min_length=3, max_length=5)
	choice_field = forms.ChoiceField(choices=[('1', 'tomato'), ('2', 'apple'), ('3', 'cherry')])
	typedchoice_field = forms.TypedChoiceField(choices=[(1, 'tomato'), (2, 'apple'), (3, 'cherry')], coerce=int, empty_value = None)
	date_field = forms.DateField()
	datetime_field = forms.DateTimeField()
	decimal_field = forms.DecimalField(min_value=0, max_value=99, max_digits=5, decimal_places=3)
	duration_field = forms.DurationField()
	email_field = forms.EmailField(min_length=5, max_length=50)
	file_field = forms.FileField(max_length=100)
	filepath_field = forms.FilePathField(path='/tmp')
	float_field = forms.FloatField()
	image_field = forms.ImageField()
	integer_field = forms.IntegerField(min_value=0, max_value=100)
	genericipaddress_field = forms.GenericIPAddressField()
	multiplechoice_field = forms.MultipleChoiceField(choices=[('1', 'tomato'), ('2', 'apple'), ('3', 'cherry')])
	typedmultiplechoice_field = forms.TypedMultipleChoiceField(choices=[(1, 'tomato'), (2, 'apple'), (3, 'cherry')], coerce=int, empty_value = None)
	nullboolean_field = forms.NullBooleanField()
	regex_field = forms.RegexField(regex=r'\w+')
	slug_field = forms.SlugField()
	time_field = forms.TimeField()
	url_field = forms.URLField(min_length=3, max_length=100)
	uuid_field = forms.UUIDField()
	combo_field = forms.ComboField(fields=[forms.CharField(max_length=20), forms.EmailField()])
	splitdatetime_field = forms.SplitDateTimeField()
	modelchoice_field = forms.ModelChoiceField(queryset=ContentType.objects.all())
	modelmultiplechoice_field = forms.ModelMultipleChoiceField(queryset=ContentType.objects.all())
	hidden = forms.CharField(widget=forms.HiddenInput)
	textarea = forms.CharField(widget=forms.Textarea)
	password = forms.CharField(widget=forms.PasswordInput)
	radio = forms.ChoiceField(choices=[('1', 'tomato'), ('2', 'apple'), ('3', 'cherry')], widget=forms.RadioSelect)
	helptext = forms.CharField(help_text = 'Some help text')
	initial = forms.CharField(initial = 'Some initial value')
	label = forms.CharField(label = 'Some specific label')
	
	def __init__(self, *args, required = False, disabled = False, with_errors = False, with_initial = False, **kwargs):
		super().__init__(*args, **kwargs)
		
		self.with_errors = with_errors
		
		for field in self.fields.values():
			field.required = required
			field.disabled = disabled
		
		if with_initial:
			class FakeFile:
				url = 'http://www.test.com'
				def __str__(self):
					return self.url
			
			self.initial.update({
				'boolean_field': True,
				'char_field': 'test',
				'choice_field': '2',
				'typedchoice_field': 2,
				'date_field': date.today(),
				'datetime_field': datetime.now(),
				'decimal_field': 0.1,
				'duration_field': timedelta(1),
				'email_field': 'test@test.com',
				'file_field': FakeFile(),
				'filepath_field': '/tmp',
				'float_field': 0.1,
				'image_field': FakeFile(),
				'integer_field': 0,
				'genericipaddress_field': '127.0.0.1',
				'multiplechoice_field': ['1', '2'],
				'typedmultiplechoice_field': [1, 2],
				'nullboolean_field': False,
				'regex_field': 'test',
				'slug_field': 'test',
				'time_field': datetime.now().time(),
				'url_field': 'http://127.0.0.1',
				'uuid_field': '12345678123456781234567812345678',
				'combo_field': 'test@test.com',
				'splitdatetime_field': datetime.now(),
				'modelchoice_field': ContentType.objects.all()[2],
				'modelmultiplechoice_field': ContentType.objects.all()[:2],
				'hidden': 'test',
				'textarea': 'multiline\ntest',
				'password': 'password',
				'radio': '3',
				'helptext': 'test',
				'initial': 'Some OTHER initial value',
				'label': 'test',
			})
	
	def clean(self):
		cleaned_data = super().clean()
		if self.with_errors:
			self.add_error(None, 'Form error #1')
			self.add_error(None, 'Form error #2')
			for name, field in self.fields.items():
				self.add_error(name, name + ' error #1')
				self.add_error(name, name + ' error #2')
		return cleaned_data
