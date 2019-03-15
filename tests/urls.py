from django.urls import path
from views import TestFormView

urlpatterns = [
	path('', TestFormView.as_view(), name='default'),
	path('required', TestFormView.as_view(), {'required': True}, name='required'),
	path('disabled', TestFormView.as_view(), {'disabled': False}, name='disabled'),
	path('with_errors', TestFormView.as_view(), {'with_errors': True}, name='with_errors'),
]
