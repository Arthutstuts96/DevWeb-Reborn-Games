from django.urls import reverse_lazy
from django.contrib.auth import login
from django.views.generic import CreateView

from user.forms import UserForm
from user.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)

        return response