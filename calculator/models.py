from django.db import models

# Create your models here.
class calc(models.Model):
    x = models.FloatField(blank=True)
    y = models.FloatField(blank=True)
    operations = models.CharField(max_length=1, blank=True)
    result = models.CharField(max_length=20, blank=True)