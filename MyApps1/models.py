from django.db import models
from django.urls import reverse
# Create your models here.
class Employee(models.Model):
    empno=models.IntegerField()
    ename=models.CharField(max_length=60)
    job=models.CharField(max_length=60)
    sal=models.FloatField()

    def __str__(self):
        return self.ename
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pkfrom})
