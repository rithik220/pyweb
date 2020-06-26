from django.db import models


class Offer(models.Model):
    code = models.CharField(max_length=15)
    description = models.CharField(max_length=150)
    discount = models.FloatField()


class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)

