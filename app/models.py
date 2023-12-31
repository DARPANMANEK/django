import json
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_organizer = models.BooleanField('Is organizer', default=False)
    is_participant = models.BooleanField('Is participant', default=False)
    event = models.CharField(max_length=50, default="")