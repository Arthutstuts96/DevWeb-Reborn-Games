from django.db import models
from game.consts import *

class Game(models.Model):
    name = models.CharField(max_length=150, null=False)
    year = models.IntegerField()
    create_date = models.DateTimeField()
    category = models.SmallIntegerField(choices=GAME_CATEGORIES)
    isUsed = models.BooleanField()
    image = models.ImageField(blank=True, upload_to='game/images')
    owner = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField(max_length=1000)
