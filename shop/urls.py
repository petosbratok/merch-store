from django.urls import path
from . import views
from .views import (
    ItemDetailView,
    CartListView,
)

urlpatterns = [
    path('', views.home, name='shop-home'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    # path('cart', CartListView.as_view(), name='cart'),
    path('cart', views.cart, name='cart'),
    path('product/<str:pk>/', views.product, name="product"),
]
