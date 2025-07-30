from django.db import models

# Create your models here.
class Recipe (models.Model):
  name = models.CharField(max_length=55)
  ingredients = models.CharField(max_length=255)
  cooking_time = models.IntegerField()
  difficulty = models.CharField(max_length=20)
  instructions = models.TextField(blank=True)
  date_created = models.DateTimeField(auto_now_add=True)
  image = models.ImageField(blank=True, null=True)

  def __str__(self):
    return str(self.name)