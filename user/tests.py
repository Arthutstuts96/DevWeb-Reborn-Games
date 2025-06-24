from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .forms import UserForm

User = get_user_model()

class RegisterViewTests(TestCase):
    def setUp(self):
        self.url = reverse('register')

    def test_get_request_renders_register_page(self):
        """Testa se a página de registro é carregada corretamente com um GET."""
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')
        self.assertIsInstance(response.context.get('form'), UserForm)

    def test_successful_registration_and_login(self):
        """
        Testa se um usuário se registra com sucesso,
        é salvo no banco e logado automaticamente.
        """
        user_data = {
            'username': 'novousuario',
            'password1': 'D_j4n_g0_T3st_P4ss!',
            'password2': 'D_j4n_g0_T3st_P4ss!',
        }
        self.assertEqual(User.objects.count(), 0)

        response = self.client.post(self.url, user_data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

        self.assertEqual(User.objects.count(), 1)
        created_user = User.objects.first()
        self.assertEqual(created_user.username, 'novousuario')
  
        self.assertIn('_auth_user_id', self.client.session)
        self.assertEqual(int(self.client.session['_auth_user_id']), created_user.id)

    def test_invalid_registration_password_mismatch(self):
        """
        Testa se usuário tenta se registrar com senhas
        que não batem.
        """
        user_data = {
            'username': 'usuarioteste',
            'password1': 'senha12',
            'password2': 'senha22',
        }
        response = self.client.post(self.url, user_data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.count(), 0)
        self.assertTrue(response.context['form'].errors)        
        self.assertNotIn('_auth_user_id', self.client.session)
