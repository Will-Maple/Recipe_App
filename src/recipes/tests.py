from django.test import TestCase
from django.urls import reverse
from .models import Recipe

# Create your tests here.
class RecipeModelTest(TestCase):
  def setUpTestData():
    Recipe.objects.create(name="Imma Test", ingredients="Unicorn Horn, Bell Bottom Jeans, a Bob Dylan Single", cooking_time=4)

  def test_recipe_name(self):
    recipe = Recipe.objects.get(id=1)
    field_label = recipe._meta.get_field('name').verbose_name
    self.assertEqual(field_label, 'name')

  def test_recipe_ingredients_max_length(self):
    recipe = Recipe.objects.get(id=1)
    max_length = recipe._meta.get_field('ingredients').max_length
    self.assertEqual(max_length, 255)

class HomePageLinkTests(TestCase):
  def test_recipes_link_in_home(self):
    response = self.client.get(reverse('recipes:home'))                 
    self.assertContains(
      response,
      f'href="{reverse("recipes:list")}"'
    )
  def test_profile_link_in_home(self):
    response = self.client.get(reverse('recipes:home'))
    self.assertContains(
      response,
      f'href="{reverse("profiles:profile")}"'
    )

  def test_recipes_link_works(self):
    response = self.client.get(reverse('recipes:list'))
    self.assertEqual(response.status_code, 200)

  def test_porfile_link_works(self):
    response = self.client.get(reverse('profiles:profile'))
    self.assertEqual(response.status_code, 200)

class RecipesListDetailLinkTests(TestCase):
  def setUp(self):
    self.recipe = Recipe.objects.create(
      name="ImmaTest",
      ingredients="Green Magic, Dust Bunny, a whole lotta cows",
      cooking_time=30,
      instructions="Smash the things together",
    )

  def test_recipe_detail_links(self):
    response = self.client.get(reverse('recipes:list'))
    detail_url = self.recipe.get_absolute_url()
    self.assertContains(response, f'href="{detail_url}"')
    detail_response = self.client.get(detail_url)
    self.assertEqual(detail_response.status_code, 200)