from django.db import models

# Create your models here.

class Hero(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=254)
    # isSubscribed = models.Boolean