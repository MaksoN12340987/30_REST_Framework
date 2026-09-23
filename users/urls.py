from django.urls import path

from .apps import UsersConfig
from .views import UsersAPI

app_name = UsersConfig.name

urlpatterns = [
    path("", UsersAPI.as_view(), name="api"),
]
