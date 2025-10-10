from rest_framework import generics
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404



class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_list_create_view = ProductListCreateAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #lookup_field = 'title'  # change lookup to title

product_detail_view = ProductDetailAPIView.as_view() 

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

product_update_view = ProductUpdateAPIView.as_view() 

class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

product_Destroy_view = ProductDestroyAPIView.as_view() 

# this for get the get the list of items only
class ProductListAPIView(generics.ListAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
product_list_view = ProductListAPIView.as_view()

@api_view(['GET','POST'])
def product_alt_view(request, pk=None, *args, **Kwargs):
    method = request.method

    if method == "GET":
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
        
    if method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)

            return Response(serializer.data)
        return Response ({"invalid":"Not good data"})
