from django.db import models
from calculator.apes import Ransom
import random


# Create your models here.
class CalcGET(models.Model):
    x = models.FloatField(blank=True)
    y = models.FloatField(blank=True)
    operations = models.CharField(max_length=1, blank=True)
    result = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return random.choice(Ransom)