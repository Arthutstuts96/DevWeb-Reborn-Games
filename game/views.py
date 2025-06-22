from django.http import FileResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from game.forms import FormGame
from game.models import Game

class Home(ListView):
    model = Game
    context_object_name = 'games'
    template_name = 'game/home.html'
    
class CreateGame(CreateView):
    model = Game
    form_class = FormGame
    template_name = 'game/create_game.html'
    success_url = reverse_lazy('home')

class EditGame(UpdateView):
    model = Game
    form_class = FormGame
    template_name = 'game/edit_game.html'
    success_url = reverse_lazy('home')

class DeleteGame(DeleteView):
    model = Game
    template_name = 'game/delete_game.html'
    success_url = reverse_lazy('home')    

class GameDetailView(DetailView):
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
