from django.http import FileResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from rest_framework.generics import ListAPIView
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

from game.forms import FormGame
from game.models import Game
from game.serializers import GameSerializer

class Home(LoginRequiredMixin, ListView):
    model = Game
    context_object_name = 'games'
    template_name = 'game/home.html'
    
class CreateGame(LoginRequiredMixin, CreateView):
    model = Game
    form_class = FormGame
    template_name = 'game/create_game.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Pega o usuário atual
        form.instance.owner = self.request.user
        return super().form_valid(form)

class EditGame(LoginRequiredMixin, UpdateView):
    model = Game
    form_class = FormGame
    template_name = 'game/edit_game.html'
    success_url = reverse_lazy('home')

class DeleteGame(LoginRequiredMixin, DeleteView):
    model = Game
    template_name = 'game/delete_game.html'
    success_url = reverse_lazy('home')    

class GameDetailView(LoginRequiredMixin, DetailView):
    model = Game
    template_name = 'game/game-view.html'
    context_object_name = 'game'


class GameImageGetter(View):
    def get(self, request, filename):
        try:
            game = Game.objects.get(image='game/images/{}'.format(filename))
            return FileResponse(game.image)
        except ObjectDoesNotExist:
            raise Http404('Foto não encontrada ou não autorizado')
        except Exception as e:
            raise e

# API que retorna todos os games
class GetAllGamesApi(ListAPIView):
    serializer_class = GameSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Game.objects.all()