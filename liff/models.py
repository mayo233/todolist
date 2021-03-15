from django.db import models

# Create your models here.
class LinePush(models.Model):
    """Lineでのプッシュ先を表す"""
    user_id = models.CharField('ユーザーID', max_length=100, unique=True)

    def __str__(self):
        return self.user_id