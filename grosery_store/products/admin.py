from django.contrib import admin
from .models import Category, SubCategory, Product


admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.site_header = "Магазин продуктов"
admin.site.site_title = "Магазин продуктов"
admin.site.index_title = "Администрирование магазина продуктов"