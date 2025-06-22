from django.urls import path
from game.views import *

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('criar/', CreateGame.as_view(), name="create-game"),
    path('editar/<int:pk>/', EditGame.as_view(), name="edit-game"),
    path('deletar/<int:pk>/', DeleteGame.as_view(), name="delete-game"),
]
