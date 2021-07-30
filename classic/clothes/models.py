from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Clothes_Main_type(models.Model):
    type = models.CharField(max_length=15)

    def __str__(self):
        return self.type

class Color(models.Model):
    color = models.CharField(max_length=20)
    def __str__(self):
        return self.color


class Clothing(models.Model):
    
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    type = models.ForeignKey(Clothes_Main_type,on_delete=models.CASCADE)
    color = models.ForeignKey(Color,on_delete=models.CASCADE)
    alias = models.CharField(max_length=10) # 별명 혹은 이름
    create_date = models.DateTimeField()
    image = models.ImageField(upload_to="clothing/images") #그냥 파일명만 저장하고 static 파일 경로 static 에 업로드하게끔

    def __str__(self):
        return self.alias
