from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Cloth(models.Model):
    type = models.CharField(max_length=50)
    color = models.CharField(max_length=15)
    alias = models.CharField(max_length=10) # 별명 혹은 이름
    create_date = models.DateTimeField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.alias