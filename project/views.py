from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.views import View

class Login(View): 
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/game')
        else:
            return render(request, 'login.html')
        
    def post(self, request):
        True
        # user = request.POST.get('nome', None)
        # password = request.POST.get('senha', None)

        # print(usuario, senha)

        # user = authenticate(request, username=usuario, password=senha)
        # if user is not None:
        #     if user.is_active:
        #         login(request, user)
        #         return redirect('/veiculo')
        #     else:
        #         return render(request, 'autenticacao.html', {'mensagem': 'Usuário está inativo'})
        # else:
        #     return render(request, 'autenticacao.html', {'mensagem': 'Usuário ou senha inválidos'})