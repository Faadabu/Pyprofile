from django.db import models

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)