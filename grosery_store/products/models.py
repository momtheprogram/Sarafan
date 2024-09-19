from django.conf import settings
from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='название категории')
    slug = models.SlugField(unique=True, verbose_name='slug')
    image = models.ImageField(upload_to='categories/', verbose_name='картинка категории')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='название подкатегории')
    slug = models.SlugField(unique=True, verbose_name='slug')
    image = models.ImageField(upload_to='subcategories/', verbose_name='картинка подкатегории')
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE, verbose_name='категория подкатегории')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.nsme

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='продукт')
    slug = models.SlugField(unique=True, verbose_name='slug')
    image = models.ImageField(upload_to='products/', verbose_name='картинка продукта')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена продукта')
    subcategory = models.ForeignKey(SubCategory, related_name='products', on_delete=models.CASCADE, verbose_name='подкатегория продукта')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='владелец корзины')

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE, verbose_name='корзина')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    quantity = models.PositiveIntegerField(default=1, verbose_name='количество позиций в корзине')

    class Meta:
        unique_together = ('cart', 'product')
        verbose_name = 'Количество позиций в корзине'