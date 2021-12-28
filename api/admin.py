from django.contrib import admin
from api.models import Category, Post

class Category(admin.ModelAdmin):
    list_display = ['id', 'category']
    list_display_links = ['id', 'category']
    search_fields = ['category']
    ordering = ['category']

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title_post', 'autor_post', 'image_post', 'publicated', 'created_at', 'updated_at']
    list_editable = ('publicated',)
    list_display_links = ['id', 'title_post']

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)