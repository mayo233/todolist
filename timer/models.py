from django.db import models
class Timer(models.Model):
    time = models.TimeField()
    created_at = models.DateTimeField('作成日時')
