from rest_framework import serializers
from . import models


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    price = serializers.FloatField()
    description = serializers.CharField()
    amount = serializers.IntegerField()
    is_active = serializers.BooleanField()


class ProductModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product
        fields = '__all__'

# class _ProductSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = models.Product
#         fields = (
#             'id',
#             'name',
#             'amount',
#             'price',
#         )


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

