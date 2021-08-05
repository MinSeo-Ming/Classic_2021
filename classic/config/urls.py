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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', include('board.urls')),
    path('clothes/', include('clothes.urls')),
    path('common/', include('common.urls')),
    path('',filter,name='home')
    #path('',views.~View.as_view(),name='home')    #추후에 메인 화면 html과 연동
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
