from django.conf.urls import url
from django.urls import path
from oauth2_provider import views as oauth2_views

from .views import UserRegister


urlpatterns = [
    path('register', views.UserRegister.as_view())
]