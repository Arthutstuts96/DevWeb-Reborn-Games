from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

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
