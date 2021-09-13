from django.contrib import admin

from users.models import UserProfileModel


@admin.register(UserProfileModel)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone']
    search_fields = ['first_name', 'last_name', 'email', 'phone']
