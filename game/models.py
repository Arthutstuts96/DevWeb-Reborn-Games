from django.db import models
from game.consts import *

class Game(models.Model):
    name = models.CharField(max_length=150, null=False)
    year = models.IntegerField()
    create_date = models.DateTimeField()
    category = models.SmallIntegerField(choices=GAME_CATEGORIES)
    isUsed = models.BooleanField()
    image = models.ImageField(null=True, upload_to='game/images')
