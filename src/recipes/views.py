from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.db.models import Q, Count
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
import pandas as pd
from .models import Recipe
from .forms import RecipesSearchForm, RecipeForm
from .utils import get_chart

# Create your views here.
def home(request):
  three_recipes = Recipe.objects.all()[:3]
  return render(request, 'recipes/home.html', {'three_recipes': three_recipes})

class RecipeListView(ListView):
  model = Recipe
  template_name = 'recipes/list.html'

  def get_queryset(self):
    queryset = super().get_queryset()
    self.form = RecipesSearchForm(self.request.GET or None)
    if self.form.is_valid() and self.form.cleaned_data['query']:
      query = self.form.cleaned_data['query']
      queryset = queryset.filter(
        Q(name__icontains=query) | Q(ingredients__icontains=query)
      )
    self.recipe_queryset = queryset
    return queryset
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    query = self.request.GET.get('query', '')
    context['form'] = getattr(self, 'form', RecipesSearchForm())
    if query:
      recipe_qs = getattr(self, 'recipe_queryset', self.get_queryset())
      df = pd.DataFrame(list(recipe_qs.values('name','ingredients', 'id')))
      df['name'] = df.apply(
        lambda row: f'<a href="{reverse("recipes:detail", kwargs={"pk": row["id"]})}">{row["name"]}</a>',
        axis = 1
      )
      context['dataframe_html'] = df.to_html(classes='table table=striped', escape=False, index=False)
      context['show_dataframe'] = True
    else:
      context['show_dataframe'] = False
    return context

class RecipeDetailView(DetailView):
  model = Recipe
  template_name = 'recipes/details.html'

@login_required
def add_recipe(request):
  if request.method == 'POST':
    form = RecipeForm(request.POST, request.FILES)
    if form.is_valid():
      recipe = form.save(commit=False)
      recipe.save()
      request.user.profile.recipes.add(recipe)
      messages.success(request, "Recipe created successfully!")
      return redirect(request.path)
    else:
      messages.error(request, "Please correct the error(s)")
  else:
    form = RecipeForm()
  return render(request, 'recipes/add.html', {'form': form})

def graphs(request):
  difficulties = ['easy', 'medium', 'difficult']
  sizes = [Recipe.objects.filter(difficulty=d).count() for d in difficulties]
  pie_data = {'labels': ['Easy', 'Medium', 'Difficult'], 'sizes': sizes}
  chart_pie = get_chart('pie', pie_data)

  labels = ['Image', 'W/o Img', 'Instructions', 'W/o Instr']
  counts = [
    Recipe.objects.exclude(image='').count(),
    Recipe.objects.filter(image='no_picture.jpg').count(),
    Recipe.objects.exclude(instructions='').count(),
    Recipe.objects.filter(instructions='').count()
  ]
  bar_data = {'labels': labels, 'counts': counts}
  chart_bar = get_chart('bar', bar_data)

  recipes_by_date = (
    Recipe.objects.values('date_created')
    .annotate(count=Count('id'))
    .order_by('date_created')
  )
  dates = [r['date_created'].strftime('%Y-%m-%d') for r in recipes_by_date]
  counts = [r['count'] for r in recipes_by_date]
  line_data = {'dates': dates, 'counts': counts}
  chart_line = get_chart('line', line_data)

  context = {
    'chart_pie': chart_pie,
    'chart_bar': chart_bar,
    'chart_line': chart_line,
  }
  return render(request, 'recipes/graphs.html', context)