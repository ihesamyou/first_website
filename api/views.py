from django.http.response import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CurrencySerializer
from features.models import Currency
from django.core.cache import cache
from features.fibonacci_sequence import fibonacci_until, fibonacci_index
from django.shortcuts import get_object_or_404


def api_docs(request):
    return render(request, 'api/api_docs.html')


def currency_docs(request):
    return render(request, 'api/currency_docs.html')


def fibonacci_docs(request):
    return render(request, 'api/fibonacci_docs.html')


def quote_docs(request):
    return render(request, 'api/quote_docs.html')


class CurrencyAPIView(APIView):
    def get(self, request, name=None):
        if name:
            currency = get_object_or_404(Currency, name=name)
            serializer = CurrencySerializer(currency)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Currency.objects.all()
        serializer = CurrencySerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


class RialConverterAPIView(APIView):
    def get(self, request, name, amount):
        currency = get_object_or_404(Currency, name=name)
        result = amount/currency.price
        return Response({"status": "success", "data": result}, status=status.HTTP_200_OK)


class CurrencyConverterAPIView(APIView):
    def get(self, request, name, amount):
        currency = get_object_or_404(Currency, name=name)
        result = amount*currency.price
        return Response({"status": "success", "data": result}, status=status.HTTP_200_OK)


class QuoteAPIView(APIView):
    def get(self, request):
        quote = cache.get('quote').decode('UTF-8')
        if quote:
            return Response({"status": "success", "data": quote}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error"}, status=status.HTTP_404_NOT_FOUND)


class FibonacciIndexAPIView(APIView):
    def get(self, request, number):
        if number < 1001:
            answer = fibonacci_index(number)
            return Response({"status": "success", "data": answer}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": "number is too big. use positive numbers less than 1000."}, status=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE)


class FibonacciUntilAPIView(APIView):
    def get(self, request, number):
        if number < 26863810024485359386146727202142923967616609318986952340123175997617981700247881689338369654483356564191827856161443356312976673642210350324634850410377680367334151172899169723197082763985615764450078474174628:
            answer = fibonacci_until(number)
            return Response({"status": "success", "data": answer}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": "number is too big."}, status=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE)
