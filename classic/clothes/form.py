from django import forms
from django.db import models
from .models import Clothing


class UploadingFileForm(forms.ModelForm):
    class Meta :
        model = Clothing

        fields=['type','color','alias','month','length','image']
        
        labels = {
            'type':'옷 분류',
            'color':'색상',
            'alias' :'옷 종류' ,
            'month':'옷을 입는 달',
            'length':'길이',
            'image' :'이미지'
        }  
