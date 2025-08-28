from django.urls import path
from .views import home, RecipeListView, RecipeDetailView, add_recipe, graphs

app_name = 'recipes'

urlpatterns = [
  path('', home, name='home'),
  path('recipes/', RecipeListView.as_view(), name='list'),
  path('detail/<int:pk>/', RecipeDetailView.as_view(), name='detail'),
  path('add_recipe/', add_recipe, name='add'),
  path('graphs/', graphs, name='graphs'),
]