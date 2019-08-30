from django.contrib.sites.models import Site
from django.db import models


class Store(models.Model):
   name = models.CharField(max_length=255)
   site = models.OneToOneField(Site, related_name="store", on_delete=models.CASCADE, null=True)

   def __str__(self):
       return self.name


class Product(models.Model):
   store = models.ForeignKey(Store, on_delete=models.CASCADE)
   title = models.CharField(max_length=255)
   description = models.TextField(blank=True, null=True)

   def __str__(self):
       return self.title