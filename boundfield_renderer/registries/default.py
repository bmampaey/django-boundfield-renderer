from django import forms
from django.template.loader import get_template
from ..registry import RendererRegistry

# Use the field.html template render method as the renderer function
field_template = get_template('default/field.html')

# Create the registry with all Django built-in form fields
renderer_registry = RendererRegistry({
	forms.BooleanField: (field_template.render, None),
	forms.CharField: (field_template.render, None),
	forms.ChoiceField: (field_template.render, None),
	forms.TypedChoiceField: (field_template.render, None),
	forms.DateField: (field_template.render, None),
	forms.DateTimeField: (field_template.render, None),
	forms.DecimalField: (field_template.render, None),
	forms.DurationField: (field_template.render, None),
	forms.EmailField: (field_template.render, None),
	forms.FileField: (field_template.render, None),
	forms.FilePathField: (field_template.render, None),
	forms.FloatField: (field_template.render, None),
	forms.ImageField: (field_template.render, None),
	forms.IntegerField: (field_template.render, None),
	forms.GenericIPAddressField: (field_template.render, None),
	forms.MultipleChoiceField: (field_template.render, None),
	forms.TypedMultipleChoiceField: (field_template.render, None),
	forms.NullBooleanField: (field_template.render, None),
	forms.RegexField: (field_template.render, None),
	forms.SlugField: (field_template.render, None),
	forms.TimeField: (field_template.render, None),
	forms.URLField: (field_template.render, None),
	forms.UUIDField: (field_template.render, None),
	forms.ComboField: (field_template.render, None),
	forms.SplitDateTimeField: (field_template.render, None),
	forms.ModelChoiceField: (field_template.render, None),
	forms.ModelMultipleChoiceField: (field_template.render, None),
})
