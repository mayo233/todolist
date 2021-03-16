from django.db import models
from django.utils import timezone

# Create your models here.
class Chara(models.Model):
    title = models.CharField('キャラ名', max_length=20)
    text = models.CharField('経験値', max_length=20)
    