from django.db import models
from django.db.models.base import Model

# Create your models here.

class Month(models.Model):
    # id == month로 설정
    month = models.IntegerField()
    min_temp = models.FloatField()
    max_temp = models.FloatField()

class fine_Dust_ppm_10(models.Model):
    grade = models.CharField(max_length=20)
    min_ppm = models.IntegerField()
    max_ppm = models.IntegerField()

class fine_Dust_ppm_2_5(models.Model):
    grade = models.CharField(max_length=20)
    min_ppm = models.IntegerField()
    max_ppm = models.IntegerField()

class Weather(models.Model):
    season= models.CharField(max_length=4,blank=True,null=True) #계절
    month = models.ForeignKey(Month,on_delete=models.CASCADE,db_column='month')
    # ppm_10  = models.ForeignKey(fine_Dust_ppm_10,on_delete=models.CASCADE,db_column='ppm_10',default='',null=True,blank=True)  
    # ppm_2_5  = models.ForeignKey(fine_Dust_ppm_2_5,on_delete=models.CASCADE,db_column='ppm_2_5', default='',null=True,blank=True)

# 컨테인즈 관계로 설계를 해라...many to many -> 어쇼시에이션 클래스 하나가 새롭게
# DDD modeling = msa ->이쪽으로 생각해보기...

