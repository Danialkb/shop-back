from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# router = DefaultRouter()
# router.register(r'products', views.ProductViewSet)
# router.register(r'categories', views.CategoryViewSet)

# urlpatterns = router.urls
urlpatterns = [
    path('products/', views.get_products),
    path('categories/', views.get_categories),
    path('products/<int:pk>/', views.get_product),
    path('categories/<int:pk>/', views.get_category),
    # path('categories/<int:pk>/products', views.get_products_by_category),
]
