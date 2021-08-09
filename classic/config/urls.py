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
from django.urls import path, include
from django.conf import settings

from django.conf.urls.static import static
from clothes.views import filter

# from mysite.views import HomeView
from board.views import base_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', include('board.urls')),
    path('clothes/', include('clothes.urls')),
    path('common/', include('common.urls')),
    path('index', base_views.index, name='index'), # 보드랑 옷 보이는걸 수정
    path('',filter,name='home')
   
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

