from rest_framework import serializers
from .models import Product

def validate_title(self, value):
    qs = Product.objects.filter(title__exact=value)
    if qs.exists():
        raise serializers.ValidationError(f"{value} is already a product name.")
    return value