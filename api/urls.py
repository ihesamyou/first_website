from django.urls import path
from . import views

urlpatterns = [
    path('docs/', views.api_docs, name='api-docs'),
    path('docs/currency_docs/', views.currency_docs, name='currency-docs'),
    path('docs/fibonacci_docs/', views.fibonacci_docs, name='fibonacci-docs'),
    path('docs/quote_docs/', views.quote_docs, name='quote-docs'),
    path('currency/', views.CurrencyAPIView.as_view()),
    path('currency/<str:name>/', views.CurrencyAPIView.as_view()),
    path('rial_converter/<str:name>/<int:amount>',
         views.RialConverterAPIView.as_view()),
    path('currency_converter/<str:name>/<int:amount>',
         views.CurrencyConverterAPIView.as_view()),
    path('quote/', views.QuoteAPIView.as_view()),
    path('fibonacci_index/<int:number>', views.FibonacciIndexAPIView.as_view()),
    path('fibonacci_until/<int:number>', views.FibonacciUntilAPIView.as_view())
]
