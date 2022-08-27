from django.db import models

# Create your models here.

class Animals(models.Model):

    GENDER = ((1, 'Hembra', ), (2, 'Macho'))

    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=20, choices=GENDER)
    raza = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    class Meta:
        db_table = 'animals'