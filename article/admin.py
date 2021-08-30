from django.contrib import admin
from django.db import models
from .models import Article, Comment
# Register your models here.

admin.site.register(Comment)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ["title", "author", "created_data", "content"]
    list_display_links = ["title", "created_data"]  # link yozelliyi verir
    search_fields = ["title"]  # search yaradir
    list_filter = ["title"]

    class Meta:
        model = Article
