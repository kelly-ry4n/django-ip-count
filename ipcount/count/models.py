from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Visitor(models.Model):

    ip = models.CharField(max_length=255)
    count = models.IntegerField()
    last_visit = models.DateTimeField(null=True)
