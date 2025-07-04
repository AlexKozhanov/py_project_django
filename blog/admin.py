from django.contrib import admin
from blog.models import Blog


@admin.register(Blog)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'png', 'creation_date', 'publication')
    list_filter = ('title',)
    search_fields = ('title',)
