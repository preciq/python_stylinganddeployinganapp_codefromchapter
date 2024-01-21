"""
URL configuration for ll_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # default paths are already defined, i.e. the admin path

    path('', include('learning_logs.urls')),
    # this allows paths defined in the urls.py module in learning_logs (which needs to be created) to be used here
    # allows learning_logs app urls to be accessed from /, the base path (so http://127.0.0.1:8000/ onwards)
    
    path('accounts/', include('accounts.urls')),
    # allows accounts app urls to be accessed from accounts/ (so http://127.0.0.1:8000/accounts/ onwards)
]


