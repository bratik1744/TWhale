from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ticker/<str:name>/', views.ticker_detail, name='ticker_detail'),
]