from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from . import models, serializers


# Create your views here.
@api_view(['GET'])
def get_products(request, *args, **kwargs):
    products = models.Product.objects.all()
    serializer = serializers.ProductSerializer(products, many=True).data
    return Response(serializer)


@api_view(['GET'])
def get_categories(request, *args, **kwargs):
    categories = models.Category.objects.all()
    serializer = serializers.CategorySerializer(categories, many=True).data
    return Response(serializer)


@api_view(['GET'])
def get_product(request, *args, **kwargs):
    # products = models.Product.objects.get(id=pk)
    product = get_object_or_404(models.Product, **kwargs)
    serializer = serializers.ProductSerializer(product).data

    return Response(serializer)


@api_view(['GET'])
def get_category(request, *args, **kwargs):
    category = get_object_or_404(models.Category, **kwargs)
    serializer = serializers.CategorySerializer(category).data
    return Response(serializer)


@api_view(['GET'])
def get_products_by_category(request, *args, **kwargs):
    category = models.Category.objects.get(**kwargs)
    products = category.products.all()
    serializer = serializers.ProductSerializer(products, many=True).data
    return Response(serializer)


# class ProductViewSet(ModelViewSet):
#     queryset = models.Product.objects.all()
#     serializer_class = serializers.ProductSerializer
#
#
# class CategoryViewSet(ModelViewSet):
#     queryset = models.Category.objects.all()
#     serializer_class = serializers.CategorySerializer
