from django.contrib import admin

from .models import Category, Dish, DishComposition, Menu


class DishCompositionInline(admin.TabularInline):
    model = DishComposition
    raw_id_fields = ["product"]


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "slug",
    ]
    prepopulated_fields = {
        "slug": ("name",),
    }


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "slug",
    ]
    prepopulated_fields = {
        "slug": ("name",),
    }


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "slug",
        "created",
        "updated",
    ]
    list_filter = [
        "created",
        "updated",
    ]
    prepopulated_fields = {
        "slug": ("name",),
    }
    inlines = [DishCompositionInline]
