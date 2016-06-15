from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Operation(models.Model):
    user = models.ForeignKey(User)
    a = models.FloatField()
    b = models.FloatField()
    operator = models.CharField(max_length=1)
    result = models.FloatField()
