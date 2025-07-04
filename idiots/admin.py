from django.contrib import admin
from idiots.models import Idiots


@admin.register(Idiots)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ('password', )
