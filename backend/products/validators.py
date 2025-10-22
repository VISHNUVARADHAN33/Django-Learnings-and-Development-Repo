from rest_framework import serializers
from .models import Product
from rest_framework.validators import UniqueValidator

#alternative validator examples kept for reference; replaced by the DRF UniqueValidator instance below.
"""
def validate_title(value):
    qs = Product.objects.filter(title__iexact=value)
    if qs.exists():
        raise serializers.ValidationError(f"{value} is already there. give some thing new")
    return value

def validate_title_no_hello(value):                                                    this are just try out differnet ways
    if "iphone" in value.lower():
        raise serializers.ValidationError(f"No more iphones are allowed")
    return value
"""
unique_product_title = UniqueValidator(queryset=Product.objects.all(), lookup='iexact')