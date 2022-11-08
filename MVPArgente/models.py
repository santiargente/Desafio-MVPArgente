from django.db import models

class Parientes(models.Model):

    nombre = models.CharField(max_length=40)
    parentezco = models.CharField(max_length=40)
    edad = models.IntegerField()

