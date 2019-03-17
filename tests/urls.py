from django.conf import settings
from django.urls import path, include
from views import TestFormView

urlpatterns = [
	path('', TestFormView.as_view(), name='default'),
	path('required', TestFormView.as_view(), {'required': True}, name='required'),
	path('disabled', TestFormView.as_view(), {'disabled': False}, name='disabled'),
	path('with_errors', TestFormView.as_view(), {'with_errors': True}, name='with_errors'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
