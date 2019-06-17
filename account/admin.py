from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']
    list_filter = ()
    search_fields = ()


admin.site.register(Profile, ProfileAdmin)

