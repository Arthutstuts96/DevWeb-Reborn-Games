from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView

from project.views import *
from user.views import RegisterView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='login', permanent=False), name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', RegisterView.as_view(), name='register'),
    path('admin/', admin.site.urls),
    path('game/', include('game.urls'), name="game"),
    path('game/<int:game_pk>/reviews/', include('review.urls')),
]
