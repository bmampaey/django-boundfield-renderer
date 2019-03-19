from django import forms
from django.template.loader import get_template
from ..registry import RendererRegistry
from ..utils import update_context, get_min, get_max, get_step, get_minlength, get_maxlength, get_options, get_optgroups, get_options_multiple, get_optgroups_multiple, get_null_boolean_options

renderer_registry = RendererRegistry()

# Use the field.html template render method as the renderer function
field_template = get_template('default/field.html')

# Register all Django built-in form fields
renderer_registry.register(forms.BooleanField, renderer=get_template('bootstrap4/fields/boolean_field.html').render, context_modifier = update_context(input_type='checkbox'))
renderer_registry.register(forms.CharField, renderer=get_template('bootstrap4/fields/char_field.html').render, context_modifier = update_context(input_type='text', min_length=get_minlength, max_length=get_maxlength))
renderer_registry.register(forms.ChoiceField, renderer=get_template('bootstrap4/fields/choice_field.html').render, context_modifier = update_context(options=get_options, optgroups=get_optgroups))
renderer_registry.register(forms.TypedChoiceField, renderer=get_template('bootstrap4/fields/typed_choice_field.html').render, context_modifier = update_context(options=get_options, optgroups=get_optgroups))
renderer_registry.register(forms.DateField, renderer=get_template('bootstrap4/fields/date_field.html').render, context_modifier = update_context(input_type='date', min=get_min, max=get_max))
renderer_registry.register(forms.DateTimeField, renderer=get_template('bootstrap4/fields/date_time_field.html').render, context_modifier = update_context(input_type='datetime-local', min=get_min, max=get_max))
renderer_registry.register(forms.DecimalField, renderer=get_template('bootstrap4/fields/decimal_field.html').render, context_modifier = update_context(input_type='number', min=get_min, max=get_max, step=get_step))
renderer_registry.register(forms.DurationField, renderer=get_template('bootstrap4/fields/duration_field.html').render, context_modifier = update_context(input_type='text'))
renderer_registry.register(forms.EmailField, renderer=get_template('bootstrap4/fields/email_field.html').render, context_modifier = update_context(input_type='email'))
renderer_registry.register(forms.FileField, renderer=get_template('bootstrap4/fields/file_field.html').render, context_modifier = update_context(input_type='file'))
renderer_registry.register(forms.FilePathField, renderer=get_template('bootstrap4/fields/file_path_field.html').render, context_modifier = update_context(options=get_options))
renderer_registry.register(forms.FloatField, renderer=get_template('bootstrap4/fields/float_field.html').render, context_modifier = update_context(input_type='number', min=get_min, max=get_max, step='any'))
renderer_registry.register(forms.ImageField, renderer=get_template('bootstrap4/fields/image_field.html').render, context_modifier = update_context(input_type='file', accept='image/*'))
renderer_registry.register(forms.IntegerField, renderer=get_template('bootstrap4/fields/integer_field.html').render, context_modifier = update_context(input_type='number', min=get_min, max=get_max, step='1'))
renderer_registry.register(forms.GenericIPAddressField, renderer=get_template('bootstrap4/fields/generic_ip_address_field.html').render, context_modifier = update_context(input_type='text'))
renderer_registry.register(forms.MultipleChoiceField, renderer=get_template('bootstrap4/fields/multiple_choice_field.html').render, context_modifier = update_context(options=get_options_multiple, optgroups=get_optgroups_multiple, multiple=True))
renderer_registry.register(forms.TypedMultipleChoiceField, renderer=get_template('bootstrap4/fields/typed_multiple_choice_field.html').render, context_modifier = update_context(options=get_options_multiple, optgroups=get_optgroups_multiple, multiple=True))
renderer_registry.register(forms.NullBooleanField, renderer=get_template('bootstrap4/fields/null_boolean_field.html').render, context_modifier = update_context(options=get_null_boolean_options))
renderer_registry.register(forms.RegexField, renderer=get_template('bootstrap4/fields/regex_field.html').render, context_modifier = update_context(input_type='text'))
renderer_registry.register(forms.SlugField, renderer=get_template('bootstrap4/fields/slug_field.html').render, context_modifier = update_context(input_type='text'))
renderer_registry.register(forms.TimeField, renderer=get_template('bootstrap4/fields/time_field.html').render, context_modifier = update_context(input_type='time', min=get_min, max=get_max))
renderer_registry.register(forms.URLField, renderer=get_template('bootstrap4/fields/url_field.html').render, context_modifier = update_context(input_type='url'))
renderer_registry.register(forms.UUIDField, renderer=get_template('bootstrap4/fields/uuid_field.html').render, context_modifier = update_context(input_type='text'))
renderer_registry.register(forms.ComboField, renderer=get_template('bootstrap4/fields/combo_field.html').render, context_modifier = update_context(input_type='text'))
renderer_registry.register(forms.SplitDateTimeField, renderer=get_template('bootstrap4/fields/split_date_time_field.html').render)
renderer_registry.register(forms.ModelChoiceField, renderer=get_template('bootstrap4/fields/model_choice_field.html').render, context_modifier = update_context(options=get_options))
renderer_registry.register(forms.ModelMultipleChoiceField, renderer=get_template('bootstrap4/fields/model_multiple_choice_field.html').render, context_modifier = update_context(options=get_options_multiple, multiple=True))
