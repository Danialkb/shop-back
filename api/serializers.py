from rest_framework import serializers
from . import models


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product
        fields = '__all__'


class _ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product
        fields = (
            'id',
            'name',
            'amount',
            'price',
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'

