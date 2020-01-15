from django.contrib import admin
from .models import (User, Entry)

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'last_updated']

class EntryAdmin(admin.ModelAdmin):
    field = '__all__'

admin.site.register(User, UserAdmin)
admin.site.register(Entry, EntryAdmin)