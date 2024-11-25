from datetime import datetime
from django.db import models

class Blog(models.Model):
    pass

class Post(models.Model):
    post_title = models.CharField(max_length=255, verbose_name='Название статьи')
    post_date = models.DateTimeField(default=datetime.now(), verbose_name='Дата создания')
    post_creator = models.CharField(max_length=100, default='guest', verbose_name='Создатель')
    post_content = models.TextField(verbose_name='Содержание статьи')
    def __str__(self):
        return self.post_title
