from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'alt', 'slug', 'status')
    prepopulated_fields = {'slug': ('title',), }


admin.site.register(Category)
