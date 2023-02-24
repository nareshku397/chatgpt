from django.db import models

# Create your models here.
class Signup(models.Model):
  email = models.CharField(max_length=255)