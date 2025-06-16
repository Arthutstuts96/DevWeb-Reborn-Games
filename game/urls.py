from django.urls import path

from game.views import Home

urlpatterns = [
    path('', Home.as_view(), name="home"),
]
