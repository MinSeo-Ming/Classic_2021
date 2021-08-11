"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

app_name ="clothes"
urlpatterns = [
    path('clothes_upload/',views.clothing_upload,name="clothes_upload"),
    # path('clothes_index/',views.clothes_index,name="clothes_index"),
    path('clothes_detail/<int:clothes_id>/',views.clothes_detail,name="clothes_detail"),
    path('clothes_update/<int:clothes_id>/',views.clothing_update,name="clothing_update"),
    path('clothes_delete/<int:clothes_id>/',views.clothing_delete,name="clothing_delete"),
    path('mypage/',views.getMyclothes,name='myclothes'),
]
