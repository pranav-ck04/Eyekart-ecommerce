from django.urls import reverse
from distutils.command.upload import upload
from tabnanny import verbose
from unicodedata import category
from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=256, blank=True)
    cat_image = models.ImageField(upload_to='photos/categories',blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name
        
    def get_url(self):
        return reverse('products_by_category', args=[self.slug])
