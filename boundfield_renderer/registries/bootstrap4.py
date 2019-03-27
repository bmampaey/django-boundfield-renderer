from django import forms
from ..registry import RendererRegistry
from ..utils import template_renderer, get_min, get_max, get_step, get_minlength, get_maxlength, get_options, get_optgroups, get_null_boolean_options, to_iso

# Create the registry with all Django built-in form fields
renderer_registry = RendererRegistry({
	forms.BooleanField: template_renderer('bootstrap4/fields/boolean_field.html', input_type='checkbox'),
	forms.CharField: template_renderer('bootstrap4/fields/char_field.html', input_type='text', min_length=get_minlength, max_length=get_maxlength),
	forms.ChoiceField: template_renderer('bootstrap4/fields/choice_field.html', options=get_options, optgroups=get_optgroups),
	forms.TypedChoiceField: template_renderer('bootstrap4/fields/typed_choice_field.html', options=get_options, optgroups=get_optgroups),
	forms.DateField: template_renderer('bootstrap4/fields/date_field.html', input_type='date', min=get_min, max=get_max, value=to_iso),
	forms.DateTimeField: template_renderer('bootstrap4/fields/date_time_field.html', input_type='datetime-local', min=get_min, max=get_max, value=to_iso),
	forms.DecimalField: template_renderer('bootstrap4/fields/decimal_field.html', input_type='number', min=get_min, max=get_max, step=get_step),
	forms.DurationField: template_renderer('bootstrap4/fields/duration_field.html', input_type='text'),
	forms.EmailField: template_renderer('bootstrap4/fields/email_field.html', input_type='email'),
	forms.FileField: template_renderer('bootstrap4/fields/file_field.html', input_type='file'),
	forms.FilePathField: template_renderer('bootstrap4/fields/file_path_field.html', options=get_options),
	forms.FloatField: template_renderer('bootstrap4/fields/float_field.html', input_type='number', min=get_min, max=get_max, step='any'),
	forms.ImageField: template_renderer('bootstrap4/fields/image_field.html', input_type='file', accept='image/*'),
	forms.IntegerField: template_renderer('bootstrap4/fields/integer_field.html', input_type='number', min=get_min, max=get_max, step='1'),
	forms.GenericIPAddressField: template_renderer('bootstrap4/fields/generic_ip_address_field.html', input_type='text'),
	forms.MultipleChoiceField: template_renderer('bootstrap4/fields/multiple_choice_field.html', options=get_options, optgroups=get_optgroups, multiple=True),
	forms.TypedMultipleChoiceField: template_renderer('bootstrap4/fields/typed_multiple_choice_field.html', options=get_options, optgroups=get_optgroups, multiple=True),
	forms.NullBooleanField: template_renderer('bootstrap4/fields/null_boolean_field.html', options=get_null_boolean_options),
	forms.RegexField: template_renderer('bootstrap4/fields/regex_field.html', input_type='text'),
	forms.SlugField: template_renderer('bootstrap4/fields/slug_field.html', input_type='text'),
	forms.TimeField: template_renderer('bootstrap4/fields/time_field.html', input_type='time', min=get_min, max=get_max, value=to_iso),
	forms.URLField: template_renderer('bootstrap4/fields/url_field.html', input_type='url'),
	forms.UUIDField: template_renderer('bootstrap4/fields/uuid_field.html', input_type='text'),
	forms.ComboField: template_renderer('bootstrap4/fields/combo_field.html', input_type='text'),
	forms.SplitDateTimeField: template_renderer('bootstrap4/fields/split_date_time_field.html'),
	forms.ModelChoiceField: template_renderer('bootstrap4/fields/model_choice_field.html', options=get_options),
	forms.ModelMultipleChoiceField: template_renderer('bootstrap4/fields/model_multiple_choice_field.html', options=get_options, multiple=True),
})
