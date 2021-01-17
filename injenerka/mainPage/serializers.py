from rest_framework import serializers
from .models import Customer, Cart, CartProduct, Product, Order, ProductOrder, ImgProduct, Login, TableOrders, Rating


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__' # все поля преобразуем в джейсон

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__' # все поля преобразуем в джейсон

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' # все поля преобразуем в джейсон

class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = '__all__' # все поля преобразуем в джейсон

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__' # все поля преобразуем в джейсон


class ProductOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrder
        fields = '__all__' # все поля преобразуем в джейсон


class ImgProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImgProduct
        fields = '__all__' # все поля преобразуем в джейсон

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = '__all__' # все поля преобразуем в джейсон

class TableOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableOrders
        fields = '__all__' # все поля преобразуем в джейсон

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__' # все поля преобразуем в джейсон