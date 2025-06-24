from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from game.models import Game, GAME_CATEGORIES
from review.forms import FormReview
from review.models import Review

User = get_user_model()

class ReviewListViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='userteste', password='123')
        self.client.force_login(self.user)
        
        self.game1 = Game.objects.create(
            name='Game 1',
            year=2023,
            owner=self.user,
            price=100.00,
            category=GAME_CATEGORIES[0][0],  
            isUsed=True,                   
            description='Description for game 1.'
        )
        self.game2 = Game.objects.create(
            name='Game 2',
            year=2024,
            owner=self.user,
            price=200.00,
            category=GAME_CATEGORIES[1][0], 
            isUsed=False,                   
            description='Description for game 2.'
        )

        Review.objects.create(game_id=self.game1, reviewer=self.user, content='Review 1 para Game 1', stars=5)
        Review.objects.create(game_id=self.game1, reviewer=self.user, content='Review 2 para Game 1', stars=4)
        Review.objects.create(game_id=self.game2, reviewer=self.user, content='Review 1 para Game 2', stars=3)
        
        self.url = reverse('review:list', kwargs={'game_pk': self.game1.pk})

    def test_queryset_is_filtered_by_game(self):
        """Testa se a lista de reviews contém apenas as reviews do jogo correto."""
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, 200)
        self.assertIn('reviews', response.context)
        self.assertEqual(len(response.context['reviews']), 2)
        for review in response.context['reviews']:
            self.assertEqual(review.game_id, self.game1)


class CreateReviewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='userteste', password='123')
        self.client.force_login(self.user)
        self.game = Game.objects.create(
            name='Game para Review',
            year=2025,
            owner=self.user,
            price=300.00,
            category=GAME_CATEGORIES[2][0],
            isUsed=True,                    
            description='Description for the game to be reviewed.' 
        )
        
        self.url = reverse('review:create-review', kwargs={'game_pk': self.game.pk})

    def test_get_request_renders_form(self):
        """Testa se a página de criação (GET) é renderizada corretamente."""
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('form'), FormReview)
        self.assertEqual(response.context.get('game'), self.game)

    def test_successful_post_request(self):
        """Testa o envio de um formulário válido (POST) para criar uma review.""" 
        review_data = {
            'content': 'Um jogo espetacular!',
            'stars': 5,
        }
        
        response = self.client.post(self.url, review_data)
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Review.objects.count(), 1)
        
        new_review = Review.objects.first()
        self.assertEqual(new_review.content, 'Um jogo espetacular!')
        self.assertEqual(new_review.game_id, self.game)
        self.assertEqual(new_review.reviewer, self.user)