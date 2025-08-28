from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class LoginProtectionTest(TestCase):
  def setUp(self):
    User.objects.create_user(username='testy', password='mctestyface')

  def test_add_redirects_if_no_user(self):
    response = self.client.get(reverse('recipes:add'))
    self.assertNotEqual(response.status_code, 200)
    self.assertRedirects(response, '/accounts/login/?next=' + reverse('recipes:add'))

  def test_add_access_if_logged_in(self):
    self.client.login(username='testy', password='mctestyface')
    response = self.client.get(reverse('recipes:add'))
    self.assertEqual(response.status_code, 200)

  def test_profile_redirects_if_no_user(self):
    response = self.client.get(reverse('profiles:profile'))
    self.assertNotEqual(response.status_code, 200)
    self.assertRedirects(response, '/accounts/login/?next=' + reverse('profiles:profile'))

  def test_add_access_if_logged_in(self):
    self.client.login(username='testy', password='mctestyface')
    response = self.client.get(reverse('profiles:profile'))
    self.assertEqual(response.status_code, 200)

class MenuLinkTestsNoUser(TestCase):
  def test_graphs_link_in_menu(self):
    response = self.client.get(reverse('recipes:home'))                 
    self.assertContains(
      response,
      f'href="{reverse("recipes:graphs")}"'
    )

  def test_graphs_link_works(self):
    response = self.client.get(reverse('recipes:graphs'))
    self.assertEqual(response.status_code, 200)

  def test_login_link_in_menu(self):
    response = self.client.get(reverse('recipes:home'))                 
    self.assertContains(
      response,
      f'href="{reverse("login")}"'
    )

  def test_login_link_works(self):
    response = self.client.get(reverse('login'))
    self.assertEqual(response.status_code, 200)

  def test_me_link_in_menu(self):
    response = self.client.get(reverse('recipes:home'))                 
    self.assertContains(
      response,
      f'href="{reverse("me")}"'
    )

  def test_graphs_link_works(self):
    response = self.client.get(reverse('me'))
    self.assertEqual(response.status_code, 200)

  def test_logout_link_not_in_menu(self):
    response = self.client.get(reverse('recipes:home'))                 
    self.assertNotContains(
      response,
      f'href="{reverse("logout")}"'
    )

class MenuLinkTestsLoggedIn(TestCase):
  def setUp(self):
    User.objects.create_user(username='testy', password='mctestyface')
    self.client.login(username='testy', password='mctestyface')

  def test_graphs_link_in_menu(self):
    response = self.client.get(reverse('recipes:home'))                 
    self.assertContains(
      response,
      f'href="{reverse("recipes:graphs")}"'
    )

  def test_graphs_link_works(self):
    response = self.client.get(reverse('recipes:graphs'))
    self.assertEqual(response.status_code, 200)

  def test_logout_link_in_menu(self):
    response = self.client.get(reverse('recipes:home'))                 
    self.assertContains(
      response,
      f'href="{reverse("logout")}"'
    )

  def test_logout_link_works(self):
    response = self.client.get(reverse('logout'))
    self.assertEqual(response.status_code, 302)

  def test_me_link_in_menu(self):
    response = self.client.get(reverse('recipes:home'))                 
    self.assertContains(
      response,
      f'href="{reverse("me")}"'
    )

  def test_graphs_link_works(self):
    response = self.client.get(reverse('me'))
    self.assertEqual(response.status_code, 200)

  def test_add_link_in_menu(self):
    response = self.client.get(reverse('recipes:home'))                 
    self.assertContains(
      response,
      f'href="{reverse("recipes:add")}"'
    )

  def test_add_link_works(self):
    response = self.client.get(reverse('recipes:add'))
    self.assertEqual(response.status_code, 200)

  def test_profiles_link_in_menu(self):
    response = self.client.get(reverse('recipes:home'))                 
    self.assertContains(
      response,
      f'href="{reverse("profiles:profile")}"'
    )

  def test_add_link_works(self):
    response = self.client.get(reverse('recipes:add'))
    self.assertEqual(response.status_code, 200)

  def test_login_link_not_in_menu(self):
    response = self.client.get(reverse('recipes:home'))                 
    self.assertNotContains(
      response,
      f'href="{reverse("login")}"'
    )