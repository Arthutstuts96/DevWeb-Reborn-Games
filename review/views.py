from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from game.models import Game
from review.forms import FormReview
from review.models import Review

class ReviewListView(LoginRequiredMixin, ListView):
    model = Review
    context_object_name = 'reviews'
    template_name = 'partials/_reviews.html'
    paginate_by = 10

    def get_queryset(self):
        id = self.kwargs['game_pk']
        queryset = Review.objects.filter(game_id=id).order_by('-create_date')
        return queryset
    
class CreateReview(LoginRequiredMixin, CreateView):
    model = Review
    form_class = FormReview
    template_name = 'review/create-review.html'

    def get_context_data(self, **kwargs):
        # Adiciona o ID do jogo para a página colocar no formulário
        context = super().get_context_data(**kwargs)
        game_pk = self.kwargs['game_pk']
        context['game'] = get_object_or_404(Game, pk=game_pk)

        return context

    def form_valid(self, form):
        game_obj = get_object_or_404(Game, pk=self.kwargs['game_pk'])
        form.instance.game_id = game_obj
        # Pega o usuário atual
        form.instance.reviewer = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('game-detail', kwargs={'pk': self.kwargs['game_pk']})

# class EditReview(LoginRequiredMixin, UpdateView):
#     model = Review
#     form_class = FormGame
#     template_name = 'game/edit_game.html'
#     success_url = reverse_lazy('home')

# class DeleteReview(LoginRequiredMixin, DeleteView):
#     model = Review
#     template_name = 'game/delete_game.html'
#     success_url = reverse_lazy('home')    
