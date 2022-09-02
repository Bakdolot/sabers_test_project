from django.contrib import admin

from .models import Article, ArticleGallery


class ArticleGalleryInline(admin.StackedInline):
    model = ArticleGallery
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    inlines = [ArticleGalleryInline]
    list_display = ("id", "title", "created_at")
    search_fields = ("title",)


admin.site.register(Article, ArticleAdmin)
