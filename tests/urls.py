from django.conf import settings
from django.urls import path, include
from django.views.generic import TemplateView
from views import DisplayFormView
from forms import BuiltinForm, CustomForm

def get_urls(view_class, form_classes, **kwargs):
	return ([
		path('default', view_class.as_view(**kwargs), {'form_classes': form_classes}, name='default'),
		path('required', view_class.as_view(**kwargs), {'form_classes': form_classes, 'required': True}, name='required'),
		path('disabled', view_class.as_view(**kwargs), {'form_classes': form_classes, 'disabled': True}, name='disabled'),
		path('with_errors', view_class.as_view(**kwargs), {'form_classes': form_classes, 'with_errors': True}, name='with_errors'),
		path('with_initial', view_class.as_view(**kwargs), {'form_classes': form_classes, 'with_initial': True}, name='with_initial'),
	], 'test')

urlpatterns = [
	path('', TemplateView.as_view(template_name = 'index.html'), name = 'index'),
	path('default/display/', include(get_urls(DisplayFormView, form_classes = {'form': BuiltinForm}, template_name = 'default/display_form.html'), namespace='default_display')),
	path('default/compare/', include(get_urls(DisplayFormView, form_classes = {'form1': BuiltinForm, 'form2': BuiltinForm}, template_name = 'default/compare_form.html'), namespace='default_compare')),
	path('custom/display/', include(get_urls(DisplayFormView, form_classes = {'form': CustomForm}, template_name = 'default/display_form.html'), namespace='custom_display')),
	path('custom/compare/', include(get_urls(DisplayFormView, form_classes = {'form1': CustomForm, 'form2': CustomForm}, template_name = 'default/compare_form.html'), namespace='custom_compare')),
	path('bootstrap4/display/', include(get_urls(DisplayFormView, form_classes = {'form': BuiltinForm}, template_name = 'bootstrap4/display_form.html'), namespace='bootstrap4_display')),
	path('bootstrap4/compare/', include(get_urls(DisplayFormView, form_classes = {'form1': BuiltinForm, 'form2': BuiltinForm}, template_name = 'bootstrap4/compare_form.html'), namespace='bootstrap4_compare')),
]

if settings.DEBUG:
	import debug_toolbar
	urlpatterns = [
		path('__debug__/', include(debug_toolbar.urls)),
	] + urlpatterns
