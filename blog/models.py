from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 150)
    excerpt = models.CharField(max_length = 200)
    image_name = modeld.CharField(max_length = 100)
    date = models.DateField(auto_now = True)
    slug = models.SlugField(unique = True, db_index = True)
    content = models.TextField(validators = [MinValueValidator(10)])
