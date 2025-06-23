from django.forms import ModelForm
from game.models import Game

class FormGame(ModelForm):
    class Meta:
        model = Game
        exclude = ['owner']