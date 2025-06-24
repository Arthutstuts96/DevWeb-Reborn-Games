from datetime import datetime
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from game.forms import FormGame
from game.models import Game, GAME_CATEGORIES
from user.models import User 

class TestHomeView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='userteste', password='123')
        self.client.force_login(self.user)
        self.game = Game.objects.create(
            name='The Legend of Zelda',
            year=1986,
            create_date=timezone.now(),
            category=GAME_CATEGORIES[0][0],
            isUsed=True,
            owner=self.user,
            price=250.00,
            description='A classic NES adventure.'
        )
        self.url = reverse('home')

    def test_get_request(self):
        """Testa se a página da home carrega corretamente (GET)"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'game/home.html')
        
        self.assertIn('games', response.context)
        self.assertEqual(len(response.context['games']), 1)
        self.assertEqual(response.context['games'][0].name, 'The Legend of Zelda')


class TestCreateGameView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='userteste', password='123')
        self.client.force_login(self.user)
        self.url = reverse('create-game')

    def test_get_request(self):
        """Testa se a página de criação carrega o formulário corretamente (GET)"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'game/create_game.html')
        self.assertIsInstance(response.context.get('form'), FormGame)

    def test_post_request(self):
        """Testa se a view consegue criar um novo game via POST"""
        data = {
            'name': 'Super Mario Bros.',
            'year': 1985,
            'category': GAME_CATEGORIES[1][0],
            'create_date': datetime.now(),
            'owner': self.user,
            'isUsed': False,
            'price': 150.50,
            'description': 'The original platformer.'
        }
        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

        self.assertEqual(Game.objects.count(), 1)
        novo_game = Game.objects.first()
        self.assertEqual(novo_game.name, 'Super Mario Bros.')


class TestEditGameView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='userteste', password='123')
        self.client.force_login(self.user)
        self.game = Game.objects.create(
            name='Sonic',
            year=1991,
            create_date=timezone.now(),
            category=GAME_CATEGORIES[0][0],
            isUsed=True,
            owner=self.user,
            price=199.00,
            description='A fast-paced platformer.'
        )
        self.url = reverse('edit-game', kwargs={'pk': self.game.pk})

    def test_get_request(self):
        """Testa se a página de edição carrega os dados do game correto (GET)"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'game/edit_game.html')
        self.assertIsInstance(response.context.get('form'), FormGame)
        self.assertEqual(response.context.get('object'), self.game)

    def test_post_request(self):
        """Testa se a view consegue editar o game via POST"""
        data = {
            'name': 'Sonic the Hedgehog',  
            'year': 1991,
            'category': self.game.category,
            'create_date': datetime.now(),
            'owner': self.user,
            'isUsed': self.game.isUsed,
            'price': 210.00, 
            'description': self.game.description,
        }
        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

        self.game.refresh_from_db()
        self.assertEqual(self.game.name, 'Sonic the Hedgehog')
        self.assertEqual(self.game.price, 210.00)


class TestDeleteGameView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='userteste', password='123')
        self.client.force_login(self.user)
        self.game = Game.objects.create(
            name='Donkey Kong',
            year=1981,
            create_date=timezone.now(),
            category=GAME_CATEGORIES[0][0],
            isUsed=True,
            owner=self.user,
            price=99.00,
            description='Arcade classic.'
        )
        self.url = reverse('delete-game', kwargs={'pk': self.game.pk})

    def test_get_request(self):
        """Testa se a página de confirmação de deleção carrega corretamente (GET)"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'game/delete_game.html')
        self.assertEqual(response.context.get('object'), self.game)

    def test_post_request(self):
        """Testa se a view consegue deletar o game via POST"""
        response = self.client.post(self.url)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

        self.assertEqual(Game.objects.count(), 0)


class TestGameDetailView(TestCase):
    def setUp(self):
        """Prepara o ambiente para o teste da DetailView."""
        self.user = User.objects.create_user(username='userteste', password='123')
        self.client.force_login(self.user)
        self.game = Game.objects.create(
            name='Chrono Trigger',
            year=1995,
            create_date=timezone.now(),
            category=GAME_CATEGORIES[2][0], 
            isUsed=True,
            owner=self.user,
            price=350.00,
            description='A time-traveling RPG.'
        )
        self.url = reverse('game-detail', kwargs={'pk': self.game.pk})

    def test_get_request(self):
        """
        Testa se a página de detalhes carrega corretamente (GET) para um
        game existente.
        """
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'game/game-view.html')

        self.assertIn('game', response.context)
        self.assertEqual(response.context['game'], self.game)
        self.assertEqual(response.context['game'].name, 'Chrono Trigger')
        
    def test_404_for_invalid_game(self):
        """
        Testa se a view retorna um erro 404 ao tentar acessar um game
        que não existe.
        """
        invalid_url = reverse('game-detail', kwargs={'pk': self.game.pk + 1})
        response = self.client.get(invalid_url)

        self.assertEqual(response.status_code, 404)