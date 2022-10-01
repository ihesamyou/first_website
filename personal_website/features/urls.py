from django.urls import path
from . import views

urlpatterns = [
    path('fibonacci_calculator/', views.fibonacci, name='fibonacci-calculator'),
    path('currency_converter/', views.currency_converter, name='currency-converter')
]
