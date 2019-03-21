from django import forms
from django.template.loader import get_template
from ..registry import RendererRegistry
from ..utils import update_context, get_min, get_max, get_step, get_minlength, get_maxlength, get_options, get_optgroups, get_null_boolean_options, to_iso

# Create the registry with all Django built-in form fields
renderer_registry = RendererRegistry({
	forms.BooleanField: (get_template('bootstrap4/fields/boolean_field.html').render, update_context(input_type='checkbox')),
	forms.CharField: (get_template('bootstrap4/fields/char_field.html').render, update_context(input_type='text', min_length=get_minlength, max_length=get_maxlength)),
	forms.ChoiceField: (get_template('bootstrap4/fields/choice_field.html').render, update_context(options=get_options, optgroups=get_optgroups)),
	forms.TypedChoiceField: (get_template('bootstrap4/fields/typed_choice_field.html').render, update_context(options=get_options, optgroups=get_optgroups)),
	forms.DateField: (get_template('bootstrap4/fields/date_field.html').render, update_context(input_type='date', min=get_min, max=get_max, value=to_iso)),
	forms.DateTimeField: (get_template('bootstrap4/fields/date_time_field.html').render, update_context(input_type='datetime-local', min=get_min, max=get_max, value=to_iso)),
	forms.DecimalField: (get_template('bootstrap4/fields/decimal_field.html').render, update_context(input_type='number', min=get_min, max=get_max, step=get_step)),
	forms.DurationField: (get_template('bootstrap4/fields/duration_field.html').render, update_context(input_type='text')),
	forms.EmailField: (get_template('bootstrap4/fields/email_field.html').render, update_context(input_type='email')),
	forms.FileField: (get_template('bootstrap4/fields/file_field.html').render, update_context(input_type='file')),
	forms.FilePathField: (get_template('bootstrap4/fields/file_path_field.html').render, update_context(options=get_options)),
	forms.FloatField: (get_template('bootstrap4/fields/float_field.html').render, update_context(input_type='number', min=get_min, max=get_max, step='any')),
	forms.ImageField: (get_template('bootstrap4/fields/image_field.html').render, update_context(input_type='file', accept='image/*')),
	forms.IntegerField: (get_template('bootstrap4/fields/integer_field.html').render, update_context(input_type='number', min=get_min, max=get_max, step='1')),
	forms.GenericIPAddressField: (get_template('bootstrap4/fields/generic_ip_address_field.html').render, update_context(input_type='text')),
	forms.MultipleChoiceField: (get_template('bootstrap4/fields/multiple_choice_field.html').render, update_context(options=get_options, optgroups=get_optgroups, multiple=True)),
	forms.TypedMultipleChoiceField: (get_template('bootstrap4/fields/typed_multiple_choice_field.html').render, update_context(options=get_options, optgroups=get_optgroups, multiple=True)),
	forms.NullBooleanField: (get_template('bootstrap4/fields/null_boolean_field.html').render, update_context(options=get_null_boolean_options)),
	forms.RegexField: (get_template('bootstrap4/fields/regex_field.html').render, update_context(input_type='text')),
	forms.SlugField: (get_template('bootstrap4/fields/slug_field.html').render, update_context(input_type='text')),
	forms.TimeField: (get_template('bootstrap4/fields/time_field.html').render, update_context(input_type='time', min=get_min, max=get_max, value=to_iso)),
	forms.URLField: (get_template('bootstrap4/fields/url_field.html').render, update_context(input_type='url')),
	forms.UUIDField: (get_template('bootstrap4/fields/uuid_field.html').render, update_context(input_type='text')),
	forms.ComboField: (get_template('bootstrap4/fields/combo_field.html').render, update_context(input_type='text')),
	forms.SplitDateTimeField: (get_template('bootstrap4/fields/split_date_time_field.html').render, None),
	forms.ModelChoiceField: (get_template('bootstrap4/fields/model_choice_field.html').render, update_context(options=get_options)),
	forms.ModelMultipleChoiceField: (get_template('bootstrap4/fields/model_multiple_choice_field.html').render, update_context(options=get_options, multiple=True)),
})
