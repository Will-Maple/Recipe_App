from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Recipe (models.Model):
  name = models.CharField(max_length=55)
  ingredients = models.CharField(max_length=255)
  cooking_time = models.IntegerField()
  DIFFICULTY_CHOICES = [
    ('easy', 'Easy'),
    ('medium', 'Medium'),
    ('difficult', 'Difficult'),
  ]
  difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='easy')
  instructions = models.TextField(blank=True)
  date_created = models.DateTimeField(auto_now_add=True)
  image = models.ImageField(upload_to='recipes', default='no_picture.jpg', blank=True, null=True)

  def get_absolute_url(self):
    return reverse ('recipes:detail', kwargs={'pk': self.pk})

  def __str__(self):
    return str(self.name)