from django.db import models
class timer(models.Model):
    start = models.IntegerField()
    stop = models.IntegerField()
    time = models.IntegerField()
