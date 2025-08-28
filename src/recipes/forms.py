from django import forms
from .models import Recipe

class RecipesSearchForm(forms.Form):
  query = forms.CharField(max_length=50)

class RecipeForm(forms.ModelForm):
  class Meta:
    model=Recipe
    fields = ['name', 'ingredients', 'cooking_time', 'difficulty', 'instructions', 'image']