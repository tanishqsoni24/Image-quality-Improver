"""FieldProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from dataclasses import field
from django.contrib import admin
from django.urls import path
from . import field_content
from django.conf import settings #added thisss
from django.conf.urls.static import static #added this


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", field_content.main, name='index'),
    path("noise_remover",field_content.index, name='index'),
    path("mexican_hat",field_content.index, name='index'),
    path("sharpener",field_content.index, name='index'),
    path("result", field_content.results, name='result'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)