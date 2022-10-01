from rest_framework import serializers
from features.models import Currency


class CurrencySerializer(serializers.ModelSerializer):
    """
    Currency Model Serializer.
    """
    name = serializers.CharField(max_length=100)
    price = serializers.IntegerField(required=False, default=None)

    class Meta:
        model = Currency
        fields = ('name', 'price')
