from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Goods(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category)

    def __str__(self):
        return "{}-{}".format(self.category.name, self.name)
