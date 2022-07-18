from django.contrib import admin
from .models import Weapon

class BattlefrontAdmin(admin.ModelAdmin):
    list_display = ('name',)

# Register your models here.

admin.site.register(Weapon, BattlefrontAdmin)
