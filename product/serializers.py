from django.http import request
import product
from model_utils import fields
from rest_framework import serializers
from .models import Product, ProductReview



class ProductListSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Product
        # exclude = ("description", "image", "created_at")
        fields = "__all__" 
# ('title', 'status', 'description', 'price', etc...)

class ProductDetailSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Product
        fields = "__all__"
    
    def to_representation(self, instance):
        representation = super(ProductDetailSerializer,
        self).to_representation(instance)
        representation['reviews'] = ProductReviewSerializer(
            ProductReview.objects.filter(product=instance.id),
            many=True
        ).data
        return representation

class ProductCreateSerializer(serializers.ModelSerializer):
    
    
    class Meta(ProductDetailSerializer.Meta):
        pass
    
    
    def validate_price(self, price):
        if price < 100:
            raise serializers.ValidationError(
                "Price cannot be negative and less then 100")
        return price

class ProductReviewSerializer(serializers.ModelSerializer):
    

    product_title = serializers.SerializerMethodField('get_product_title')


    class Meta:
        model = ProductReview
        fields = "__all__"

    
    def get_product_title(self, product_review):
        title = product_review.product.title
        return title


    def validate_product(self, product):
        if self.Meta.model.objects.filter(product=product).exists():
            raise serializers.ValidationError(
                "You cannot comment under this post"
            )        
        return product

    def validate_rating(self, rating):
        
        if rating not in range(1, 6):
            raise serializers.ValidationError(
                "Rating should be in range from 1 to 5"
            )
        return rating
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')
        print(request, 'Hello')
        if not request.user.is_anonymous:
            representation['author'] = request.user.email
        return representation


        #instance.author etc. hw