# from django.db import models
from djongo import models
from django.urls import reverse


class Quote(models.Model):
    _id = models.ObjectIdField(default=None)
    quote = models.TextField(max_length=1000, default=None)
    author = models.CharField(max_length=200, default=None)

    # this is for deplaying text as a object name in admin panel

    def __str__(self):
        return self.quote
