from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe

# Create your views here.
def home(request):
  three_recipes = Recipe.objects.all()[:3]
  return render(request, 'recipes/home.html', {'three_recipes': three_recipes})

class RecipeListView(ListView):
  model = Recipe
  template_name = 'recipes/list.html'

class RecipeDetailView(DetailView):
  model = Recipe
  template_name = 'recipes/details.html'