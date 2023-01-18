from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# router = DefaultRouter()
# router.register(r'products', views.ProductViewSet)
# router.register(r'categories', views.CategoryViewSet)

# urlpatterns = router.urls
urlpatterns = [
    path(r'products/', views.get_products),
    path(r'categories/', views.get_categories),
    path(r'products/<int:pk>/', views.get_product),
    path(r'categories/<int:pk>/', views.get_category),
    path(r'categories/<int:pk>/products', views.get_products_by_category),
]
