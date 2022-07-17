from django.urls import path
from . import views
from .views import (
    DeleteOrderItemAPI,
    IncreaseOrderItemAPI,
    DecreaseOrderItemAPI,
    SaveDeliveryInfoAPI,
    CheckoutView,
    CreateCheckoutSessionView,
)

urlpatterns = [
    path('', views.home, name='shop-home'),
    path('cart', views.cart, name='cart'),
    path('product/<str:pk>/', views.product, name="product"),
    path('checkout', CheckoutView.as_view(), name='checkout'),
    path('create-checkout-session/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('order/<str:pk>/', views.order, name='order'),
    path('cancel/', views.cancel, name='cancel'),
    path('webhook/', views.stripe_webhook),
    path('deletecookies/<str:order_id>/', views.delete_user_cookies),
    path('delete-order-item/<str:pk>', DeleteOrderItemAPI.as_view(), name='delete-order-item-api'),
    path('increase-order-item/<str:pk>', IncreaseOrderItemAPI.as_view(), name='increase-order-item-api'),
    path('decrease-order-item/<str:pk>', DecreaseOrderItemAPI.as_view(), name='decrease-order-item-api'),
    path('save-delivery-info', SaveDeliveryInfoAPI.as_view(), name='save-delivery-infoi'),
]
