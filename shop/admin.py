from django.contrib import admin

# Register your models here.
from .models import Good, Type

admin.site.register(Good)
admin.site.register(Type)
