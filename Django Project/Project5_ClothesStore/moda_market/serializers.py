from rest_framework import serializers
from .models import User,Item,UserPaymentInfo,FavoriteItem,ItemOption

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'user_type')

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class UpdateItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'gender', 'category', 'price', 'brand', 'rating']

class UserPaymentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPaymentInfo
        fields = ('credit_card_number',)

class FavoriteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteItem
        fields = '__all__'

class ItemOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemOption
        fields = '__all__'
