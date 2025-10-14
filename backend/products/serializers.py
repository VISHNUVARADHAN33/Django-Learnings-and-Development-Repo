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
    related_products = ProductInlineSerializer(source='user.product_set.all', read_only=True, many=True)
    my_user_data = serializers.SerializerMethodField(read_only = True)
    discount = serializers.SerializerMethodField(read_only=True)
    owner=UserPublicSerializer(source= 'user', read_only=True)
    #url = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk')
    title = serializers.CharField(validators =[unique_product_title]) #validate_title_no_hello
    #name = serializers.CharField(source="title", read_only=True)                                                                                              # -> learned for validation
    #email= serializers.EmailField(write_only=True)                                                   --> RFC comment after model serializer learning
    class Meta:
        model = Product
        fields = ['related_products','owner','my_user_data','url','edit_url','id', 'title', 'price', 'content', 'Discounted_price', 'discount']  #'email', "" " " "  "        "         "                      '       'user', -> this comment while learning the request user 
    

    def get_my_user_data(self, obj):
        return{
            "username": obj.user.username
        }
    # def validate_title(self, value):
    #     qs = Product.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already there. give some thing new")
    #     return value
    # Reason for the comment: This learned on model serializer
    """
    def create(self, validated_data):                      
        #email = validated_data.pop('email')  -> Reason for comment this handel on view.py
        obj = super(). create(validated_data)
        #print(email, obj)                    ->    "     "      "    "      "
        return obj
    
    def update(self, instance, validated_data):
        email = validated_data.pop('email')
        return super().update(instance, validated_data)

        """
    def get_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()

    # def get_url(self, obj):
    #     request = self.context.get('request')
    #     if request is None:
    #         return None
    #     return reverse('product-detail', kwargs={'pk':obj.pk},request=request)

    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('product-edit', kwargs={'pk':obj.pk},request=request)


