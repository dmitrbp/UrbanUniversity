from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'post_date', 'post_creator')
    list_filter = ('post_date', 'post_creator')
