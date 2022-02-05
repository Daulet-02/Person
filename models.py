from django.db import models


# Create your models here.
class Person(models.Model):
    iin = models.CharField(max_length=12)
    age = models.IntegerField()

    def __str__(self):
      return self.iin



