from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.views import View

from project import settings

class Login(View): 
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/game')
        else:
            return render(request, 'login.html')
        
    def post(self, request):
        user = request.POST.get('username', None)
        password = request.POST.get('password', None)

        print(user, password)

        user = authenticate(request, username=user, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/game')
            else:
                return render(request, 'login.html', {'mensagem': 'Usuário está inativo'})
        else:
            return render(request, 'login.html', {'mensagem': 'Usuário ou senha inválidos'})
        
class Logout(View):
    def get(self, request):
        logout(request)
        return redirect(settings.LOGIN_URL)