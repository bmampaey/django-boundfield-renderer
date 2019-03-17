from django import forms
from django.template.loader import get_template
from ..registry import RendererRegistry

renderer_registry = RendererRegistry()

# Use the field.html template render method as the renderer function
field_template = get_template('default/field.html')

# Register all Django built-in form fields
renderer_registry.register(
	forms.BooleanField,
	forms.CharField,
	forms.ChoiceField,
	forms.TypedChoiceField,
	forms.DateField,
	forms.DateTimeField,
	forms.DecimalField,
	forms.DurationField,
	forms.EmailField,
	forms.FileField,
	forms.FilePathField,
	forms.FloatField,
	forms.ImageField,
	forms.IntegerField,
	forms.GenericIPAddressField,
	forms.MultipleChoiceField,
	forms.TypedMultipleChoiceField,
	forms.NullBooleanField,
	forms.RegexField,
	forms.SlugField,
	forms.TimeField,
	forms.URLField,
	forms.UUIDField,
	forms.ComboField,
	forms.SplitDateTimeField,
	forms.ModelChoiceField,
	forms.ModelMultipleChoiceField,
	renderer = field_template.render
)
