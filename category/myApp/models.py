from django.db import models

# Create your models here.
class Laptop(models.Model):
    model = models.IntegerField(primary_key=True)
    speed = models.FloatField(blank=True, null=True)
    ram = models.IntegerField(blank=True, null=True)
    hd = models.IntegerField(blank=True, null=True)
    screen = models.FloatField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Laptop'


class Pc(models.Model):
    model = models.IntegerField(primary_key=True)
    speed = models.FloatField(blank=True, null=True)
    ram = models.IntegerField(blank=True, null=True)
    hd = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PC'


class Printer(models.Model):
    model = models.IntegerField(primary_key=True)
    color = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Printer'


class Product(models.Model):
    maker = models.CharField(max_length=10, blank=True, null=True)
    model = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Product'
