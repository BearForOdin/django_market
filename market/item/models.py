from django.db import models

class Category(models.Model):
    names = models.CharField(max_length=255)