from django.conf import settings
from django.urls import path, include
from views import CompareFormView

urlpatterns = [
	path('', CompareFormView.as_view(), name='default'),
	path('required', CompareFormView.as_view(), {'required': True}, name='required'),
	path('disabled', CompareFormView.as_view(), {'disabled': True}, name='disabled'),
	path('with_errors', CompareFormView.as_view(), {'with_errors': True}, name='with_errors'),
	path('with_initial', CompareFormView.as_view(), {'with_initial': True}, name='with_initial'),
]

if settings.DEBUG:
	import debug_toolbar
	urlpatterns = [
		path('__debug__/', include(debug_toolbar.urls)),
	] + urlpatterns
