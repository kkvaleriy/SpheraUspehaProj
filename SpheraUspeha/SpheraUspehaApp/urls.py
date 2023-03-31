from django.urls import path
from .views import MainView, Product, OrderView, SearchView

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('product/<slug>', Product.as_view(), name='product'),
    path('order/', OrderView.as_view(), name='order'),
    path('order/thank/', OrderView.as_view(), name='thank'),
    path('search/', SearchView.as_view(), name='search')
]