from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('article/<int:pk>/', views.article,
         name='article-detail'),
    path('article/<int:pk>/<int:cm>/', views.article,
         name='article-detail'),
    path('about/', views.about, name='about-me')
]
