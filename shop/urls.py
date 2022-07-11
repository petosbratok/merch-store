from django.urls import path
from . import views
from .views import (
    ItemDetailView,
    CartListView,
    DeleteOrderItemAPI,
    IncreaseOrderItemAPI,
    DecreaseOrderItemAPI
)

urlpatterns = [
    path('', views.home, name='shop-home'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    # path('cart', CartListView.as_view(), name='cart'),
    path('cart', views.cart, name='cart'),
    path('product/<str:pk>/', views.product, name="product"),
    path('delete-order-item/<str:pk>', DeleteOrderItemAPI.as_view(), name='delete-order-item-api'),
    path('increase-order-item/<str:pk>', IncreaseOrderItemAPI.as_view(), name='increase-order-item-api'),
    path('decrease-order-item/<str:pk>', DecreaseOrderItemAPI.as_view(), name='decrease-order-item-api'),
]
