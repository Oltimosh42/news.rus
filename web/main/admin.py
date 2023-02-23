from django.contrib import admin
from .models import *


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_add', 'cat')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')
    list_filter = ('time_add', 'cat')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Category, CategoryAdmin)
