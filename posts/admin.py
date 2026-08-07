from django.contrib import admin
from .models import Post, Media

class MediaInline(admin.TabularInline):
    model = Media
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'category', 'post_type', 'created_at', 'likes_count']
    list_filter = ['post_type', 'category', 'created_at']
    search_fields = ['title', 'content']
    inlines = [MediaInline]
    readonly_fields = ['likes_count', 'comments_count', 'created_at', 'updated_at']

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ['post', 'media_type', 'file', 'order']
    list_filter = ['media_type']



