from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import MallFloorView

app_name = "api"

urlpatterns = [
	
]

urlpatterns = format_suffix_patterns(urlpatterns)