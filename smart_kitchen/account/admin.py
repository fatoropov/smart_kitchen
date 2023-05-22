from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'date_of_birth',
                    'photo',
                    'dorm_number',
                    'room_number']
    raw_id_fields = ['user']
