from django.contrib import admin

from .models import Profile, UserDinnerware, UserProducts


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "date_of_birth",
        "photo",
        "dorm_number",
        "room_number",
    ]
    raw_id_fields = ["user"]


@admin.register(UserProducts)
class UserProductsAdmin(admin.ModelAdmin):
    list_display = [
        "user_id",
        "product_id",
        "quantity",
    ]
    raw_id_fields = ["user_id"]


@admin.register(UserDinnerware)
class UserDinnerwareAdmin(admin.ModelAdmin):
    list_display = [
        "user_id",
        "dinnerware_id",
        "quantity",
    ]
    raw_id_fields = ["user_id"]
