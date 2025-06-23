from django.db import models
from game.consts import *
from project import settings

class Game(models.Model):
    name = models.CharField(max_length=150, null=False)
    year = models.IntegerField()
    create_date = models.DateTimeField(auto_now_add=True)
    category = models.SmallIntegerField(choices=GAME_CATEGORIES)
    isUsed = models.BooleanField()
    image = models.ImageField(blank=True, upload_to='game/images')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)    
    price = models.FloatField()
    description = models.TextField(max_length=1000)
