from django.db import models
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=500)
    # deadline = models.DurationField(default=timezone.timedelta(days=1))
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)