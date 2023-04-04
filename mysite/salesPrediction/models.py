from django.db import models

# Create your models here.

class Sales(models.Model):
    model = models.CharField(max_length=500)
    month = models.CharField(max_length=500)
    sales = models.IntegerField()
    color = models.CharField(max_length=500)
    region = models.TextField(max_length=500)
    date = models.CharField(max_length=500)

class Predictions(models.Model):
    model = models.CharField(max_length=500)
    color = models.CharField(max_length=500)
    region=  models.CharField(max_length=500)
    month = models.CharField(max_length=500)
    prediction= models.IntegerField()