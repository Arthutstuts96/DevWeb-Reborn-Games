from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from review.models import Review

class ReviewListView(ListView):
    model = Review
    context_object_name = 'reviews'
    template_name = 'partials/_reviews.html'
    paginate_by = 10

    def get_queryset(self):
        id = self.kwargs['game_pk']
        queryset = Review.objects.filter(game_id=id).order_by('-create_date')
        return queryset
    
# class CreateReview(CreateView):
#     model = Review
#     form_class = FormGame
#     template_name = 'game/create_game.html'
#     success_url = reverse_lazy('home')

# class EditReview(UpdateView):
#     model = Review
#     form_class = FormGame
#     template_name = 'game/edit_game.html'
#     success_url = reverse_lazy('home')

# class DeleteReview(DeleteView):
#     model = Review
#     template_name = 'game/delete_game.html'
#     success_url = reverse_lazy('home')    
