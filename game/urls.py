from django.urls import path
from game.views import *

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('criar/', CreateGame.as_view(), name="create-game"),
]
