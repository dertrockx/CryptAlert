# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Coin
from django.contrib import admin

# Register your models here.
class CoinAdmin(admin.ModelAdmin):
    list_display = ['coin_id', 'name', 'symbol']

admin.site.register(Coin, CoinAdmin)
    
