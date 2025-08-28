from django.test import TestCase
from django.urls import reverse
from .models import Recipe
from .forms import RecipesSearchForm, RecipeForm

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
  def test_login_link_in_home(self):
    response = self.client.get(reverse('recipes:home'))
    self.assertContains(
      response,
      f'href="{reverse("login")}"'
    )

  def test_recipes_link_works(self):
    response = self.client.get(reverse('recipes:list'))
    self.assertEqual(response.status_code, 200)

  def test_login_link_works(self):
    response = self.client.get(reverse('login'))
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

  class RecipesSearchTest(TestCase):
    def test_valid_search(self):
      form = RecipesSearchForm({
        'query': 'Water'
      })
      self.assertTrue(form.is_valid())

    def missing_query(self):
      form = RecipesSearchForm({
        'query': ''
      })
      self.assertFalse(form.is_valid())

    def query_length_test(self):
      form = RecipesSearchForm({
        'query': 'x' * 70
      })
      self.assertFalse(form.is_valid())

class RecipeFormTest(TestCase):
    def test_valid_recipe_input(self):
      form = RecipeForm({
        'name': 'Water',
        'ingredients': 'h, 2, o',
        'cooking_time': 5,
        'difficulty': 'easy',
        'instructions': '',
        'image': None
      })
      self.assertTrue(form.is_valid())

    def missing_name(self):
      form = RecipeForm({
        'name': '',
        'ingredients': 'h, 2, o',
        'cooking_time': 5,
        'difficulty': 'easy',
        'instructions': '',
        'image': None
      })
      self.assertFalse(form.is_valid())

    def missing_ingredients(self):
      form = RecipeForm({
        'name': 'water',
        'ingredients': '',
        'cooking_time': 5,
        'difficulty': 'easy',
        'instructions': '',
        'image': None
      })
      self.assertFalse(form.is_valid())

    def missing_cooking_time(self):
      form = RecipeForm({
        'name': 'Water',
        'ingredients': 'h, 2, o',
        'cooking_time': '',
        'difficulty': 'easy',
        'instructions': '',
        'image': None
      })
      self.assertFalse(form.is_valid())

    def name_too_long(self):
      form = RecipeForm({
        'name': 'x' * 60,
        'ingredients': 'h, 2, o',
        'cooking_time': 5,
        'difficulty': 'easy',
        'instructions': '',
        'image': None
      })
      self.assertFalse(form.is_valid())

    def ingredients_too_long(self):
      form = RecipeForm({
        'name': 'water',
        'ingredients': 'x' * 300,
        'cooking_time': 5,
        'difficulty': 'easy',
        'instructions': '',
        'image': None
      })
      self.assertFalse(form.is_valid())