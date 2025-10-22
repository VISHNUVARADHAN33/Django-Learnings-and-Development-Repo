from rest_framework import serializers
from products.models import Product
from rest_framework.reverse import reverse
from .validators import  unique_product_title #validate_title_no_hello
from api.serializers import UserPublicSerializer



class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field = "pk",
        read_only = True
    )
    title = serializers.CharField(read_only=True)




class ProductSerializer(serializers.ModelSerializer):
    owner=UserPublicSerializer(source= 'user', read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk')
    title = serializers.CharField(validators =[unique_product_title]) #validate_title_no_hello
    body = serializers.CharField(source='content')

    class Meta:
        model = Product
        fields = ['owner','id', 'title', 'price', 'body', 'Discounted_price', 'path', 'public', 'endpoint','url','edit_url']  #'email', 'related_products',"" 'my_user_data'," " "  "  , 'discount'      "         "                      '       'user', -> this comment while learning the request user 
    

    def get_my_user_data(self, obj):
        return{
            "username": obj.user.username
        }

    def get_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()

    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('product-edit', kwargs={'pk':obj.pk},request=request)


