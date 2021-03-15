from django.db import models
class timer(models.Model):
    start = models.TimeField()
    stop = models.TimeField()
    total＿time = models.IntegerField()
