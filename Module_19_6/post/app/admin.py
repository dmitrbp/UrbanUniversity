from django.contrib import admin
from .models import *

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'post_date', 'post_creator')
    list_filter = ('post_date', 'post_creator')

@admin.register(Topic)
class PostAdmin(admin.ModelAdmin):
    list_display = ('topic_title', 'topic_desc')

@admin.register(SubTopic)
class PostAdmin(admin.ModelAdmin):
    list_display = ('stopic_title',)
