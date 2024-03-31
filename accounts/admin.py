from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')
    list_display_link = ('id', 'username')

admin.site.register(CustomUser, CustomUserAdmin)