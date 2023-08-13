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
    path('', views.home),
    path('games/', views.games),
    path('hatlista/', views.hatlista),
    path('api/', views.api_docs),
    path('api/v1/', views.api),
    path('styles/get_style/', views.home_style),
    path('styles/home/', views.home_style),
    path('dashboard/', views.dashboard),
    path('js/', views.js), # No longer in use
    
]
