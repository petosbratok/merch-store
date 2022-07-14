from django.urls import path
from . import views
from .views import (
    DeleteOrderItemAPI,
    IncreaseOrderItemAPI,
    DecreaseOrderItemAPI,
    CheckoutView,
)

urlpatterns = [
    path('', views.home, name='shop-home'),
    path('cart', views.cart, name='cart'),
    path('product/<str:pk>/', views.product, name="product"),
    path('checkout', CheckoutView.as_view(), name='checkout'),
    path('delete-order-item/<str:pk>', DeleteOrderItemAPI.as_view(), name='delete-order-item-api'),
    path('increase-order-item/<str:pk>', IncreaseOrderItemAPI.as_view(), name='increase-order-item-api'),
    path('decrease-order-item/<str:pk>', DecreaseOrderItemAPI.as_view(), name='decrease-order-item-api'),
]
