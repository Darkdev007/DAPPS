from django.contrib import admin
from .models import Crypto

class CryptoAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Crypto,CryptoAdmin)