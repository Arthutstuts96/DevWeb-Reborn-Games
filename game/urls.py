from django.urls import path
from game.views import *
from review.views import ReviewListView

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('criar/', CreateGame.as_view(), name="create-game"),
    path('editar/<int:pk>/', EditGame.as_view(), name="edit-game"),
    path('deletar/<int:pk>/', DeleteGame.as_view(), name="delete-game"),
    path('<int:pk>/', GameDetailView.as_view(), name='game-detail'),
    path('images/<str:filename>/', GameImageGetter.as_view(), name="game-image"),
]
