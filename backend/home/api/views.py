import json
from products.serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.forms.models import model_to_dict
from products.models import Product
# Create your views here.
@api_view(['GET'])
def api_home(request, *args, **kwargs):
    # DRF
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        data = ProductSerializer(instance).data
    return Response(data)