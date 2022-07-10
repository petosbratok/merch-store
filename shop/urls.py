from django.urls import path
from . import views
from .views import (
    Home,
)

urlpatterns = [
    path('', Home.as_view(), name='shop-home'),
]
