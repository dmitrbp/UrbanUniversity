from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=6, decimal_places=2)
    age = models.IntegerField()

class Game(models.Model):
    title = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField()
    age_limit = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')
