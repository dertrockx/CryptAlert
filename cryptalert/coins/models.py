# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.db import models

# Create your models here.



class CoinQuerySet(models.QuerySet):
    def serialize(self):
        qs = list(self.values('id', 'coin_id', 'name', 'symbol'))
        return json.dumps(qs)

class CoinManager(models.Manager):
    def get_queryset(self):
        return CoinQuerySet(self.model, using=self._db)

class Coin(models.Model):
	coin_id = models.CharField(max_length=50)
	name 	= models.CharField(max_length=100)
	symbol 	= models.CharField(max_length=50)

	objects = CoinManager()

	def __str__(self):
		return "{name} - {symbol}".format(name=self.name, symbol=self.symbol)

