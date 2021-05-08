from django.db import models

# Create your models here.
class Quote(models.Model):
    name = models.CharField(max_length=100, default=None)
    quote = models.CharField(max_length=300, default=None)
    author = models.CharField(max_length=100, default=None)
    email = models.CharField(max_length=100, default=None)

    #this is for deplaying text as a object name in admin panel
    def __str__(self):
        return self.quote