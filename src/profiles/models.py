from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipe

# Create your models here.
class Profile (models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  recipes = models.ManyToManyField(Recipe, blank=True)
  avatar = models.ImageField(upload_to='avatars/', default='no_avatar.jpg', blank=True, null=True)
  about_me= models.TextField(blank=True)

  def __str__(self):
    return self.user.username