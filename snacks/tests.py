from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from snacks.models import Snack

class SnackTests(TestCase):
  def setup(self):
    self.user = get_user_model().objects.create_user(
      username='tester', email='test@gmail.com', password=
      'password')
    self.snack = Snack.objects.create(
      name = 'fruit', purchaser = 'bran2miz', description = 'this fruit is delicious!'
      )
    
