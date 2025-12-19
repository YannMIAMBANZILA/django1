from django.contrib import admin
from django.utils.html import format_html

from . import models

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'user', 'published_at')
    list_filter = ('status', 'created_at', 'published_at', 'user')
    search_fields = ('title', 'content')
    list_per_page = 20
    list_editable = ('status',)

admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Category)
admin.site.register(models.Tag)

def display_thumb(self, obj):
    if obj.thumb:
        return format_html('<img src="{}" width="50" height="50" />', obj.thumb.url)
    return "None"

## display_thumb.short_description = 'Thumbnail'