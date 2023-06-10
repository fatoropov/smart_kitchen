from django.contrib import admin
from .models import CategoryDinnerware, Dinnerware


@admin.register(CategoryDinnerware)
class CategoryDinnerwaresAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Dinnerware)
class DinnerwareAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'available',
                    'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['available']
    prepopulated_fields = {'slug': ('name',)}
