from rest_framework import serializers
from products.models import Product
from rest_framework.reverse import reverse

class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)
    #url = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk')
    #email= serializers.EmailField(write_only=True)                                                   --> RFC comment after model serializer learning
    class Meta:
        model = Product
        fields = ['url','edit_url','id', 'title', 'price', 'content', 'Discounted_price', 'discount']  #'email', "" " " "  "        "         "
    # Reason for the comment: This learned on model serializer
    # def create(self, validated_data):                      
    #     #email = validated_data.pop('email')  -> Reason for comment this handel on view.py
    #     obj = super(). create(validated_data)
    #     #print(email, obj)                    ->    "     "      "    "      "
    #     return obj
    
    # def update(self, instance, validated_data):
    #     email = validated_data.pop('email')
    #     return super().update(instance, validated_data)

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


