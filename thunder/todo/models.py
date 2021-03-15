from django.db import models
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    title = models.CharField('タイトル', max_length=20)
    text = models.TextField('タスク', max_length=500)
    deadline = models.DateTimeField('期限', default=timezone.timedelta(days=1))
    created_at = models.DateTimeField('作成日', auto_now_add=True)
    updated_at = models.DateTimeField('更新日', auto_now=True)