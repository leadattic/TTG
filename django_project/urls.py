"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from . import views, api


urlpatterns = [
    # Under main service
    path('', views.home),
    path('hatlista/', views.hatlista),
    path('api/', views.api_docs),
    path('styles/get_style/', views.get_style),
    path('faq/', views.faq), 
    path('styles/', views.styles),
    path('styles/is_style/', views.is_style),

    # Under games service
    path('games/', views.games),

    # Under api service
    path('api/v1/', views.api),


    # Not under any service
    path('dashboard/', views.dashboard),
]
