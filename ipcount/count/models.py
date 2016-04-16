from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Visitor(models.Model):

    ip = models.CharField(max_length=255)
    count = models.IntegerField()
    last_visit = models.DateTimeField(null=True)
    current_visit = models.DateTimeField(null=True)


    def update_to_now(self):

        self.last_visit = self.current_visit
        self.current_visit = timezone.now()

    
    def __unicode__(self):
        return "{} with {} visits last visited on {}".format(self.ip, self.count, self.current_visit)
