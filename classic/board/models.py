from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    content = models.CharField(max_length=200)
    #외래키로 작성자 id

    def __str__(self):
        return str(self.title) + " : " + str(self.content)
