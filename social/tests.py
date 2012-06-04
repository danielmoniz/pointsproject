import unittest
from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User

class SocialTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('testman', 'testman@test.com', 'testtest')

    def tearDown(self):
        self.client.logout()
        self.user.delete()

    def test_wall_submit(self):
        pass
