from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.
class ProfileModelTest(TestCase):
  def setUpTestData():
    user = User.objects.create_user(username='ImmaTest', password='abcd1234')
    Profile.objects.create(user=user, about_me='I am a test user, I like long walks on the beach')

  def test_profile_user(self):
    profile = Profile.objects.get(id=1)
    field_label = profile._meta.get_field('user').verbose_name
    self.assertEqual(field_label, 'user')

class ProfilePageLinkTest(TestCase):
  def test_recipes_link_in_profile(self):
    response = self.client.get(reverse('profiles:profile'))                 
    self.assertContains(
      response,
      f'href="{reverse("recipes:home")}"'
    )

  def test_recipes_link_works(self):
    response = self.client.get(reverse('recipes:home'))
    self.assertEqual(response.status_code, 200)