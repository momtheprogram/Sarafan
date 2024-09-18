from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.Slugfield(unique=True)
    image = models.ImageField(upload_to='categories/')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.Slugfield(unique=True)
    image = models.ImageField(upload_to='subcategories/')
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nsme

class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.Slugfield(unique=True)
    image = models.ImageField(upload_to='products/')
    price = models.DeimalField(max_length=10, decimal_places=2)
    subcategory = models.ForeignKey(Subcategory, related_name='products', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
