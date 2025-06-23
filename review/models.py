from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from game.models import Game
from project import settings

class Review(models.Model):
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    content = models.TextField() 
    create_date = models.DateTimeField(auto_now_add=True)
    stars = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    likes = models.IntegerField(default=0, validators=[MinValueValidator(0)])