from django.contrib.auth.models import User
from django.db import models

# Create your models here.

"""
    This contains the users BLOB (vault)
"""
class UserSite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blob = models.CharField(max_length=4096)

