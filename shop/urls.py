from django.urls import path
from . import views
from .views import (
    HomeListView,
    ItemDetailView,
)

urlpatterns = [
    path('', HomeListView.as_view(), name='shop-home'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),

]
