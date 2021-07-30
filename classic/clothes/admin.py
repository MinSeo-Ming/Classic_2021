from django.contrib import admin
from .models import Clothes_Main_type, Clothing, Color

admin.site.register(Clothing)
admin.site.register(Color)
admin.site.register(Clothes_Main_type)