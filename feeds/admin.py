from django.contrib import admin
from .models import Source, Board, Article


class SourceAdmin(admin.ModelAdmin):
    list_display = ('name', )


class BoardAdmin(admin.ModelAdmin):
    list_display = ('name', 'source')


class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'topic',
        'author',
        'url',
        'source',
        'board',
        'publish_time'
    )

admin.site.register(Source, SourceAdmin)
admin.site.register(Board, BoardAdmin)
admin.site.register(Article, ArticleAdmin)
