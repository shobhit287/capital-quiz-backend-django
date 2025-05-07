"""
URL configuration for city_quiz project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from . import views

URL_PREFIX = "api"
urlpatterns = [
    path(URL_PREFIX, views.server_status, name="server_status"),
    path(f"{URL_PREFIX}/random-country", views.Quiz.as_view(), name="random_country"),
    path(f"{URL_PREFIX}/get-capital", views.Quiz.as_view(), name="get_capital"),
]
