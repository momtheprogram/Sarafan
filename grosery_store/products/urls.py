from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    CategoryViewSet,
    SubCategoryViewSet,
    ProductViewSet,
    CartViewSet,
    CustomAuthToken,
    ProtectedView,
)

app_name = 'products'

router = DefaultRouter()

router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubCategoryViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('cart/', CartViewSet.as_view({
        'get': 'get_cart',
        'post': 'add_to_cart',
    })),
    path('cart/<int:pk>/', CartViewSet.as_view({
        'put': 'update_cart_item',
        'delete': 'delete_cart_item',
    })),
    path('cart/clear/', CartViewSet.as_view({'post': 'clear_cart'})),
    path('api/token/', CustomAuthToken.as_view(), name='api_token_auth'),
    path('api/protected/', ProtectedView.as_view(), name='protected_view'),
]
