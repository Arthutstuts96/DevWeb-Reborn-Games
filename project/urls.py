from django.contrib import admin
from django.urls import include, path
from project.views import *

urlpatterns = [
    path('', Login.as_view(), name="login"),
    path('admin/', admin.site.urls),
    path('game/', include('game.urls'), name="game")
]
