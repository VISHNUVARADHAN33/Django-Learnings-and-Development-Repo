from rest_framework import generics
from products.models import Product
from products.serializers import ProductSerializer

class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_create_view = ProductCreateAPIView.as_view()


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #lookup_field = 'title'  # change lookup to title


product_detail_view = ProductDetailAPIView.as_view() 