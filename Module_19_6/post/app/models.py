from datetime import datetime
from django.db import models

class Post(models.Model):
    post_title = models.CharField(max_length=255, verbose_name='Название статьи')
    post_date = models.DateTimeField(default=datetime.now(), verbose_name='Дата создания')
    post_creator = models.CharField(max_length=100, default='guest', verbose_name='Создатель')
    post_content = models.TextField(verbose_name='Содержание статьи')
    def __str__(self):
        return self.post_title

class Topic(models.Model):
    topic_title = models.CharField(max_length=100, verbose_name='Название темы')
    topic_desc = models.CharField(max_length=255, verbose_name='Описание темы')
    def __str__(self):
        return self.topic_title

class SubTopic(models.Model):
    stopic_title = models.CharField(max_length=100, verbose_name='Название темы')
    def __str__(self):
        return self.stopic_title