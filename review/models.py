from django.db import models

from game.models import Game

class Review(models.Model):
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    reviewer = models.CharField(max_length=100)
    content = models.TextField()
    stars = models.SmallIntegerField()
    likes = models.IntegerField()   
    create_date = models.DateTimeField(auto_now_add=True)
