from django.contrib import admin
from author.models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'tel', 'email')
    search_fields = ('name', 'age', 'tel', 'email')
    list_filter = ('name', 'email')
    fields = ('name', 'email', 'age', 'tel', 'address')
admin.site.register(User, UserAdmin)