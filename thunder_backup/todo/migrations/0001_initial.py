# Generated by Django 3.1.7 on 2021-03-15 10:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='タイトル')),
                ('text', models.TextField(max_length=500, verbose_name='タスク')),
                ('deadline', models.DateTimeField(default=datetime.timedelta(days=1), verbose_name='期限')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日')),
            ],
        ),
    ]
