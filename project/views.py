from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def login_register_view(request):
    login_form = AuthenticationForm(request)
    register_form = UserCreationForm()

    return render(request, 'login.html', {
        'form': login_form,
        'register_form': register_form,
    })
