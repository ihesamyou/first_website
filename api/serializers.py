from rest_framework import serializers
from features.models import Currency
from blog.models import Quote
from features.fibonacci_sequence import fibonacci_index, fibonacci_until


class CurrencySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    price = serializers.IntegerField(required=False, default=None)

    class Meta:
        model = Currency
        fields = ('__all__')
