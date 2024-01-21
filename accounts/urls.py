"""Defines URL patterns for accounts."""
from django.urls import path, include
from . import views

app_name = 'accounts'
urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),
    # note that the path specified here is http://127.0.0.1:8000/accounts/, as defined in ll_project, so anything we add in the empty string will come after this path
    # we also include the default django auth urls (i.e. login, logout) via django.contrib.auth.urls
    # these also appear to not be needed in views since they are implemented by default
    
    # Registration page.
    path('register/', views.register, name='register'),
    # registration page url path specified here
]

