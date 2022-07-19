from django.contrib import admin
from .models import Weapon, Group, Fighter

class WeaponAdmin(admin.ModelAdmin):
    list_display = ('name',)

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name',)

class FighterAdmin(admin.ModelAdmin):
    list_display = ('name', 'weapon', 'group',)

# Register your models here.

admin.site.register(Weapon, WeaponAdmin)
admin.site.register(Group, GroupAdmin)

admin.site.register(Fighter, FighterAdmin)
