from django.test import TestCase
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