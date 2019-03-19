from django import forms
from django.template.loader import get_template
from ..registry import RendererRegistry
from ..utils import update_context

renderer_registry = RendererRegistry()

# Use the field.html template render method as the renderer function
field_template = get_template('default/field.html')

# Register all Django built-in form fields
renderer_registry.register(forms.BooleanField, renderer = get_template('bootstrap4/boolean_field.html').render)
renderer_registry.register(forms.CharField, renderer = get_template('bootstrap4/char_field.html').render)
renderer_registry.register(forms.ChoiceField, renderer = get_template('bootstrap4/choice_field.html').render)
renderer_registry.register(forms.TypedChoiceField, renderer = get_template('bootstrap4/typed_choice_field.html').render)
renderer_registry.register(forms.DateField, renderer = get_template('bootstrap4/date_field.html').render)
renderer_registry.register(forms.DateTimeField, renderer = get_template('bootstrap4/date_time_field.html').render)
renderer_registry.register(forms.DecimalField, renderer = get_template('bootstrap4/decimal_field.html').render)
renderer_registry.register(forms.DurationField, renderer = get_template('bootstrap4/duration_field.html').render)
renderer_registry.register(forms.EmailField, renderer = get_template('bootstrap4/email_field.html').render)
renderer_registry.register(forms.FileField, renderer = get_template('bootstrap4/file_field.html').render)
renderer_registry.register(forms.FilePathField, renderer = get_template('bootstrap4/file_path_field.html').render)
renderer_registry.register(forms.FloatField, renderer = get_template('bootstrap4/float_field.html').render)
renderer_registry.register(forms.ImageField, renderer = get_template('bootstrap4/image_field.html').render)
renderer_registry.register(forms.IntegerField, renderer = get_template('bootstrap4/integer_field.html').render)
renderer_registry.register(forms.GenericIPAddressField, renderer = get_template('bootstrap4/generic_ip_address_field.html').render)
renderer_registry.register(forms.MultipleChoiceField, renderer = get_template('bootstrap4/multiple_choice_field.html').render)
renderer_registry.register(forms.TypedMultipleChoiceField, renderer = get_template('bootstrap4/typed_multiple_choice_field.html').render)
renderer_registry.register(forms.NullBooleanField, renderer = get_template('bootstrap4/null_boolean_field.html').render)
renderer_registry.register(forms.RegexField, renderer = get_template('bootstrap4/regex_field.html').render)
renderer_registry.register(forms.SlugField, renderer = get_template('bootstrap4/slug_field.html').render)
renderer_registry.register(forms.TimeField, renderer = get_template('bootstrap4/time_field.html').render)
renderer_registry.register(forms.URLField, renderer = get_template('bootstrap4/url_field.html').render)
renderer_registry.register(forms.UUIDField, renderer = get_template('bootstrap4/uuid_field.html').render)
renderer_registry.register(forms.ComboField, renderer = get_template('bootstrap4/combo_field.html').render)
renderer_registry.register(forms.SplitDateTimeField, renderer = get_template('bootstrap4/split_date_time_field.html').render)
renderer_registry.register(forms.ModelChoiceField, renderer = get_template('bootstrap4/model_choice_field.html').render)
renderer_registry.register(forms.ModelMultipleChoiceField, renderer = get_template('bootstrap4/model_multiple_choice_field.html').render)
