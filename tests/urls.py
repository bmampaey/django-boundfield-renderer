from django.conf import settings
from django.urls import path, include
from views import DisplayFormView
from forms import BuiltinForm, CustomForm

def get_urls(view_class, **kwargs):
	return [
		path('', view_class.as_view(**kwargs), name='default'),
		path('required', view_class.as_view(**kwargs), {'required': True}, name='required'),
		path('disabled', view_class.as_view(**kwargs), {'disabled': True}, name='disabled'),
		path('with_errors', view_class.as_view(**kwargs), {'with_errors': True}, name='with_errors'),
		path('with_initial', view_class.as_view(**kwargs), {'with_initial': True}, name='with_initial'),
	]

urlpatterns = [
	path('default/display/', include((get_urls(DisplayFormView, form_class = BuiltinForm, template_name = 'default/display_form.html'),'default_display'))),
	path('default/compare/', include((get_urls(DisplayFormView, form_class = BuiltinForm, template_name = 'default/compare_form.html'),'default_compare'))),
	path('custom/display/', include((get_urls(DisplayFormView, form_class = CustomForm, template_name = 'default/display_form.html'),'custom_display'))),
	path('custom/compare/', include((get_urls(DisplayFormView, form_class = CustomForm, template_name = 'default/compare_form.html'),'custom_compare'))),
	path('bootstrap4/display/', include((get_urls(DisplayFormView, form_class = BuiltinForm, template_name = 'bootstrap4/display_form.html'),'bootstrap4_display'))),
	path('bootstrap4/compare/', include((get_urls(DisplayFormView, form_class = BuiltinForm, template_name = 'bootstrap4/compare_form.html'),'bootstrap4_compare'))),
]

if settings.DEBUG:
	import debug_toolbar
	urlpatterns = [
		path('__debug__/', include(debug_toolbar.urls)),
	] + urlpatterns
