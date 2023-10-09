from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'email', 'phone']
    list_display_links = ['firstname', 'lastname']
    list_filter = ['firstname', 'lastname']


admin.site.register(User, UserAdmin)