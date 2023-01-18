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
    return JsonResponse(serializer, safe=False)


@api_view(['GET'])
def get_categories(request, *args, **kwargs):
    categories = models.Category.objects.all()
    serializer = serializers.CategorySerializer(categories, many=True).data
    return JsonResponse(serializer, safe=False)


@api_view(['GET'])
def get_product(request, pk, *args, **kwargs):
    # products = models.Product.objects.get(id=pk)
    product = get_object_or_404(models.Product, id=pk)
    serializer = serializers.ProductSerializer(product).data

    return JsonResponse(serializer, safe=False)


def get_category(request, pk, *args, **kwargs):
    category = get_object_or_404(models.Category, id=pk)
    serializer = serializers.CategorySerializer(category).data
    return JsonResponse(serializer, safe=False)


def get_products_by_category(request, pk, *args, **kwargs):
    category = get_object_or_404(models.Category, id=pk)
    products = category.products.all()
    serializer = serializers.ProductSerializer(products, many=True).data
    return JsonResponse(serializer, safe=False)


# class ProductViewSet(ModelViewSet):
#     queryset = models.Product.objects.all()
#     serializer_class = serializers.ProductSerializer
#
#
# class CategoryViewSet(ModelViewSet):
#     queryset = models.Category.objects.all()
#     serializer_class = serializers.CategorySerializer
