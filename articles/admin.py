from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'price')
    list_display_links = ('name',)
    search_fields = ('name', 'description')
    list_per_page = 25

admin.site.register(Article, ArticleAdmin)
