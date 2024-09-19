from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination

from .models import Category, SubCategory, Product
from serializers import CategorySerializer, SubCategorySerializer, ProductSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = StandardResultsSetPagination


class SubCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    pagination_class = StandardResultsSetPagination


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination
