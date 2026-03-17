from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from .models import Team, UserProfile


class TrackerApiTests(TestCase):
	def setUp(self):
		self.client = APIClient()
		self.team = Team.objects.create(name='Blue Sharks', description='Morning team')
		self.user = UserProfile.objects.create(
			username='mona',
			first_name='Mona',
			last_name='Octo',
			email='mona@example.com',
			team=self.team,
			fitness_level='intermediate',
		)

	def test_api_root(self):
		response = self.client.get(reverse('api-root'))
		self.assertEqual(response.status_code, 200)
		self.assertIn('endpoints', response.json())

	def test_users_endpoint(self):
		response = self.client.get('/api/users/')
		self.assertEqual(response.status_code, 200)
		self.assertGreaterEqual(len(response.json()), 1)
