from django.contrib import admin
from django.urls import include, path
from project.views import *

urlpatterns = [
    path('', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
    path('admin/', admin.site.urls),
    path('game/', include('game.urls'), name="game"),
    path('game/<int:game_pk>/reviews/', include('review.urls'), name='review'),
]
