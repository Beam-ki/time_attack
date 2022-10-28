from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.
class Articles(models.Model):
    # author=models.ForeignKey(,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    content=models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.title)