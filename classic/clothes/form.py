from django import forms
from django.db import models
from .models import Clothing


class UploadingFileForm(forms.ModelForm):
    class Meta :
        model = Clothing

        fields=['type','color','alias','image']
        widgets = {
        }
        labels = {
            'type':'옷 분류',
            'color':'색상',
            'alias' :'옷 종류' ,
            'image' :'이미지'
        }  
