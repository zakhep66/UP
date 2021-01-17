from .models import Customer, Cart, CartProduct, Product, Order, ProductOrder, ImgProduct, Login, TableOrders, Rating
from rest_framework import viewsets, permissions
from .serializers import CustomerSerializer, CartSerializer, CartProductSerializer, ProductSerializer, OrderSerializer, ProductOrderSerializer, ImgProductSerializer, LoginSerializer, TableOrdersSerializer, RatingSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all() # объекты клиента в БД
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = CustomerSerializer


class CartProductViewSet(viewsets.ModelViewSet):
    queryset = CartProduct.objects.all() # объекты клиента в БД
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = CartProductSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all() # объекты клиента в БД
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = CartSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all() # объекты клиента в БД
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProductSerializer


class ProductOrderViewSet(viewsets.ModelViewSet):
    queryset = ProductOrder.objects.all() # объекты клиента в БД
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProductOrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all() # объекты клиента в БД
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = OrderSerializer


class ImgProductViewSet(viewsets.ModelViewSet):
    queryset = ImgProduct.objects.all() # объекты клиента в БД
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = ImgProductSerializer


class LoginViewSet(viewsets.ModelViewSet):
    queryset = Login.objects.all() # объекты клиента в БД
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = LoginSerializer


class TableOrdersViewSet(viewsets.ModelViewSet):
    queryset = TableOrders.objects.all() # объекты клиента в БД
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = TableOrdersSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all() # объекты клиента в БД
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = RatingSerializer